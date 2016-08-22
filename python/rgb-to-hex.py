# https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r, g, b):
    def clamp(x):
        return max(0, min(x, 255))

    return ('%02x%02x%02x' % (clamp(r), clamp(g), clamp(b))).upper()
