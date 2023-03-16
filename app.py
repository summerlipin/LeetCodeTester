import sys
from flask import Flask, render_template, request, session
import requests
from flask_assets import Environment
import json
import sqlite3

# Configure application
app = Flask(__name__, instance_relative_config=False)
assets = Environment(app)
app.config.from_object('config') # this is for bundling javascript, for later use


# set sectet_key (require by flask)
app.secret_key = "leetCodeSecrete"

# declare variables
totalLineNum = 0
questionContent = ""
tileSlugs = []


# Assigning header (won't change on pages)
_header = {
    'authority' : 'leetcode.com',
    'accept': '*/*',
    'scheme': 'https',
    'path': '/graphql/'
}

@app.route("/")
def index():
    return homepage(_topic = "")

@app.route("/index/<_topic>", methods=["GET", 'POST'])
def homepage(_topic=""):
    if _topic == "":
        _topic = "top-interview-questions"
    try:
        # region Usage of request.post
        '''
        requests.post(url, data={key: value}, json={key: value},
        headers={key:value}, args)
        *(data, json, headers parameters are optional.)
        '''
        #endregion

        # Assigning post data
        _data = {
            "query": "\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ",
            "variables": {
                "categorySlug": "",
                "skip": 0,
                "limit": 1000,
                "filters": {
                    "listId": _topic
                }
            }
        }

        # Get top-interview-questions from leetcode
        objResponse = requests.post("https://leetcode.com/graphql/", json = _data, headers = _header)
        jsResponse = json.loads(objResponse.content)
        jsQuetions = jsResponse["data"]["problemsetQuestionList"]["questions"]
        # Reformat topic and install to session in order to show on homepage
        _topic = " ".join(_topic.split('-')).upper()
        session["topic"] = _topic
        return render_template("index.html", data = jsQuetions, topic = _topic)
    except:
        # if something went wrong, render user to error page
        return render_template("wrong.html")

@app.route("/sandbox/<titleSlug>/<title>", methods=["GET", 'POST'])
def sandBox(titleSlug = "", title = ""):
    inCode = ""
    outPut = ""
    if request.method == "POST":
        try:
            # Get input code and how many lines of code
            inCode = request.form.get("inCode")
            totalLineNum = request.form.get("totalLines")
            if totalLineNum != '':
                session["totalLineNum"] = totalLineNum
            # redirect sys.stdout to a file
            # store sys.stdout for later
            org_stdout = sys.stdout
            # open a file and redirect standard output to the file
            sys.stdout = f = open("file.txt", "w")
            inCode = "" if inCode == None else inCode
            # execute the code, the output will redirect to "file.txt"
            exec(str(inCode))
            # redirect standard output back to org_stdout (redirect output back to the console)
            sys.stdout = org_stdout
            # close the file
            f.close()
            # read the executed output
            outPut = open("file.txt", "r").read()

        except Exception as e:
            # if any error occurs, redirect standard output back to org_stdout
            # and show the error
            org_stdout = sys.stdout
            outPut = e
            pass
        return render_template("sandbox.html", Code = inCode, Result = outPut, totalLineNum = session["totalLineNum"], QContent = session["questionContent"])
    else:
        # Assigning post data
        _data = {
            "query": "\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n  }\n}\n    ",
            "variables": {
                "titleSlug": titleSlug
            }
        }

        # Get top-interview-questions from leetcode
        objResponse = requests.post("https://leetcode.com/graphql/", json = _data, headers = _header)
        jsResponse = json.loads(objResponse.content)
        QuestionContent = jsResponse["data"]["question"]["content"]
        QuestionContent = str(QuestionContent).replace("\n\n", "")
        QuestionContent = QuestionContent.replace("\n", "")

        # Get starting code - python version
        _data = {
            "query": "\n    query questionEditorData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    codeSnippets {\n      lang\n      langSlug\n      code\n    }\n    envInfo\n    enableRunCode\n  }\n}\n    ",
            "variables": {
                "titleSlug": titleSlug
            }
        }

        objResponse = requests.post("https://leetcode.com/graphql/", json = _data, headers = _header)
        jsResponse = json.loads(objResponse.content)
        funName = ""
        for item in jsResponse["data"]["question"]["codeSnippets"]:
            if item["lang"] == "Python":
                inCode = item["code"]
                # get the function name
                funName = inCode[str(inCode).index('Solution'):]
                funName = funName[str(funName).index('def '):]
                funName = funName[funName.index(' ') + 1:funName.index("(")]
                break

        inCode = inCode + '\n#Remmber to add your parameters to test your function\nresult = Solution().' + funName + '()\nprint(result)'
        session["questionContent"] = QuestionContent
        session["totalLineNum"] = len(inCode.split('\n'))
        return render_template("sandbox.html", QContent = QuestionContent, Code = inCode, totalLineNum = session["totalLineNum"])

