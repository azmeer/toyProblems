process.stdin.resume();
process.stdin.setEncoding('utf-8');

var __input_stdin = "";
var __input_stdin_array = "";
var __input_currentline = 0;

process.stdin.on('data', function (data) {
    __input_stdin += data;
});

/*
 * Complete the function below.
 */
function oddNumbers(l, r) {
  const results = [];
  for (let i = l; i <= r; i++) {
    if (Math.abs(i % 2) === 1) results.push(i);
  }
  return results;
}

var fs = require('fs');
var wstream = fs.createWriteStream(process.env.OUTPUT_PATH);
process.stdin.on('end', function () {
    __input_stdin_array = __input_stdin.split("\n");
    var res;

    var _l = parseInt(__input_stdin_array[__input_currentline].trim(), 10);
    __input_currentline += 1;
    
    var _r = parseInt(__input_stdin_array[__input_currentline].trim(), 10);
    __input_currentline += 1;
    
    res = oddNumbers(_l, _r);
    for(var res_i=0; res_i < res.length; res_i++) {
        wstream.write(res[res_i]+"\n");
    }
    
    wstream.end();
});
