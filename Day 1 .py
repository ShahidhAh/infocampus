#1
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("Name:"+name+" Age:",age)


#2
name=input("username:")
pswd=input("password:")
if name=="admin" and pswd=="1234":
    print("Login Successfull")
else:
    print("Incorrect username or password")


#3
mark=int(input("Enter your mark:"))
if mark>=50:
    print("Eligible for higher studies")
else:
    print("Not eligible")


#4
num=int(input("Enter a number:"))
if num%2==0:
    print("Number ",num," is even")
else:
    print("Number ",num,"is odd")


#5
num=int(input("Enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")


#6
marks=int(input("Enter your mark:"))
if marks>=80:
    print("Grade A")
elif marks>=60:
    print("Grade B")
elif marks>=40:
    print("Grade C")
else:
    print("Failed")


#7
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1>num2:
    print(num1,"greater than",num2)
elif num2>num1:
    print(num2,"greater than",num1)
else:
    print("equal numbers")


#8
balance=10000
amt=int(input("Enter amount to withdraw:"))
if amt<=balance:
    bal=balance-amt
    print("amount withdrawn:",amt,",available balance:",bal)
else:
    print("Insufficient balance")

