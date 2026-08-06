def fib_itr(n):
  if n==0 or n==1:
    return 1
  p0 = 1
  p1 = 1
  count = 2
  while count <= n:
    sum = p1 + p0
    p0 = p1
    p1 = sum
    count += 1
  return sum

def fib_rec(n):
  if n==0 or n==1:
    return 1
  return fib_rec(n-1) + fib_rec(n-2)

if __name__ == '__main__':
  x = int(input("Number? "))
  print('Iterative',x,'fibonacci number is',fib_itr(x))
  print('Recursive ',x,'fibonacci number is',fib_rec(x))