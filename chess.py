def hi(x):
  i=ord(x[0])
  j=int(x[1])   
  i=i-64 
  return(i*10+j,i,j)
def king(a,a2,a1):
  z1=[(a1+1)*10+a2+1,(a1-1)*10+a2-1,(a1+1)*10+a2-1,(a1-1)*10+a2+1]
  z2=[(a1)*10+a2+1,(a1)*10+a2-1,(a1+1)*10+a2,(a1-1)*10+a2]
  return(z1+z2)
def knight(a,a2,a1):
  x=[(a1-2)*10+(a2-1),(a1-2)*10+(a2+1),(a1+2)*10+(a2-1),(a1+2)*10+(a2+1)]
  y=[(a2-2)+(a1-1)*10,(a2-2)+(a1+1)*10,(a2+2)+(a1-1)*10,(a2+2)+(a1+1)*10]
  return(x+y)
def bishop(a,a1,a2):
  for j in range(11,89):
    if(j%10+j//10==a1+a2):
      z.append(j)
  g=1
  for i in range((a2-a1)+1,9):
    if(g==9):break
    z.append((g)+i*10)
    g=g+1
  return(z)
def rook(a,a1,a2):
  for j in range(11,89):
    if(j%10==a1 or j//10==a2):
      z.append(j)
  return(z)
def queen(a,a1,a2):
  z=bishop(a,a1,a2)+rook(a,a1,a2)
  return(z)
def pawn(a,a1,a2):
  if(cc==1):
    z.append(a1+(a2-1)*10)
    if(a2==7):
      z.append(a1+(a2-2)*10)
  else:
    z.append(a1+(a2+1)*10)
    if(a2==2):
      z.append(a1+(a2+2)*10)
  return(z)
  
def board():
  print("                  BLACK SIDE              ")
  print("  =========================================")
  print("  |",b[0][0],"|",b[0][1],"|",b[0][2],"|",b[0][3],"|",b[0][4],"|",b[0][5],"|",b[0][6],"|",b[0][7],"|",b[0][8],"|   |")
  print("  =========================================")
  print("  |",b[1][0],"|",b[1][1],"|",b[1][2],"|",b[1][3],"|",b[1][4],"|",b[1][5],"|",b[1][6],"|",b[1][7],"|",b[1][8],"| 1 |")
  print("  =========================================")
  print("  |",b[2][0],"|",b[2][1],"|",b[2][2],"|",b[2][3],"|",b[2][4],"|",b[2][5],"|",b[2][6],"|",b[2][7],"|",b[2][8],"| 2 |")
  print("  =========================================")
  print("  |",b[3][0],"|",b[3][1],"|",b[3][2],"|",b[3][3],"|",b[3][4],"|",b[3][5],"|",b[3][6],"|",b[3][7],"|",b[3][8],"| 3 |")
  print("  =========================================")
  print("  |",b[4][0],"|",b[4][1],"|",b[4][2],"|",b[4][3],"|",b[4][4],"|",b[4][5],"|",b[4][6],"|",b[4][7],"|",b[4][8],"| 4 |")
  print("  =========================================")
  print("  |",b[5][0],"|",b[5][1],"|",b[5][2],"|",b[5][3],"|",b[5][4],"|",b[5][5],"|",b[5][6],"|",b[5][7],"|",b[5][8],"| 5 |")
  print("  =========================================")
  print("  |",b[6][0],"|",b[6][1],"|",b[6][2],"|",b[6][3],"|",b[6][4],"|",b[6][5],"|",b[6][6],"|",b[6][7],"|",b[6][8],"| 6 |")
  print("  =========================================")
  print("  |",b[7][0],"|",b[7][1],"|",b[7][2],"|",b[7][3],"|",b[7][4],"|",b[7][5],"|",b[7][6],"|",b[7][7],"|",b[7][8],"| 7 |")
  print("  =========================================")
  print("  |",b[8][0],"|",b[8][1],"|",b[8][2],"|",b[8][3],"|",b[8][4],"|",b[8][5],"|",b[8][6],"|",b[8][7],"|",b[8][8],"| 8 |")
  print("  =========================================")
  print("  |   | A | B | C | D | E | F | G | H |   |")
  print("  =========================================")
  print("                  WHITE SIDE               ")
b=[[" ","A","B","C","D","E","F","G","H"],
["1"," "," "," "," "," "," "," "," "],
["2"," "," "," "," "," "," "," "," "],
["3"," "," "," "," "," "," "," "," "],
["4"," "," "," "," "," "," "," "," "],
["5"," "," "," "," "," "," "," "," "],
["6"," "," "," "," "," "," "," "," "],
["7"," "," "," "," "," "," "," "," "],
["8"," "," "," "," "," "," "," "," "]]  
board()
print("Enter your coin colour: \n1 for White \n2 for Black")
cc=int((input("Enter...")))
print("Enter your coin :\n1 for King(அரசன்)\n2 for Queen(அரசி)\n3 for Bishop(அமைச்சர்)\n4 for Knight(குதிரை)\n5 for Rook(யானை)\n6 for pawn(சிப்பாய்)")
n=int(input("Enter ..."))
print("Enter your position of coin:\n@First lette is alphabet in capital\n@Second letter in number\n@Example A5,E5,C8")
p=input("Enter ...")
z=[]
a,a1,a2=hi(p)
if(not(a<=88 and a>=11 and n>=1 and n<=6)):
  print("invalid input")
else:
  if(n==1):z=king(a,a1,a2)
  elif(n==2):z=queen(a,a1,a2)
  elif(n==3):z=bishop(a,a1,a2)
  elif(n==4):z=knight(a,a1,a2)
  elif(n==5):z=rook(a,a1,a2)
  elif(n==6):z=pawn(a,a1,a2)
  else:print("BUG")
  new=[]
  for s in range(len(z)):
    if(z[s]>=11 and z[s]<=88 and z[s]%10!=0 and z[s]%10!=9):
      new.append(z[s])
  for u in range(len(new)):
    b[new[u]//10][new[u]%10]="X"
    b[a2][a1]="O"
  board()
  print("O is your coin position")
  print("X is the positions you can move")


print("            HAPPY CODDING")
