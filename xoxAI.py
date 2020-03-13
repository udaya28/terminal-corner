import random
def ai():
    print("ai")
    print("hello")
    #if(a[0]=="X"):
    if(a[2]=="X" and a[1]!=" " and a[0]=="X"):
      a[1]="O"
      r.remove(1)
    elif(a[6]=="X" and a[3]!=" "and a[0]=="X"):
      a[3]="O"
      r.remove(3)
    elif(a[8]=="X" and a[4]!=" "and a[0]=="X"): 
      a[4]="O"
      r.remove(4)
    elif(a[3]=="X" and a[6]!=" "and a[0]=="X"):
      a[6]="O"
      r.remove(6)
    elif(a[1]=="X" and a[2]!=" "and a[0]=="X"):
      a[2]="O"
      r.remove(2)
    elif(a[4]=="X" and a[8]!=" "and a[0]=="X"):
      a[8]="O"
      r.remove(8)
    #elif(a[1]=="X"):
    elif(a[0]=="X" and a[2]!=" " and a[1]=="X"):
      a[2]="O"
      r.remove(2)
    elif(a[2]=="X" and a[0]!=" "and a[1]=="X"):
      a[0]="O"
      r.remove(0)
    elif(a[4]=="X" and a[7]!=" "and a[1]=="X"):
      a[7]="O"
      r.remove(7)
    elif(a[7]=="X" and a[4]!=" "and a[1]=="X"):
      a[4]="O"
      r.remove(4)
   #elif(a[2]=="X"):
    elif(a[0]=="X" and a[1]!=" " and a[2]=="X"):
      a[1]="O"
      r.remove(1)
    elif(a[1]=="X" and a[0]!=" " and a[2]=="X"):
      a[0]="O"
      r.remove(0)
    elif(a[5]=="X" and a[8]!=" " and a[2]=="X"): 
      a[8]="O"
      r.remove(8)
    elif(a[4]=="X" and a[6]!=" " and a[2]=="X"):
      a[6]="O"
      r.remove(6)
    elif(a[6]=="X" and a[4]!=" " and a[2]=="X"):
      a[4]="O"
      r.remove(4)
    elif(a[8]=="X" and a[5]!=" " and a[2]=="X"):
      a[5]="O"
      r.remove(5)
    #elif(a[3]=="X"):
    elif(a[0]=="X" and a[6]!=" " and a[3]=="X"):
      a[6]="O"
      r.remove(6)
    elif(a[6]=="X" and a[0]!=" " and a[3]=="X"):
      a[0]="O"
      r.remove(0)
    elif(a[4]=="X" and a[5]!=" " and a[3]=="X"): 
      a[5]="O"
      r.remove(5)
    elif(a[5]=="X" and a[4]!=" " and a[3]=="X"):
      a[4]="O"
      r.remove(4)
    #elif(a[4]=="X"):
    elif(a[0]=="X" and a[8]!=" " and a[4]=="X"):
      a[8]="O"
      r.remove(8)
    elif(a[1]=="X" and a[7]!=" " and a[4]=="X"):
      a[7]="O"
      r.remove(7)
    elif(a[2]=="X" and a[6]!=" " and a[4]=="X"): 
      a[6]="O"
      r.remove(6)
    elif(a[3]=="X" and a[5]!=" " and a[4]=="X"):
      a[5]="O"
      r.remove(5)
    elif(a[5]=="X" and a[3]!=" " and a[4]=="X"):
      a[3]="O"
      r.remove(3)
    elif(a[6]=="X" and a[2]!=" " and a[4]=="X"):
      a[2]="O"
      r.remove(2)
    elif(a[7]=="X" and a[1]!=" " and a[4]=="X"):
      a[1]="O"
      r.remove(1)
    elif(a[8]=="X" and a[0]!=" " and a[4]=="X"):
      a[0]="O"
      r.remove(0)
    #elif(a[5]=="X"):
    elif(a[2]=="X" and a[8]!=" " and a[5]=="X"):
      a[8]="O"
      r.remove(8)
    elif(a[3]=="X" and a[4]!=" " and a[5]=="X"):
      a[4]="O"
      r.remove(4)
    elif(a[4]=="X" and a[3]!=" " and a[5]=="X"): 
      a[3]="O"
      r.remove(3)
    elif(a[8]=="X" and a[2]!=" " and a[5]=="X"):
      a[2]="O"
      r.remove(2)
    #elif(a[6]=="X"):
    elif(a[0]=="X" and a[3]!=" " and a[6]=="X"):
      a[3]="O"
      r.remove(3)
    elif(a[2]=="X" and a[4]!=" " and a[6]=="X"):
      a[4]="O"
      r.remove(4)
    elif(a[3]=="X" and a[0]!=" " and a[6]=="X"): 
      a[0]="O"
      r.remove(0)
    elif(a[4]=="X" and a[2]!=" " and a[6]=="X"):
      a[2]="O"
      r.remove(2)
    elif(a[7]=="X" and a[8]!=" " and a[6]=="X"):
      a[8]="O"
      r.remove(8)
    elif(a[8]=="X" and a[7]!=" " and a[6]=="X"):
      a[7]="O"
      r.remove(7)
    #elif(a[7]=="X"):
    elif(a[1]=="X" and a[4]!=" " and a[7]=="X"):
      a[4]="O"
      r.remove(4)
    elif(a[4]=="X" and a[1]!=" " and a[7]=="X"):
      a[1]="O"
      r.remove(1)
    elif(a[6]=="X" and a[8]!=" " and a[7]=="X"): 
      a[8]="O"
      r.remove(8)
    elif(a[8]=="X" and a[6]!=" " and a[7]=="X"):
      a[6]="O"
      r.remove(6)
    #elif(a[8]=="X"):
    elif(a[0]=="X" and a[4]!=" " and a[8]=="X"):
      a[4]="O"
      r.remove(4)
    elif(a[2]=="X" and a[5]!=" " and a[8]=="X"):
      a[5]="O"
      r.remove(5)
    elif(a[4]=="X" and a[0]!=" " and a[8]=="X"): 
      a[0]="O"
      r.remove(0)
    elif(a[5]=="X" and a[2]!=" " and a[8]=="X"):
      a[2]="O"
      r.remove(2)
    elif(a[6]=="X" and a[7]!=" " and a[8]=="X"):
      a[7]="O"
      r.remove(7)
    elif(a[7]=="X" and a[6]!=" " and a[8]=="X"):
      a[6]="O"
      r.remove(6)
    else:
      print("ran")
      m=ran(r)
      print(m)
      a[m]="O"
      r.remove(m)
   

   
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
r=[0,1,2,3,4,5,6,7,8]
a[2]="X"
a[1]="X"
ai()
dis()
#li=[[a[0],a[1],a[2]], [a[3],a[4],a[5]], [a[6],a[7],a[8]], [a[0],a[3],a[6]] ,[a[1],a[4],a[7]] ,[a[2],a[5],a[8]] ,[a[0],a[4],a[8]] ,[a[6],a[4],a[2]]]
#na=input("Enter your name :")
na="udaya"
nb="COMPUTER"
for i in range(1,10):
  print(a)
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
    ai()
    #r.remove(n)
else:
  if(check()):
    win(i+1)
  else:
    dis()
    print("match is draw")





