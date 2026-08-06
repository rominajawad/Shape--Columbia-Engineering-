li = [ 51, 21, 300, 55, 7 ]
print(li)

min_so_far = li[0]
for x in li:
  if(x<min_so_far):
    min_so_far = x

print("Minimum:",min_so_far)