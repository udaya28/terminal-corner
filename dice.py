import random
def inp(s):
    i=input(s)
    for x in i:
        if((ord(x)>=48) and (ord(x)<=57)):
           pass
        else:
            print("\nINVALID INPUT \nInput must be a integer  ")
            return(inp(s))
    return i
def dies(x):
    if(x==1):
        print(" _______")
        print("|       |")
        print("|   x   |")
        print("|       |")
        print("|_______|")
    elif(x==2):
        print(" _______")
        print("|       |")
        print("| x   x |")
        print("|       |")
        print("|_______|")
    elif(x==3):
        print(" _______")
        print("| x     |")
        print("|   x   |")
        print("|     x |")
        print("|_______|")
    elif(x==4):
        print(" _______")
        print("| x   x |")
        print("|       |")
        print("| x   x |")
        print("|_______|")
    elif(x==5):
        print(" _______")
        print("| x   x |")
        print("|   x   |")
        print("| x   x |")
        print("|_______|")
    elif(x==6):
        print(" _______")
        print("| x   x |")
        print("| x   x |")
        print("| x   x |")
        print("|_______|")
def ran():
    r=random.randrange(1,7)
    return r

nn=int(inp("Enter number of dies to roll : "))
n=int(inp("Enter number of times to roll : ")) 
for c in range(n):
    m=input("\nPress Entre ")
    a=[]
    for i in range(nn):
        a.append(ran())
    for x in a:
        dies(x)
        print()
    print("Sum is :",sum(a))
print("\n\tTHE END")
print("\nHAPPY CODDING")
