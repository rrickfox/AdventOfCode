var contents = [];
var maxX = 0;
var maxY = 0;
var xy;
var twice = 0;

function readSingleFile(evt) {
  //Retrieve the first (and only!) File from the FileList object
  var f = evt.target.files[0]; 

  if (f) {
    var r = new FileReader();
    r.onload = function(e) { 
      var content = e.target.result;                  
      var temp = content.split("\r\n");
      for(let i = 0; i < temp.length; i++) {
        let x = temp[i].split(" ");
        let topleft = x[2].split(",");  
        let left = parseInt(topleft[0]);
        let top = parseInt(topleft[1].split(":")[0]);
        let dim = x[3].split("x");
        let width = parseInt(dim[0]);
        let height = parseInt(dim[1]);
        contents[i] = [left, top, width, height];
        if(left + width > maxX) {
          maxX = left + width;
        }
        if(top + height > maxY) {
          maxY = top + height;
        }
      }
      
      xy = new Array(maxX);
      
      for (var i = 0; i < xy.length; i++) {
        xy[i] = [];
      }
      //console.log(contents); 
      aoc();
    }
    r.readAsText(f);
  } else { 
    alert("Failed to load file");
  }
}

function aoc() {  
  for(let i = 0; i < maxX; i++) {
    for(let j = 0; j < maxY; j++) {
      xy[i][j] = 0;
    }
  }
                             
  for(var i = 0; i < contents.length; i++) {
    for(var x = 0; x < contents[i][2]; x++) {
      for(var y = 0; y < contents[i][3]; y++) {
        if(xy[contents[i][0] + x][contents[i][1] + y] == 1) {
          twice++;  
        }
        xy[contents[i][0] + x][contents[i][1] + y]++;
      }
    }
  }
  
  var used;
  for(var i = 0; i < contents.length; i++) {
    used = false;
    for(var x = 0; x < contents[i][2]; x++) {
      for(var y = 0; y < contents[i][3]; y++) {
        if(xy[contents[i][0] + x][contents[i][1] + y] > 1) {
          used = true;
        }  
      }
    }
    if(!used) {
      alert(i + 1);
      return 0;
    }
  }
}

document.getElementById("fileinput").addEventListener("change", readSingleFile, false);