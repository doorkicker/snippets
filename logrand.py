from math import *
from random import *
random.seed()
#w is just p**0.5

def findRuns(p):
  #i = randint(0, p-1)
  w = p**0.5
  i = randint(0, ceil(w))
  count = 0
  while i < floor(w):
    #i = randint(i+1, p)
    i = randint(i+1, ceil(w))
    count = count + 1
  return count

#running average
def rAvg(p, limit = 100):
  i = 0
  result = 0
  while i < limit:
    result = result + findRuns(p)
    i = i + 1
    print(f"avg: {result/i}")
  
  return result/i
  
  
#what I want to do is run rAvg for a given p
#and then save that. And then increment p, and do it again.
#and then once p hits some limit, stop
#then I want to go through each, iterating them, against each p's actual log
#and once I have all the differences between estimte log and average, I want to average the logs.
#and then like the fast-square doom hack, I can add or multiply in this constant
#and use rAvg to get the logarithms in question



def getConst(p, runs):
  results = []
  i = 2
  while i < p:
    results.append(rAvg(p, runs))
    i = i + 1
  
  actuals = []
  j = 0
  while j < len(results):
    actuals.append(log(j+1)/(results[j]*2))
    j = j + 1
  
  final = sum(actuals)/len(actuals)
  print(f"average constant: {final}") #returns on average, the error inherent in rAvg and findRuns
  return sum(actuals)/len(actuals)
  
    
    
'''
actuals.append(log(p)/(results[j]*2))
Instead of doing it this way I can also do it like 

  actuals.append(log(p)-(results[j]*2))

Assuming log(p) is always above the righthand side.
And then do something like rate.append(actuals[j+1]-actuals[j])
and only iterating while j < p, or j < p-1
(so we dont fall off the edge of the list).

And then we'd figure out the average between them, or the rate
of change. 

This also doesn't factor in the effects of applying *different kinds* of average, like
mean, vs geometric mean.
'''



'''
avg: 2.3
2.3
>>>
>>>
>>>
>>> (2.3*2)-(2.43/2)
3.385
>>> log(697)
6.546785410760524
>>> ((2.3*2)-(2.43/2))*2
6.77
>>> ((2.3*2)-(2.43))*2
4.339999999999999
>>> ((2.3*2)+(2.43))*2
14.059999999999999
>>> ((2.3*2)+(2.43))
7.029999999999999


2.43 seems to be the rate of change avg between all logs under 1000
'''


def getConst(p, runs):
  results = []
  i = 2
  while i < p:
    results.append(rAvg(p, runs))
    i = i + 1
  
  actuals = []
  j = 0
  result = None
  while j < len(results):
    result = abs(log(j)-(results[j]*2))
    if result < 1:
      result = 1/result
    
    actuals.append(result)
    j = j + 1
  
  final = sum(actuals)/len(actuals)
  print(f"average constant: {final}") #returns on average, the error inherent in rAvg and findRuns
  return sum(actuals)/len(actuals)
  
   


