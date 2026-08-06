candidate = int(input("Give me a number: "))

count = 2
is_prime = True

while count*count<=candidate:
  if candidate%count == 0:
    is_prime = False
    break
  count += 1

if is_prime:
  print("prime")
else:
  print("not prime")