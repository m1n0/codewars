// https://www.codewars.com/kata/decode-the-morse-code
decodeMorse = function(morseCode){
  function decodeLetter(l) {
    return MORSE_CODE[l];
  }

  function decodeWord(w) {
    return w.split(' ').map(decodeLetter).join('')
  }

  return morseCode.trim().split('   ').map(decodeWord).join(' ');
}
