def tower(source,dest,spare,disks):
  if(disks!=0):
    tower(source,spare,dest,disks-1)
    print("Move disk",disks,"from",source,"to",dest)
    tower(spare,dest,source,disks-1)

if __name__ == '__main__':
  x = int(input('How many? '))
  tower('A','C','B',x)