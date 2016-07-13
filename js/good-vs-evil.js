// https://www.codewars.com/kata/52761ee4cffbc69732000738
function goodVsEvil(good, evil){
  var goodMap = [1, 2, 3, 3, 4, 10];
  var evilMap = [1, 2, 2, 2, 3, 5, 10];

  goodSum = sum(good.split(' '), goodMap);
  evilSum = sum(evil.split(' '), evilMap);

  if (goodSum == evilSum) {
    return 'Battle Result: No victor on this battle field';
  }
  else if (goodSum > evilSum) {
    return 'Battle Result: Good triumphs over Evil';
  }
  else {
    return 'Battle Result: Evil eradicates all trace of Good';
  }
}

function sum(army, map) {
  var sum = 0;
  for (var i = 0; i < army.length; i++) {
    sum += parseInt(army[i]) * parseInt(map[i]);
  }

  return sum;
}
