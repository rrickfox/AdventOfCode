var contents;

function readSingleFile(evt) {
  //Retrieve the first (and only!) File from the FileList object
  var f = evt.target.files[0]; 

  if (f) {
    var r = new FileReader();
    r.onload = function(e) { 
     var content = e.target.result;                  
      contents = content.split("\r\n");
      //console.log(contents); 
      aoc();
    }
    r.readAsText(f);
  } else { 
    alert("Failed to load file");
  }
}

function aoc() {                                
  var letters = "abcdefghijklmnopqrstuvwxyz";
  var sets = new Array(contents.length);

  for(let i = 0; i < contents.length; i++) {  
    for(let j = i + 1; j < contents.length; j++) {
      for(let k = 0; k < contents[j].length; k++) {
        if(contents[j].slice(0, k) + contents[j].slice(k+1, contents[j].length) == contents[i].slice(0, k) + contents[i].slice(k+1, contents[i].length)) {
          alert(contents[j].slice(0, k) + contents[j].slice(k+1, contents[j].length));
          return 0;
        }
      }  
    }
    
    console.log("==========");
  }
}

document.getElementById("fileinput").addEventListener("change", readSingleFile, false);