// https://www.codewars.com/kata/unique-in-order/javascript
var uniqueInOrder=function(iterable){
  var prev = "";
  var res = [];

  for (var i = 0, len = iterable.length; i < len; i++) {
    if (iterable[i] != prev) {
      res.push(iterable[i]);
      prev = iterable[i];
    }
  }

  return res;
}
