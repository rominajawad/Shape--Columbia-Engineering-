word = 'hello'
display=  '_'*len(word)
print(display)
ld = list(display)
print(ld)
ld[1] = 'e'
print(ld)
output = ''.join(ld)
print(output)
