user_input=input("Enter a list of numbers: ")
number=[] #save it in an array

count=1
val_list=[] #list for the numbers we have seen
count_list=[] #list for the count (how many times we have seen)

for val in user_input.split(): #i made it in a list 
  number.append(int(val)) #then filled the list with the numbers provided by the user

number.sort()

prev_num=number[0] #very first number
#start looking by second number
for i in range(1,len(number)): #starting at index 1 because the previous number is being comp to
  current_num=number[i]
  if(current_num == prev_num):
    count=+1
  # if its not the same, then its unique so save it
  else:
    val_list.append(prev_num)
    count_list.append(count)
    
    #then reset it so that it knows where to start from
  prev_num=current_num
  count=1

#now when the loop end, its just adds the last numbers
val_list.append(prev_num)
count_list.append(count)
