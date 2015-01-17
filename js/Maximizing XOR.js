process.stdin.resume();
process.stdin.setEncoding('ascii');

var _input_stdin = "";
var _input_array = "";
var currentLine = 0;

process.stdin.on('data', function (data) {
    _input_stdin += data;
});

function maxXor(l, r) {
    var max = 0;
    for (i = l; i <= r; i++) {
        for (j = l; j<= r; j++) {
            var xor = i ^ j;
            if (xor > max) {
                max = xor;
            }
        }
    }
    return max;
};

process.stdin.on('end', function () {
    _input_array = _input_stdin.split("\n");
    var res;
    var _l = parseInt(_input_array[currentLine].trim(), 10);
    currentLine += 1;
    
    var _r = parseInt(_input_array[currentLine].trim(), 10);
    currentLine += 1;
    
    res = maxXor(_l, _r);
    process.stdout.write(""+res);
});
