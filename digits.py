import random
random.seed()
from math import *
from time import perf_counter
from decimal import *




def floor(n):
  return n-(n%1)
  
  
def ceil(n):
  return floor(n)+1
  



mult = 1
getcontext().prec = 64*mult

Dec = Decimal
d = Decimal

  
  
  
def getDigits(p):
  results = []
  #i = 0
  i = d(str(len(str(floor(p)))-1))
  while i >= 0:
    results.append((floor((p/(10**i))%d('10')))*(10**i))
    i = i - 1
  
  return results

  
  
def rawDigits(p):
  results = []
  #i = 0
  i = d(str(len(str(floor(p)))-1))
  while i >= 0:
    results.append((floor((p/(10**i))%d('10'))))
    i = i - 1
  
  return results
  
#sumdigits 
def sumD(p):
  results = rawDigits(p)
  return sum(results)

  