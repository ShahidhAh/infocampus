#1
for i in range(1,11):
    print(i)


#2
n=int(input("Enter a number:"))
sum=0

for i in range (1,n):
    sum+=i
print(sum)


#3
n=int(input("Enter a number:"))

for i in range (1,11):
    print(i,"x",n,"=",n*i)


#4
attempt=3
usr="admin"
pss=1234

while attempt>0:
    user=input("username:")
    pswd=int(input("password:"))
    if user==usr and pss==pswd:
        print("Login Successfull")
        break
    else:
        attempt-=1
        print("Error,",attempt,"left")
if attempt==0:
    print("Account Locked")


#5
n=int(input("Enter a number:"))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("No.of Odd:",odd,"and Even:",even)


#6
print("1.Add\n2.Substract\n3.Multiplication\n4.Exit")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter your choice:"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print("Exiting..")
else:
    print("Invalid choice")


#7
pswd=input("Password:")
len=len(pswd)
if len>=8:
    print("Strong password")
elif len>=5:
    print("Medium")
else:
    print("Weak password")