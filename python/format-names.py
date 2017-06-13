# https://www.codewars.com/kata/53368a47e38700bd8300030d
def namelist(names):
    if len(names) == 0: return ''
    if len(names) == 1: return names[0]['name']
    if len(names) > 1: return ' & '.join([(", ".join([person['name'] for person in names][:-1])), names[-1]['name']])

names = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
print(namelist(names))
