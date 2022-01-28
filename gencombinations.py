def genSimpleRules(atoms):
  #atoms = ["alpha", "beta", "gamma", "delta"] #just example words
  atoms = atoms
  rules = []
  i = 0
  j = 0
  while i < len(atoms):
    j = 0
    while j < len(atoms):
      rules.append(atoms[i] + ", " + atoms[j])
      j=j+1
    
    i=i+1
  return rules

def genComplexRules(molecules, atoms):
  #atoms = ["alpha", "beta", "gamma", "delta"]
  rules = []
  i = 0
  j = 0
  while i < len(molecules):
    j = 0
    while j < len(atoms):
      rules.append("(" + molecules[i] + ", " + atoms[j] + ")")
      j = j + 1
    
    i = i + 1
  
  for rule in rules:
    print(rule)
  return rules
