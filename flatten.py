#only goes to a depth of 1, i.e. shallow flatten
def flat1(ls):
  flat = []
  for subl in ls:
    for item in subl:
      flat.append(item)
      
  return flat
