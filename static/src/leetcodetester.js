const codeSpace = document.querySelector('.codeSpace')
const lineCounter = document.querySelector('.lineCounter')
var numberOfLines = 1
var debugArray = []

if (codeSpace) {
    //  
    codeSpace.addEventListener('keyup', event => {
      numberOfLines = event.target.value.split('\n').length
      lineCounter.innerHTML = Array(numberOfLines).fill('<span class="lineNum"></span>').join('')
      document.getElementById("totalLineNum").value = numberOfLines
    })
    
    // tab for space
    codeSpace.addEventListener('keydown', event => {
        if (event.key === 'Tab') {
          const start = codeSpace.selectionStart
          const end = codeSpace.selectionEnd
      
          codeSpace.value = codeSpace.value.substring(0, start) + '    ' + codeSpace.value.substring(end)
          codeSpace.focus()
          codeSpace.selectionEnd = end + 4
          event.preventDefault()
        }
      })
    
      // debug function for later use
      // lineCounter.addEventListener('click', function(e){
      // var tmpArr = document.querySelectorAll(".lineNum")
      // if (e.target.className == "lineNum") {
      //     var line = [...tmpArr].indexOf(e.target) + 1
      //     if (debugArray.find(item => item == line))
      //     {
      //       debugArray.pop(line)        
      //       e.target.classList.remove("debug")
      //     }
      //     else
      //     {
      //       e.target.classList.add("debug")
      //       debugArray.push(line)
      //     }
      //   }
      // })

}