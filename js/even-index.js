// https://www.codewars.com/kata/5679aa472b8f57fb8c000047
function findEvenIndex(arr)
{
  var left = 0;
  for (var i = 1; i < arr.length; i++) {
    left += arr[i-1];

    var right = 0;
    for (var j = i+1; j < arr.length; j++) {
      right += arr[j];
    }
    if (left == right) return i
  }
  return -1
}
