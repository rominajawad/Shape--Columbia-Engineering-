answer = int(input("What is the answer? "))

if(answer == 42):
  print("You've found it!")
  print("Great job!")
elif(answer == 41 or answer == 43):
  print("You're close.")
else:
  print("That's not it")
  print("keep looking")

print("This is the end")