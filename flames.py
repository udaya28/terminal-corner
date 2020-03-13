

def abc(z,ln):
  if(z>6 and z%ln==0):return(ln)
  else:return(z%ln)
def display(a):
  if(a=='x'):print('\tEnter valid input')
  elif(a=='f'):print('\tFriend')
  elif(a=='l'):print('\tLove')
  elif(a=='a'):print('\tAffection')
  elif(a=='m'):print('\tMarriage')
  elif(a=='e'):print('\tEnemy')
  elif(a=='s'):print('\tSister')
sa=input("\tEnter your name:")
sb=input("\tEnter another name:")
a,b=list(sa),list(sb)
for i in range(len(a)):
  for j in range(len(b)):
    if (a[i]==b[j]):a[i]=b[j]=0
while (0 in a):a.remove(0)
while(0 in b):b.remove(0)
z=len(a)+len(b)
A="flames"
if(z>6):
  for i in range(0 ,6):
    ln=len(A)
    n=abc(z,ln)
    if(ln==1):break
    A=A[n:ln]+A[0:n-1]
elif(z==0):A='x'
else: 
  x=['s','e','f','e','f','m']
  A=x[z-1]
display(A)

    