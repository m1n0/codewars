# https://www.codewars.com/kata/the-hunger-games-zoo-disaster
def who_eats_who(zoo):
    rules = {
        'antelope': ['grass'],
        'big-fish': ['little-fish'],
        'bug': ['leaves'],
        'bear': ['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],
        'chicken': ['bug'],
        'cow': ['grass'],
        'fox': ['chicken', 'sheep'],
        'giraffe': ['leaves'],
        'lion': ['antelope', 'cow'],
        'panda': ['leaves'],
        'sheep': ['grass'],
    }

    zoo = zoo.split(',')

    out = []
    out.append(",".join(zoo))
    done = False
    while not done:
        done = True
        for i, eater in enumerate(zoo):
            if eater in rules:
                if i != 0:
                    if zoo[i - 1] in rules[eater]:
                        out.append("{} eats {}".format(eater, zoo[i - 1]))
                        del(zoo[i - 1])
                        done = False
                        break
                if i != (len(zoo) - 1):
                    if zoo[i + 1] in rules[eater]:
                        out.append("{} eats {}".format(eater, zoo[i + 1]))
                        del(zoo[i + 1])
                        done = False
                        break

    out.append(",".join(zoo))
    return out

input = "fox,bug,chicken,grass,sheep"
input = "bug,chicken,grass,sheep"
input = "bear,big-fish,lion,cow,bug,leaves"
print(who_eats_who(input))
