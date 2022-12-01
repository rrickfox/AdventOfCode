var contents = [];
var guards = [], allguards = [];

function readSingleFile(evt) {
  //Retrieve the first (and only!) File from the FileList object
  var f = evt.target.files[0]; 

  if (f) {
    var r = new FileReader();
    r.onload = function(e) { 
      var content = e.target.result;                  
      let temp = content.split("\r\n");
      //console.log(contents); 
      for(var i = 0; i < temp.length; i++) {
        let dt = temp[i].split(" ");
        let date = dt[0].split("-");
        let year = date[0].slice(1);
        let time = dt[1].split(":");
        let min = time[1].slice(0, -1);
        var action, guard = 0;
        if(dt[2] == "Guard") {
          action = 0;
          guard = parseInt(dt[3].slice(1));  
        } else if(dt[2] == "falls") {
          action = 1;
        } else if(dt[2] == "wakes") {
          action = 2;
        }
        contents[i] = [parseInt(year), parseInt(date[1]), parseInt(date[2]), parseInt(time[0]), parseInt(min), action, guard];
      }
      aoc();
    }
    r.readAsText(f);
  } else { 
    alert("Failed to load file");
  }
}

function swap(a, b){
  var temp = contents[a];
  contents[a] = contents[b];
  contents[b] = temp;
}

function cut(start, end, index) {
  var i = start;
  var j = end - 1;
  var pivot = contents[end][index];
  
  do {
    while(contents[i][index] < pivot && i < end - 1) {
      i++;
    }
    
    while (contents[j][index] >= pivot && j > start) {
      j--;  
    }
    
    if(i < j) {
      swap(i, j);
    }
  } while(i < j);
  
  if(contents[i][index] >= pivot) {
    swap(i, end);
  }
  
  return i;
}

function quicksort(start, end, index) {
  if(start < end) {
    var pivot = cut(start, end, index);
    quicksort(start, pivot - 1, index);
    quicksort(pivot + 1, end, index);
  }
}

function aoc() {
  quicksort(0, contents.length - 1, 1); 
  var index = 0, last = contents[0][1];
  for(var i = 0; i < contents.length; i++) {
    if(contents[i][1] != last) {
      quicksort(index, i-1, 2);
      index = i;
      last = contents[i][1];
    } else if(i == contents.length - 1) {
      quicksort(index, i, 2);
      index = i;
      last = contents[i][1];
    }    
  }
  index = 0;
  last = contents[0][2];
  for(var i = 0; i < contents.length; i++) {
    if(contents[i][2] != last) {
      quicksort(index, i-1, 3);
      index = i;
      last = contents[i][2];
    } else if(i == contents.length - 1) {
      quicksort(index, i, 3);
      index = i;
      last = contents[i][2];
    }    
  }
  index = 0;
  last = contents[0][3];
  for(var i = 0; i < contents.length; i++) {
    if(contents[i][3] != last) {
      quicksort(index, i-1, 4);
      index = i;
      last = contents[i][3];
    } else if(i == contents.length - 1) {
      quicksort(index, i, 4);
      index = i;
      last = contents[i][3];
    }    
  }
  
  var lastguard = 0, lastminute = 0;;
  for(var i = 0; i < contents.length; i++) {
    if(contents[i][5] === 0) {
      if(guards["#" + contents[i][6]] !== undefined) {
        guards["#" + contents[i][6]] = 0;
        allguards.push("#" + contents[i][6]);
      }
      lastguard = contents[i][6];
    } else {
      if(contents[i][5] == 1) {
        lastminute = contents[i][4];  
      } else if(contents[i][5] == 2) {
        guards["#" + lastguard] += (contents[i][4] - 1) - lastminute
      }
    }  
  }
  
  var max = 0;
  var maxguard;
  for(var i = 0; i < allguards.length; i++) {
    if(guards[allguards[i]] > max){
      max = guards[allguards[i]];
      maxguard = allguards[i];
    }
  }
  
  alert(max);
  alert(maxguard); 
}

document.getElementById("fileinput").addEventListener("change", readSingleFile, false);