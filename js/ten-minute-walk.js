// https://www.codewars.com/kata/54da539698b8a2ad76000228
function isValidWalk(walk) {
  var x = 0;
  var y = 0;

  for (var i = 0; i < walk.length; i++) {
    switch (walk[i]) {
      case 'n': y++; break
      case 's': y--; break
      case 'e': x++; break
      case 'w': x--; break
    }
  }
  return x == 0 && y == 0 && walk.length == 10
}
