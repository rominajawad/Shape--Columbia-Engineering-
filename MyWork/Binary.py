li=[1,3,5,2,4,5,10,67,56,34,55,77,22,66,8] # [1,2,3,4,5]
li.sort()
user= int(input("Enter a number you want to search: "))
left=0
right=len(li)-1
BooleanSwitch = True

while right>=left:
  middle=(right+left)//2
  if(user==li[middle]):
    print("its found at index: ", middle)
    BooleanSwitch = False
    break
  elif(user<li[middle]):
    right=middle-1
  else:
    left=middle+1

if (BooleanSwitch): #This means BooleanSwitch == True
  print(-1) #I need this to only run when the print statement above does not run
