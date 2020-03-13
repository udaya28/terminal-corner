import random
import sys
c=[0]
def ansck():
  a=(l[0]=="*" and l[1]=="*" and l[2]=="*" and l[3]=="*" and l[4]=="*")
  b=(l[5]=="*" and l[6]=="*" and l[7]=="*" and l[8]=="*" and l[9]=="*")
  c=(l[10]=="*" and l[11]=="*" and l[12]=="*" and l[13]=="*" and l[14]=="*")
  d=(l[15]=="*" and l[16]=="*" and l[17]=="*" and l[18]=="*" and l[19]=="*")
  e=(l[20]=="*" and l[21]=="*" and l[22]=="*" and l[23]=="*" and l[24]=="*")
  f=(l[0]=="*" and l[5]=="*" and l[10]=="*" and l[15]=="*" and l[20]=="*")
  g=(l[1]=="*" and l[6]=="*" and l[11]=="*" and l[16]=="*" and l[21]=="*")
  h=(l[2]=="*" and l[7]=="*" and l[12]=="*" and l[17]=="*" and l[22]=="*")
  i=(l[3]=="*" and l[8]=="*" and l[13]=="*" and l[18]=="*" and l[23]=="*")
  j=(l[4]=="*" and l[9]=="*" and l[14]=="*" and l[19]=="*" and l[24]=="*")
  k=(l[0]=="*" and l[6]=="*" and l[12]=="*" and l[18]=="*" and l[24]=="*")
  m=(l[4]=="*" and l[8]=="*" and l[12]=="*" and l[16]=="*" and l[20]=="*")
  l3=[a,b,c,d,e,f,g,h,i,j,k,m]
  return l3
def check():
  i=input("Enter the number:")
  if (ord(i[0]) in range(47,59)):
    i=int(i)
  else:
    print("Input Error: Your input contains: \n 1.Special Character \n 2.Alphabet")
    return check()
  if i<=25 and i not in c:
    c.append(i)
    l2=[" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9"]
    if i in range(1,10):
      i=l2[i-1]
    id=l.index(i)
    if (l[id]!="*"):
      l[id]="*"
      printer()
      ans=ansck()
      count=0
      for i in ans:
        if i==True:
          count+=1
      b=["B","I","N","G","O"]
      for j in range (0,count):
        b[j]="*"
      print("-----------------------------")
      print("|",b[0],"|","|",b[1],"|","|",b[2],"|","|",b[3],"|","|",b[4],"|")
      print("-----------------------------")
      if (b[0]=="*" and b[1]=="*" and b[2]=="*" and b[3]=="*" and b[4]=="*"):
        print ("Game over:")
        sys.exit()
    else:
      print("Already crossed!")
      return check()
  else:
    print("NOT IN RANGE or ALREADY CROSSED")
    return check()
def printer ():
  
  print("|——————————————————————————————————————|")
  print("|  |",l[0],"|","|",l[1],"|","|",l[2],"|","|",l[3],"|","|",l[4],"|  |")
  print("|   ————————————————————————————————   |")
  print("|  |",l[5],"|","|",l[6],"|","|",l[7],"|","|",l[8],"|","|",l[9],"|  |")
  print("|   ————————————————————————————————   |")
  print("|  |",l[10],"|","|",l[11],"|","|",l[12],"|","|",l[13],"|","|",l[14],"|  |")
  print("|   ————————————————————————————————   |")
  print("|  |",l[15],"|","|",l[16],"|","|",l[17],"|","|",l[18],"|","|",l[19],"|  |")
  print("|   ————————————————————————————————   |")
  print("|  |",l[20],"|","|",l[21],"|","|",l[22],"|","|",l[23],"|","|",l[24],"|  |")
  print("|——————————————————————————————————————|")
  
 
  
l = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

count=0
random.shuffle(l)
print("*************Your BINGO sheet***********")
printer()
j=0
while(j!=25):
  check()
  j=j+1
