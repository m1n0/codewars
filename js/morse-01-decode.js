// https://www.codewars.com/kata/decode-the-morse-code
decodeMorse = function(morseCode){
  var result = '';
  var words = morseCode.trim().split('   ')

  for (var i = 0; i < words.length; i++) {
    var letters = words[i].split(' ')
    for (var j = 0; j < letters.length; j++) {
      result += MORSE_CODE[letters[j]];
    }
    result += " ";
  }

  return result.trim();
}
