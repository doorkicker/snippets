import random
import os
import sys
random.seed()
from math import *
from time import perf_counter
from decimal import *
Dec = Decimal
d = Decimal



#could probably replace these with zip
#elNames = [] #names of your variables
#elements = [] #values of your variables

#generate determinates of elements
def determine(elements, elNames, fileName="determinants"):
  i = 0
  j = 0
  k = 0
  l = 0
  fileCount = 0
  #results = [None]*1_000_000
  results = []
  resultNames = []
  startTime = perf_counter()
  while i < len(elements):
    print("working: " + str((((i+1)/len(elements))*100))[:5] + "% done")
    print("new elements: " + str(len(results)))
    j = 0
    while j < len(elements):
      k = 0
      while k < len(elements):
        l = 0
        while l < len(elements):
          results.append((elements[i]*elements[j]) - (elements[k]*elements[l]))
          #results[(i*j*k)+l] = (elements[i]*elements[j]) - (elements[k]*elements[l])
          #resultNames.append("(" + elNames[i] + "*" + elNames[j] + ")" + "-" + "(" + elNames[k] + "*" + elNames[l] + ")")

          #if str(results[len(results)-1:]) != [None]:
          if len(results) >= 1_000_000:
            #open a new file, write out the results, close file and continue
            f = open(fileName+str(fileCount)+".txt", "a")
            #print("first result: " + str(results[0]))
            print("writing intermediate results to file...")
            for result in results:
              f.write(str(result)[:64] + "\n")
            f.close()
            print("done writing. closing stream. allocating fresh list...")
            #results = [None]*1_000_000 #reset results and continue
            results = []
            fileCount = fileCount + 1
          
          l = l + 1
        k = k + 1
      j = j + 1
    i = i + 1
  
  #return results, resultNames
  #do a final write of results:
  f = open(fileName+"Final.txt", "a")
  print("DONE. writing remaining determinants to determinants.txt file...")
  for result in results:
    f.write(str(result)[:64] + "\n")
  f.close()
  print("time: " + str(perf_counter() - startTime) + "s\n")
  print("Determination calculations COMPLETE!")


  

def determineFast(start, elements, elNames, target, quitAfterFirst=True, accuracy=Dec('0.0000000000000000001')):
  if start > 0:
    start = start * 1_000_000
    i = int(floor((start/(len(elements)**4))*len(elements)))
  else:
    i = 0
  j = 0
  k = 0
  l = 0
  result = None
  results = []
  resultStr = None
  #results = [None]*1_000_000
  startTime = perf_counter()
  while i < len(elements):
    print("working: " + str((((i+1)/len(elements))*100)-0.01)[:5] + "% done")
    j = 0
    while j < len(elements):
      k = 0
      while k < len(elements):
        l = 0
        while l < len(elements):
          result = Dec.copy_abs(Dec(elements[i]*elements[j]) - (elements[k]*elements[l]))
          if target+accuracy >= result and target-accuracy <= result and quitAfterFirst == True:
            print("***** SUCCESS !!! *****")
            print("working: 100% done")
            print("time: " + str(perf_counter() - startTime) + "s\n")
            print("found results!")
            print("result: " + "\n" + str(result))
            resultStr = "(" + elNames[i] + "*" + elNames[j] + ")" + "-" + "(" + elNames[k] + "*" + elNames[l] + ")"
            print("(" + elNames[i] + "*" + elNames[j] + ")" + "-" + "(" + elNames[k] + "*" + elNames[l] + ")")
            return resultStr
          elif target+accuracy >= result and target-accuracy <= result and quitAfterFirst == False:
            print("***** SUCCESS !!! *****")
            print("working: 100% done")
            print("time: " + str(perf_counter() - startTime) + "s\n")
            print("found results!")
            print("result: " + "\n" + str(result))
            resultStr = "(" + elNames[i] + "*" + elNames[j] + ")" + "-" + "(" + elNames[k] + "*" + elNames[l] + ")"
            print("(" + elNames[i] + "*" + elNames[j] + ")" + "-" + "(" + elNames[k] + "*" + elNames[l] + ")")
            results.append(resultStr)
            
          l = l + 1
        k = k + 1
      j = j + 1
    i = i + 1

  print("time: " + str(perf_counter() - startTime) + "s\n")
  if quitAfterFirst == False:
    if len(results) > 0:
      print("Determination calculations COMPLETE! Found determinants!")
      return results
  else:
    print("Determination calculations COMPLETE! No determinants found.")
    return None
