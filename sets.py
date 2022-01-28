
# ##############
#returns the difference of two sets
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
  nullset.sort() #recently added 12.04.2020
  #print(str(nullset))
  return nullset


#returns what each set has in common
def common(lsa, lsb):
  difference = set(list(set(lsb) - set(lsa)) + list(set(lsa)-set(lsb))) #what they dont have in common
  commons = list(set(lsb)-difference) #what they have in common
  commons.sort()
  return commons


#returns the index of variables in the main list
def dep_indexs(vars, elements=elements):
  results = []
  for element in vars:
    results.append(elements.index(element))
  
  return results

  
  
#first list is the list to check for your elements
#second list is the elements you want to look for
def containsAll(list1, list2):
  return all(elm in list1 for elm in list2)

def containsAny(list1, list2):
  return any(elm in list1 for elm in list2)
