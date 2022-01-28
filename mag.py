from math import *

def mag(n):
  return (10**(len(str(((Dec(round(n))*10)))[:-2])))

def Mag(n):
  return len(str(10**(len(str(((Dec(round(n))*10)))[:-2]))))

def maglen(n):
  print(len(str(mag(floor(n)))))  
  
def Maglen(n):
  return int(len(str(mag(floor(n)))))  
