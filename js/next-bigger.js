// https://www.codewars.com/kata/55983863da40caa2c900004e
function nextBigger(n){
  var results = [];
  var digits = (""+n).split("");
  var nextBig = -1

  var permutations = permute(digits)

  function permute(arr, memo) {
    var cur, memo = memo || [];

    for (var i = 0; i < arr.length; i++) {
      cur = arr.splice(i, 1);
      if (arr.length === 0) {
        results.push(memo.concat(cur));
      }
      permute(arr.slice(), memo.concat(cur));
      arr.splice(i, 0, cur[0]);
    }

    return results;
  }

  for (var i = 0; i < permutations.length; i++) {
    var val = '';

    for (var j = 0; j < permutations[i].length; j++) {
      val += permutations[i][j];
    }

    val = parseInt(val);

    if ((nextBig == -1 && val > n) || (nextBig > val > n )) {
      nextBig = val
    }
  }
  return nextBig
}
