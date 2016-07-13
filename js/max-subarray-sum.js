// https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
var maxSequence = function(arr){
  var max = 0;

  for (var i = 0; i < arr.length; i++) {
    var currentSum = 0;
    for (var j = i; j >= 0; j--) {
      currentSum += arr[j];
      if (currentSum > max) max = currentSum;
    }
  }
  return max;
}
