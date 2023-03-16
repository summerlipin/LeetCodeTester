# LeetCodeTester
#### Video Demo: https://youtu.be/3z95gI7b_r8
#### Description:
This is a LeetCodeTester 1.0
What it can do for now:
* Load the newest LeetCodeQuestions for topics of Top Interview Questions and Top Liked Questions and test for it!

What are the features are expected for 2.0:
* Save the questions and solutions into DB
* Timing the efficiency of the code for further analysis and generate report

What are the features are expected for 3.0:
* Online debug version

The reason for creating this project:
I personally love scraping the web content(It feels like digging secrets), and I also want to practice my Python skill. Furthermore, I want to (ultimately) create a free leetcode online debugger which can help me and others to conquer more leetcode questions easily!

Skills:
Backend language: Python
Backend framework: Flask
Frontend language: Html, CSS, Javascript
Frontend framework: Bootstrap
(with Jinja template engine)

The project layout:
<img alt="ProjectImage" src="/static/img/ProjectImage.png">

What I learned from Jinja:
Jinja is not a language! It's a template engine! I like Jinja a lot. It's easy to pick up because it allows me to write code similar to Python syntax. There are two things about Jinja that I need to look up for my project are "auto increment counter" and "url_for".
For the recent version of Jinja, we can just {% set count = count + 1 %} due to the scoping rules.However, we can use this syntax {% set __ = count.append(1) %} to do the counter!
As for url_for, if we want to send parameters values back to our Flask but without using a form, we can se our anchor href like this {{url_for("function name in your app.py", parameter1 = value1, parameter2 = value2 ) }}

What I learned from Flask:
We call it Micro-framework because it's light and can be set up really quick.
For now I just know some basic but important things about Flask.
1. After import Flask, we need to create an instance by app = Flask(\__name__). The argument is actully the name of the app's name or package. But we usually input it \__name__ for most cases.
2. We use @app.route() to tell which URL we should go to and the entry will be @app.route("/")
3. We can also return a function for the route and make it redirect to other pages.

What I learned from Python:
There is one technique I would like to share which is "redirect sys.stdout to a file"

Fisrt, we can store sys.stdout for a variable
(we need to remember where we should direct back before we redirect the ouput)

**org_stdout = sys.stdout**

Second, open a file and redirect standard output to the file

**sys.stdout = f = open("file.txt", "w")**

execute the code, the output will redirect to "file.txt"

**exec(str(inCode))**

redirect standard output back to org_stdout (redirect output back to the console)

**sys.stdout = org_stdout**

read the executed output

**outPut = open("file.txt", "r").read()**


* 2.0 est. release date 2023/4/30
* 3.0 est. release date to be announced (Due to pty dosen't support Windows, try to find a workaround)
* node_modules is for later use