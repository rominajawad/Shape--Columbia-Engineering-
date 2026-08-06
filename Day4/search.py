li = [ 55, 21, 100, 35, 71 ]
print(li)

v = int(input("What are you looking for? "))

location = -1
i = 0
while(i<len(li)):
  if li[i] == v:
    location = i
    break
  i += 1

if location<0:
  print("Value:",v,"was not found")
else:
  print("Value:",v,"was found at location",location)

li.sort()
print(li)

v = int(input("What are you looking for? "))

location = -1
start = 0
stop = len(li) - 1

while start<=stop:
  mid = (start+stop)//2
  if li[mid] < v:
    # Upper half
    start = mid+1
  elif li[mid] > v:
    # Lower half 
    stop = mid-1
  else: # li[mid] == v
    location = mid
    break

if location<0:
  print("Value:",v,"was not found")
else:
  print("Value:",v,"was found at location",location)

