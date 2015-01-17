// https://www.hackerrank.com/challenges/angry-children

function processData(k, array) {
    var min = Number.POSITIVE_INFINITY;
    for (var i=0; i<array.length - k; i++) {
        checkMin = array[i+k-1] - array[i];
        if (checkMin < min) {
            min = checkMin;
        }
    }
    return min;
}

process.stdin.resume();
process.stdin.setEncoding("ascii");

_input = "";
_input_array = "";
array = [];
currentline = 0;

process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on('end', function () {
    _input_array = _input.split("\n");
    var n = parseInt(_input_array[currentline].trim(), 10);
    currentline += 1;
    
    var k = parseInt(_input_array[currentline].trim(), 10);
    currentline += 1;
    
    for (var i=0; i<n; i++) {
        array.push(parseInt(_input_array[currentline].trim(), 10));
        currentline++;
    }
    array.sort(function (a, b) {return a-b});
  
    res = processData(k, array);
    process.stdout.write("" + res);
});
