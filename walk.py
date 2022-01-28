import random
import os
import sys
random.seed()
from math import *
from decimal import *

#could probably replace these with zip
ops = ["+", "-", "*", "/", "*2", "/2", "*3", "/3", "*4", "/4", "**0.5", "**2", "**3", "**4", "1/", "*-1"]
#walks a list of elements, trying to find an identity or series of ops that matches a given target

#total random walks, min is the minimum length of the chain, max is the maximum length
def walk(start, min, max, reps, target, elements, elNames, accuracy=Dec('0.00000001'), jiggle=False, ops=ops):
  partial = start
  temp = partial
  i = 0
  el = start
  oplist = [] #used to build operations string
  while i < reps:
    j = 0
    k = random.randint(min, max)
    
    #begin initial random walk
    try:
      stepStr = "(" + elNames[elements.index(start)] + ")" #could cause issues if the value isn't in the list
    except:
      stepStr = "(" + str(start) + ")"
    partial = start
    temp = partial
    while j <= k:
      m = random.randint(0, len(elements)-1)
      el = elements[m]
      op = ops[random.randint(0, len(ops)-1)]
      if jiggle == True:
        jiggle = (random.randint(1, 10)/10)*random.randint(-1, 1)
      else:
        jiggle = 0
      try:
        if op == "+":
          temp = Dec.copy_abs(partial + el)
          #then check to see if it is target
          #then log the new operation in the list
          partial = temp
          stepStr = "(" + stepStr + "+" + elNames[m] + ")"
        if op == "-":
          temp = Dec.copy_abs(partial - el)
          partial = temp
          stepStr = "Dec.copy_abs(" + stepStr + "-" + elNames[m] + ")"
        if op == "*":
          temp = Dec.copy_abs(partial * el)
          partial = temp
          stepStr = "(" + stepStr + "*" + elNames[m] + ")"
        if op == "/":
          temp = partial / el
          partial = temp
          stepStr = "(" + stepStr + "/" + elNames[m] + ")"
        if op == "*2":
          temp == partial * 2
          partial = temp
          stepStr = "(" + stepStr + "*2" + ")"
        if op == "/2":
          temp = partial / 2
          partial = temp
          stepStr = "(" + stepStr + "/2" + ")"
        if op == "*3":
          temp = partial * 3
          partial = temp
          stepStr = "(" + stepStr + "*3" + ")"
        if op == "/3":
          temp = partial / 3
          partial = temp
          stepStr = "(" + stepStr + "/3" + ")"
        if op == "*4":
          temp = partial * 4
          partial = temp
          stepStr = "(" + stepStr + "*4" + ")"
        if op == "/4":
          temp = partial / 4
          partial = temp
          stepStr = "(" + stepStr + "/4" + ")"
        if op == "**0.5":
          temp = Dec.copy_abs(partial**Dec(Dec(0.5)+jiggle))
          partial = temp
          stepStr = "Dec.copy_abs(" + stepStr + "**(0.5+" + str(jiggle) + ")" + ")"
        if op == "**2":
          temp = Dec.copy_abs(partial**Dec(2+jiggle))
          partial = temp
          stepStr = "(" + stepStr + "**(2+" + str(jiggle) + ")" + ")"
        if op == "**3":
          temp = Dec(Dec.copy_abs(partial**Dec(3+jiggle))) #Dec.copy_abs may cause issues here
          partial = temp
          stepStr = "(" + stepStr + "**(3+" + str(jiggle) + ")" + ")"
        if op == "**4":
          temp = partial**(4+jiggle)
          partial = temp
          stepStr = "(" + stepStr + "**(4+" + str(jiggle) + ")" + ")"
        if op == "sublimate":
          temp = sublimate(partial)
          partial = temp
          stepStr = "(sublimate(" + stepStr + "))"
        if op == "1/":
          temp = (1/partial)+1
          partial = temp
          stepStr = "((1/" + stepStr + ")+1)"
        if op == "*-1":
          temp = partial*-1
          partial = temp
          stepStr = "(" + stepStr + "*-1)"
        if op == "*10":
          temp = partial*10
          partial = temp
          stepStr = "(" + stepStr + ")"
        if op == "/10":
          temp = partial/10
          partial = temp
          stepStr = "(" + stepStr + "/10)"
        if op == "10/":
          temp = 10/partial
          partial = temp
          stepStr = "(10/" + stepStr + ")"
        
        print(str(partial))
        print(str(stepStr))
        if (target)+accuracy >= partial and (target)-accuracy <= partial:
          print("FOUND TARGET!")
          print(stepStr)
          print("partial: " + str(partial))
          #should just check to see if it is a factor instead
          return partial, stepStr
      except:
        pass
      
      
      j = j + 1
    print(stepStr)
    print("Final partial:" + str(partial))
    i = i + 1
  
  print("no target found!")
  return None
  

  
  
  

def walkAll(min, max, reps, target, elements, elNames, accuracy=Dec('0.00000001'), jiggle=False, ops=ops):
  i = 0
  results = []
  result = None
  while i < len(elements):
    result = walk(elements[i], min, max, reps, target, elements, accuracy, jiggle, ops)
    if result != None:
      results.append(result)
      result = None
    
    i = i + 1
  
  return results


  
  

  
#tries to match our target to a randomized trace
def randomTrace(target, elements, elNames, cutoff=1000, accuracy=Dec('0.00000001')):
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