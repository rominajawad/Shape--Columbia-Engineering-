from collections import deque

def josephus(n, k):
  q = deque(range(1,n+1))
  count = 0
  while len(q) > 1:
    current = q.popleft()
    count += 1
    if count == k:
      print('Bye bye', current)
      count = 0
    else:
      q.append(current)

  return q.popleft()

if __name__== '__main__':
  print(josephus(20,5))


