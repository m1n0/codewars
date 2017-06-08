# https://www.codewars.com/kata/soundex
import re
def soundex(name):
    remove_chars = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = [
        ['b', 'f', 'p', 'v'],
        ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
        ['d', 't'],
        ['l'],
        ['m', 'n'],
        ['r'],
    ]

    words = []
    # Repeat the algo for each word in provided name.
    for word in name.split(' '):
        out = []
        # 1. Get first letter and get rid of 'w' and 'h'
        first_char = ''
        for i ,c in enumerate(word):
            try:
                int(c)
            except ValueError:
                first_char = c if not first_char else first_char
            if c in ['w', 'h'] and i != 0:
                pass
            else:
                out.append(c)
        # Reset vars
        word = out
        out = []

        # 2. Replace consonants with numbers.
        for c in word:
            lower_case = c.lower()
            found = False
            for i, forbidden_set in enumerate(consonants):
                found = False
                if lower_case in forbidden_set:
                    out.append(i + 1)
                    found = True
                    break
            if not found:
                out.append(c)


        # 3 Get rid of double digits
        word = re.sub(r'(\d)\1+', r'\1', ''.join(str(c) for c in out))
        # Reset vars
        out = []

        # 4. Get rid of forbidden chars.
        out.append(word[0])
        for c in word[1:]:
            if c in remove_chars:
                pass
            else:
                out.append(c)

        # 5. Make sure first char is char and not int.
        try:
            int(out[0])
        except ValueError:
            pass
        else:
            out[0] = first_char

        # Join chars into a word, pad or trim and capitalize.
        words.append(''.join(str(c) for c in out).ljust(4, '0')[0:4].capitalize())

    return ' '.join(words)
