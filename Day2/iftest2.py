answer = float(input("What is the answer? "))

if(answer == 42):
  print("You've found it!")
  print("Great job!")
elif(41<=answer<=43):
#elif(answer>=41 and answer<=43):  
  print("You're close.")
else:
  print("That's not it")
  print("keep looking")

print("This is the end")