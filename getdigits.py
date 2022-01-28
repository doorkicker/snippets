from math import *
from decimal import *
d = Decimal

#returns the digits of p
def getDigits(p):
  results = []
  #i = 0
  i = d(str(len(str(floor(p)))-1))
  while i >= 0:
    results.append((floor((p/(10**i))%d('10')))*(10**i))
    i = i - 1
  
  return results
