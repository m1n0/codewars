// https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
var maxSequence = function(arr){
  var max = 0;

  for (var i = 0; i < arr.length; i++) {
    for (var j = i; j >= 0; j--) {
      var currentSum = 0;
      for (var k = i; k >= j; k--) {
        currentSum += arr[k];
      }
      
      if (currentSum > max) max = currentSum;
    }
  }

  return max;
}
