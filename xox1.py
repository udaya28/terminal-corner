import random

def ran(r):
  x=random.choice(r)
  return(x)

def alpa(n):
  return(n.isalpha())

def num(n):
  if(n in r):
    return True
  else:
    return False


def inpu(ss):
  n=input(ss)
  x=not(alpa(n))
  y=False
  if(x):
    n=int(n)
    y=num(n)
  if(x and y):
    return(n)
  else:
    dis()
    print("wrong input")
    print("enter the valid input")
    return(inpu(ss))

def check():
  x=(a[0]==a[1]==a[2]!=" " or a[3]==a[4]==a[5]!=" " or a[6]==a[7]==a[8]!=" ")
  y=(a[0]==a[3]==a[6]!=" " or a[1]==a[4]==a[7]!=" " or a[2]==a[5]==a[8]!=" ")
  z=(a[0]==a[4]==a[8]!=" " or a[6]==a[4]==a[2]!=" ")
  return(x or y or z )

def win(i):
  if(i%2!=1):
    print("winner is ",na)
  else:
    print("winner is ",nb)

def dis():
  print()
  print("————————————————————————————————————————————————————")
  print("|        board                     position        |")
  print("|  ———————————————————        ———————————————————  |")
  print("|  | ",a[0]," | ",a[1]," | ",a[2]," |       ","| ","1"," | ","2"," | ","3"," |  |")
  print("|  ———————————————————        ———————————————————  |")
  print("|  | ",a[3]," | ",a[4]," | ",a[5]," |       ","| ","4"," | ","5"," | ","6"," |  |")
  print("|  ———————————————————        ———————————————————  |")
  print("|  | ",a[6]," | ",a[7]," | ",a[8]," |       ","| ","7"," | ","8"," | ","9"," |  |")
  print("|  ———————————————————        ———————————————————  |")
  print("————————————————————————————————————————————————————")
 
a=[" "," "," "," "," "," "," "," "," "]
dis()
r=[1,2,3,4,5,6,7,8,9]
na=input("Enter your name :")
nb="COMPUTER"
for i in range(1,10):
  dis()
  if(check()):
    win(i)
    print("game ends")
    break
  if(i%2!=0):
    n=inpu("Enter your position :")
    r.remove(n)
    a[n-1]="X"
  else:
    print(nb,"'s Turn ",end="")
    n=ran(r)
    r.remove(n)
    a[n-1]="O"
else:
  if(check()):
    win(i+1)
  else:
    dis()
    print("match is draw")





