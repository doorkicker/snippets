def nullset(ls1, ls2):
  if len(ls1) <= len(ls2):
     #what we're filtering from, the longer list, index or basis list
     basis = ls2
     #the shorter list
     resultant = ls1
  else:
     basis = ls1
     resultant = ls2
  
  #the difference between the lists, whats missing from the basis
  nullset = list(set(basis)-set(resultant))
  nullset.sort()
  #print(str(nullset))
  return nullset


#returns what each set has in common
def common(lsa, lsb):
  difference = set(list(set(lsb) - set(lsa)) + list(set(lsa)-set(lsb))) #what they dont have in common
  commons = list(set(lsb)-difference) #what they have in common
  commons.sort()
  return commons
