// https://www.codewars.com/kata/5226eb40316b56c8d500030f
function pascalsTriangle(n) {
  var res = []
  var rows = []

  for (var i = 0; i < n; i++) {
    rows[i] = []

    for (var j = 0; j <= i; j++) {
      if (j == 0 || j == i) {
        rows[i][j] = 1;
        res.push(1);
      }
      else {
        var num = rows[i-1][j-1] + rows[i-1][j]
        rows[i][j] = num
        res.push(num);
      }
    }
  }

  return res;
}
