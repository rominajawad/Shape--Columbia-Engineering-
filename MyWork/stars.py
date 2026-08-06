user_input=input("Enter a list of numbers: ")
numbers=[]
for val in user_input.split():
  numbers.append(int(val))

numbers.sort() # sort the newly made list

sum=0
count=0

length=len(numbers)

if(length%2!=0): 
  for val in numbers:
    sum+=val
    count++
  middle=sum/count
print("The middle is: " , middle)

else:
  for val2 in numbers:
    lower_middle=numbers[(val2//2)-1]
    upper_middle=number[(val2//2)]
print(lower_middle, upper_middle)
