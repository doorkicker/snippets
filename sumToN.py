def sumToN(n, inclusive=False, iOrTotal=False, op='sum'):
  #if inclusive is true, sums up and including n
  #if iOrTotal is false, sums up to and/or including i
  #otherwise, if iOrTotal is True, sums up to and/or including total, instead
  i = 0
  total = 0
  if op == 'sum':
    if iOrTotal == False:
      if inclusive == False:
        i = 0
        total = 0
        while i < n:
          total = total + primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
      else:
        i = 0
        total = 0
        while i <= n:
          total = total + primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
    
    else:
      if inclusive == False:
        i = 0
        total = 0
        while total < n:
          total = total + primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
      else:
        i = 0
        total = 0
        while total <= n:
          total = total + primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
  elif op == 'mult' or op == 'multiply' or op == '*':
    if iOrTotal == False:
      if inclusive == False:
        i = 0
        total = 1
        while i < n:
          total = total * primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
      else:
        i = 0
        total = 1
        while i <= n:
          total = total * primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
    
    else:
      if inclusive == False:
        i = 0
        total = 1
        while total < n:
          total = total * primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i]
      else:
        i = 0
        total = 1
        while total <= n:
          total = total * primes[i]
          i = i + 1
        print(f"i: {i}, total: {total}, n/i: {n/i}, {n/total}, last prime: {primes[i]}")
        return i, total, primes[i] 
