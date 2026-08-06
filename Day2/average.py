sum = 0
count = 0

num = int(input("Enter a number(negative to stop): "))

while(num>=0):
  sum += num
  count += 1
  num = int(input("Enter a number(negative to stop): "))

if(count==0):
  print("No valid input")
else:
  print("Average:",sum/count)