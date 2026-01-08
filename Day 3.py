#1.login validation
def validation(u,p):
    if u=="user" and p=="asss":
        return True
    else:
        return False

user=input("username:")
pswd=input("password:")

print(validation(user,pswd))


#2.Eligibility function
def eligible(age):
    if age>=18:
        return "Eligible"
    else:
        return "Not Eligible"
    
ag=int(input("Age:"))
print(eligible(ag))