// https://www.hackerrank.com/challenges/sherlock-and-queries
var trivialSolution = function (N, M, A, B, C) {
    var mod = 1000000007;
    for (var i=1; i<=M; i++) {
        for (var j=1; j<=N; j += 1) {
            if (j % B[i] === 0) {
                A[j] = ((A[j] % mod) * (C[i] % mod)) % mod;
            }
        }
    }
    return A;
}

var smartSolution = function (N, M, A, B, C) {
    var mod = 1000000007;
    
    var bCounts = {};
    for (var i=1; i<M+1; i++) {
        if (B[i] in bCounts) {
            bCounts[B[i]] = (bCounts[B[i]] * C[i]) % mod;
        }
        else {
            bCounts[B[i]] = C[i];
        }  
    }
    
    for (var i=1; i<N+1; i++) {
        for (var j=1; j < Math.floor(N/i) + 1; j++) {
            if (i in bCounts) {
                l = (A[i*j] * bCounts[i]) % mod;
                A[i*j] = l;
            }
        }
    }
    return A;
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

var stringToIntArray = function (str) {
    return str.split(' ').map(function( i ) {
        return parseInt(i, 10);
    });
}

process.stdin.on('end', function () {
    _input_array = _input.split("\n");
    var t = stringToIntArray(_input_array[currentline]);
    var N = t[0];
    var M = t[1];
    currentline += 1;
    
    var A = stringToIntArray(_input_array[currentline]);
    A.unshift(0);
    currentline += 1;
    
    var B = stringToIntArray(_input_array[currentline]);
    B.unshift(0);
    currentline += 1;
    
    var C = stringToIntArray(_input_array[currentline]);
    C.unshift(0);
    currentline += 1;
    
    var res = smartSolution(N, M, A, B, C);
    res.shift();
    process.stdout.write(res.join(' '));
});