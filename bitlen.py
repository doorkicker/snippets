from math import *
from decimal import *

def bitlength(n):
  i = 1
  while floor(n/(2**i)) > 0:
    i = i + 1
    
  print("bit length: " + str(i))
  return i

  
#alternative
def bitlen(p):
  return int(len(bin(int(p))[2:]))

