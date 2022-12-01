var contents;

function readSingleFile(evt) {
  //Retrieve the first (and only!) File from the FileList object
  var f = evt.target.files[0]; 

  if (f) {
    var r = new FileReader();
    r.onload = function(e) { 
     var content = e.target.result;
      alert( "Got the file.\n" 
            +"name: " + f.name + "\n"
            +"type: " + f.type + "\n"
            +"size: " + f.size + " bytes"
      );                          
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
  var freq = 0, length = contents.length, twice = false;
  var done = [freq];
  for(var i = 0; twice == false; i++) {
    freq += parseInt(contents[i]);
    console.log(contents[i]);
    console.log(freq);
    console.log("==========");
    if(done.includes(freq)) {
      twice = true;
    } else {
      done.push(freq);
    }                   
    if(i == length - 1) {
      i = -1;
      continue;
    }
  }
  alert(freq);      
}

document.getElementById("fileinput").addEventListener("change", readSingleFile, false);