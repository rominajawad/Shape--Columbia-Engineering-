s= input("Enter a DNA sequence: ") # s is the dna sequence
user_find= input("The searching sequence: ")
is_found=false;
max_index=len(s)-len(user_find)-1 #finding the max index to look at

found_index=-1 # default it to this if this is not found
for i in range(max_index):
  if s[i:i:len(user_find)] == sub:
    is_found=true
    found_index=i
    break

  if is_found:
    print(found_index)
  else:
    print(-1)
