# https://www.codewars.com/kata/53368a47e38700bd8300030d
def namelist(names):
    l = len(names)
    if (l == 0): return ''
    elif (l == 1): return names[0]['name']
    else: return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
