def binary_search_itr(li,x):
  start = 0
  stop = len(li) - 1

  while start<=stop:
    mid = (start+stop)//2
    if li[mid]<x:
      start = mid+1
    elif li[mid]>x:
      stop = mid-1
    else:
      return mid
  return -1

def binary_search_rec(li,x):
  return binary_search_rec_helper(li,x,0,len(li)-1)

def binary_search_rec_helper(li,x,start, stop):
  if start > stop:
    return -1

  mid = (start+stop)//2

  if li[mid]<x:
    return binary_search_rec_helper(li,x,mid+1,stop)
  elif li[mid]>x:
    return binary_search_rec_helper(li,x,start,mid-1)
  else:
    return mid


if __name__ == '__main__':
  stuff = [ 3, 5, 2, 4, 1, 7]
  stuff.sort()
  print(stuff)
  val = int(input("What value? "))
  print(binary_search_itr(stuff,val))
  print(binary_search_rec(stuff,val))