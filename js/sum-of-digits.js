// https://www.codewars.com/kata/541c8630095125aba6000c00
function digital_root(n) {
  var digits = (""+n).split("");

  var sum = digits.reduce(function(s, d) {
    return s + d;
  });

  var sumDigits = (""+sum).split("");

  if (sumDigits.length == 1) {
    return sum;
  }
  else {
    return digital_root(sum);
  }
}
