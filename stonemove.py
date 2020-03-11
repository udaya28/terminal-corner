import sys
def oppo(i,m):
  temp=l[i-1]
  l[i-1]=l[m-1]
  l[m-1]=temp
  win()
  print(l)
    
def win():
  x=(l[0]==l[1]==l[2]=="X" or l[3]==l[4]==l[5]=="X" or l[6]==l[7]==l[8]=="X")
  y=(l[0]==l[3]==l[6]=="X" or l[1]==l[4]==l[7]=="X" or l[2]==l[5]==l[8]=="X")
  p=(l[0]==l[1]==l[2]=="O" or l[3]==l[4]==l[5]=="O" or l[6]==l[7]==l[8]=="O")
  q=(l[0]==l[3]==l[6]=="O" or l[1]==l[4]==l[7]=="O" or l[2]==l[5]==l[8]=="O")
  if(x or y):
    print("1 st player is winner")
    sys.exit()
  if(p or q):
    print("2 st player is winner")
    sys.exit()
  
  
  
def movpos(i):
  win()
  m=int(input())
  if i==1 and m in[2,4] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==2 and m in[1,3,5] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==3 and m in[2,6] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==4 and m in[1,5,7] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==5 and m in[2,4,6,8] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==6 and m in[3,5,9] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==7 and m in[4,8] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==8 and m in[7,9,5] and l[m-1]==" ":
    oppo(i,m)
    printer()
  elif i==9 and m in[8,6] and l[m-1]==" ":
    oppo(i,m)
    printer()
  else:
    print("wrong input,please coin to be moved:")
    check()
    
    
def check():
  win()
  i=int(input())
  print("Enter the moving position:")
  if (j%2==0 and l[i-1]=="O"):
    movpos(i)
  elif(j%2==1 and l[i-1]=="X"):
    movpos(i)
  else:
    print("May you selected Empty space or Opponent's coin:\n Enter correct one :")
    return check()
    
    
def inval():
  x=input()
  if( x.isalpha()):
    print("Input Error: Enter only number")
    return inval()
  else:
    x=int(x)
    if (x in range(1,10))and l[x-1]==" ":
      return x
    elif(l[int(x)-1]=="O" or l[int(x)-1]=="X") :
      print("This position is already filled.........\n Enter the correct:")
      return inval()
    else:
      print ("Input Error: May your input contain,\n 1. Number greater than 9. \n 2.Special character.\n Please enter the correct position...")
      return inval()
    
    
    
def printer():
  print("         *------------------------------*")
  print("         |  ",l[0],"=========",l[1],"========",l[2],"  |")
  print("         |   ||         ||         ||   |")
  print("         |   ||         ||         ||   |")
  print("         |   ||         ||         ||   |")
  print("         |  ",l[3],"=========",l[4],"========",l[5],"  |")
  print("         |   ||         ||         ||   |")
  print("         |   ||         ||         ||   |")
  print("         |   ||         ||         ||   |")
  print("         |  ",l[6],"=========",l[7],"========",l[8],"  |")
  print("         *------------------------------*")
  
  
  
l=[" "," "," "," "," "," "," "," "," "]
printer()
#p1=input("Player 1 name:")
#p2=input("Player 2 name:")
p1="udaya"
p2="nitesh"
print ("Enter the position value by 1 to 6")
count1=1;j=1;
global prepos
global m
for i in range (1,7):
  win()
  if (i%2==0):
    print(p2,"Enter your ",count1,"coin:")
    prepos=inval()
    l[prepos-1]="O"
    printer()
  else:
    print(p1,"Enter your ",count1,"coin:")
    prepos=inval()
    l[prepos-1]="X"
    count1=count1+1
    printer()
while(1):
  win()
  print("Enter the present position of the moving coin:")
  check()
  j=j+1
