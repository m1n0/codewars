// https://www.codewars.com/kata/54df2067ecaa226eca000229
function f(n){
  if (!isPositiveInteger(n)) {
    return false;
  }

  return (n*(n+1)) / 2;
};

function isPositiveInteger(s) {
    var i = +s;
    if (i < 0) return false;
    if (i != ~~i) return false;
    if (i <= 0) return false;
    return true;
}
