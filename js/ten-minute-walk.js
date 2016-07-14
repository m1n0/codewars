// https://www.codewars.com/kata/54da539698b8a2ad76000228
function isValidWalk(walk) {
  var x = 0;
  var y = 0;

  for (var i = 0; i < walk.length; i++) {
    if (walk[i] == 'n') y += 1
    if (walk[i] == 's') y += -1
    if (walk[i] == 'e') x += 1
    if (walk[i] == 'w') x += -1
  }
  return (x == 0 && y == 0 && walk.length == 10) ? true : false;
}
