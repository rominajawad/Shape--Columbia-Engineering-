def power(base, exp):
  if(exp == 0):
    return 1
  
  return base*power(base,exp-1)

if __name__ == "__main__":
  b = int(input('Base: '))
  e = int(input('Exp: '))
  print(power(b,e))