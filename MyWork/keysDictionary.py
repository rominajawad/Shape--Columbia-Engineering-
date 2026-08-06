x = {1:'a', 2:'b', 3:'c'}
y = {2:'d', 3:'e', 4:'f'}

z={}

for key in x:
  z[key]=[x[key]]

print(z)

for key in y:
  if(key in z):
    z[key].append(y[key])
  else:
    z[key]=[y[key]] #list so that we can add things 
  print(z)

print(z)
