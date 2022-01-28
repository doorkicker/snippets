#now sort
def largest(ls):
  i = 0
  val = [0, 0]
  while i < len(ls):
    if ls[i][1] > val[1]:
      val = ls[i]
    i = i + 1
  
  return val