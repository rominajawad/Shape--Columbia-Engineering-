import string

candidate = input("Potential Palindrome: ")

c_lower = candidate.lower()
c_no_space = c_lower.replace(' ','')

for c in string.punctuation:
  c_no_space = c_no_space.replace(c,'')

print('Processed string:',c_no_space)

reverse = c_no_space[::-1]
if c_no_space==reverse:
  print(candidate,"is a palindrome!")
else:
  print(candidate,"is not a palindrome.")
