import random
random.seed()
from math import *
from decimal import *
dec = Decimal



#tries to match our target to a randomized trace
def randomTrace(target, cutoff=1000, accuracy=Dec('0.00000001')):
  i = 0
  while i < cutoff:
    _j = random.randint(0, len(elements)-1)
    _k = random.randint(0, len(elements)-1)
    _l = random.randint(0, len(elements)-1)
    _m = random.randint(0, len(elements)-1)
    _ji = random.randint(-1, 1)
    _ki = random.randint(-1, 1)
    _li = random.randint(-1, 1)
    _mi = random.randint(-1, 1)
    resultStr = "(" + elNames[_j] + "*" + str(_ji) + ")" + "+" "(" + elNames[_k] + "*" + str(_ki) + ")" + "+" "(" + elNames[_l] + "*" + str(_li) + ")" + "+" "(" + elNames[_m] + "*" + str(_mi) + ")"
    result = (elements[_j]*_ji) + (elements[_k]*_ki) + (elements[_l]*_li) + (elements[_m]*_mi) 
    print(str(result))
    print(resultStr)
    if (target)+accuracy >= result and (target)-accuracy <= result:
      print("*** !!!!!!!! ****")
      print("found target trace! : " + resultStr)
      print("ratio: " + str(result/target))
      print("trace: " + resultStr)
      return resultStr
    else:
      i = i + 1
  
  print(" ")
  print("no trace found! try lowering the accuracy or increasing cutoff.")
  return None
 

 
#finds a matching trace for the given target variable
def nTrace(var, acc=d('0.0000001')):
  i = ceil(var)
  
  result = None
  while i > 0:
    result = randomTrace(var-i, 1_000, acc)
    if result != None:
      print(f"nTrace complete. -i: {i}")
      return result
    #else
    result = randomTrace(var+i, 1_000, acc)
    if result != None:
      print(f"nTrace complete. +i: {i}")
      return result
    #else
    i = i + 1
    
  #else
  return None
 