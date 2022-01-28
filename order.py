#given a list of numbers or variables in a string, with relation '>'
#determines if the relations hold, and returns a dictionary of the values

def tOrder(string):
  el = string.split(" > ")
  work = "{"
  for e in el:
    work = work + "'" + e + "'" +":" + e + ", "
  
  if eval(string) == True:
    print("order HOLDS.")
  else:
    print("order MODIFIED.")
  
  work = work + "}"
  return eval(work)

  
#finds an ordering of a set of pairs of dictionary elements
def findOrder(elmPairs):
  result = elmPairs
  #for e in result:
  #  result[result.index(e)] = Dec.copy_abs(e)
  
  sort_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
  string = ""
  for i in sort_result:
    #print(i[0])
    string = string + " > " + i[0]
  
  string = string[3:] #removes the erroneous additional ">"
  #return sort_result
  return string
