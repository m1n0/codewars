// https://www.codewars.com/kata/human-readable-time
function humanReadable(s) {
  return  pad(parseInt(s / 3600)) + ":" +
          pad(parseInt(s / 60 % 60)) + ":" +
          pad(parseInt(s % 60))
}

function pad(n) {
  return ("0" + n).slice(-2)
}
