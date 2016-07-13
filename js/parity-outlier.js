// https://www.codewars.com/kata/5526fc09a1bbd946250002dc
function findOutlier(integers){
  var parity = 0;

  for (var i = 0; i < 3; i++) {
    checkEven(integers[i]) ? parity++ : parity--;
  }

  if (parity > 0) {
    for (var i = 0; i < integers.length; i++) {
      if (!checkEven(integers[i])) return integers[i]
    }
  }
  else if (parity < 0) {
    for (var i = 0; i < integers.length; i++) {
      if (checkEven(integers[i])) return integers[i]
    }
  }
}

function checkEven(n) {
  return (parseInt(String(n).slice(-1)) % 2 == 0) ? true : false;
}
