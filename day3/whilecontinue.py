limit = int(input("How high? "))
count = 1;

while(count<=limit):
  if count==13:
    count += 1
    continue;
  print(count)
  count += 1

print("This is the end.")