#1.Create a list to store customer names , allow the user to add,remove,show
customer=[]
while True:
    print("1.Add\n2.Remove\n3.Show\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        name=input("Name:")
        customer.append(name)
    elif ch==2:
        name=input("Name:")
        if name in customer:
            customer.remove()
    elif ch==3:
        print(customer)
    elif ch==4:
        print("Exit..")
        break
    else:
        print("invalid choice")

#3.Customer Phone Directory
customer={
    "shahid":"987654320",
    "sulafa":"963852741",
    "rohan":"741852963",
    "nived":"789456123"
}
n=input("Enter name:")
if n in customer:
    print("Phone:",customer[n])
else:
    print("name not found")