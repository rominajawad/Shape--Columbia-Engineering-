def factorial(n):
  # Base case
  if n == 0:
    return 1
  
  return n*factorial(n-1)

if __name__ == '__main__':
  x = int(input('Give me a number: '))
  print(x,'factorial is',factorial(x))