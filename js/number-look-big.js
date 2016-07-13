// https://www.codewars.com/kata/5287e858c6b5a9678200083c
function narcissistic( value ) {
  var res = 0;
  str = String(value);

  for (var i = 0; i < str.length; i++) {
    res += Math.pow(str[i], str.length);
  }

  return (res === value) ? true : false;
}
