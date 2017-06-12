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

def recoverSecret(triplets: list) -> str:
    """ Other solutions inspired """
    out = list(set([char for triplet in triplets for char in triplet]))

    finished = False
    while not finished:
        finished = True
        for triplet in triplets:
            if out.index(triplet[0]) > out.index(triplet[1]):
                swap(out, triplet[0], triplet[1])
                finished = False
            if out.index(triplet[1]) > out.index(triplet[2]):
                swap(out, triplet[1], triplet[2])
                finished = False
    return ''.join(out)


def swap(l: list, a: str, b: str):
    l.remove(a)
    l.insert(l.index(b), a)


def recoverSecret_traditional(triplets):
    """ A more traditional iterative approach"""
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
