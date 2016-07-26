# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee
def ip_to_int32(ip):
  res = ''
  for part in ip.split('.'):
      b = bin(int(part))[2:]
      res += "%08d" % (int(b))

  return(int(res, 2));
