secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

def recoverSecret(triplets):
    out = ''
    for triplet in triplets:
        for c in triplet:
            i = out.find(c)
            if i == -1:
                out += c

    finished = False
    while not finished:
        finished = True
        for triplet in triplets:
            # 0
            index_0 = out.find(triplet[0])
            index_1 = out.find(triplet[1])
            while index_0 > index_1:
                finished = False
                out = swap(out, index_0, index_0 - 1)
                index_0 = out.find(triplet[0])
                index_1 = out.find(triplet[1])

            # 2
            index_1 = out.find(triplet[1])
            index_2 = out.find(triplet[2])
            while index_1 > index_2:
                finished = False
                out = swap(out, index_1, index_1 - 1)
                index_1 = out.find(triplet[1])
                index_2 = out.find(triplet[2])

    return out

def swap(string, i, j):
    chars = list(string)
    chars[i], chars[j] = chars[j], chars[i]
    return "".join(chars)


print(recoverSecret(triplets))
