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
  var sets = [];
  var letters = "abcdefghijklmnopqrstuvwxyz";
  var twice = 0, three = 0;
  for(let i = 0; i < contents.length; i++) {  
    for(let i = 0; i < letters.length; i++) {
      sets[letters.charAt(i)] = 0;    
    }
    console.log(JSON.stringify(sets));
    let string = contents[i];
    for(let j = 0; j < string.length; j++) {
      sets[string.charAt(j)]++;  
    }
    console.log(JSON.stringify(sets));
    let alreadyTwice = false, alreadyThree = false;
    for(let x = 0; x < letters.length; x++) {
      if(sets[letters.charAt(x)] == 2 && !alreadyTwice) {
        twice++;
        alreadyTwice = true;
      }
      if(sets[letters.charAt(x)] == 3 && !alreadyThree) {
        three++;
        alreadyThree = true;
      }
    }
    console.log("twice: " + twice + " three: " + three);
    console.log("==========");
  }
  alert(twice * three);
}

document.getElementById("fileinput").addEventListener("change", readSingleFile, false);