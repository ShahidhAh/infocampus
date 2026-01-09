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

#5. CRM CUSTOMER MANAGEMENT USING NESTED DICTIONARY
customers = {
    1: {"name": "Arun", "email": "arun@gmail.com", "status": "Lead"},
    2: {"name": "Meera", "email": "meera@gmail.com", "status": "Customer"}
}
while True:
    print("--MAIN MENU--\n1.Display Customer\n2.Add Customer\n3.Update Customer\n4.Search Customer\n5.Delete Customer\n6.Display Customer by Status\n7.Count Customer by Status\n8.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        for id in customers:
            print("ID:",id)
            print("Name:",customers[id]["name"])
            print("Email:",customers[id]["email"])
            print("Status:",customers[id]["status"])
            print("___________________")
        continue
    elif ch==2:
        cid=int(input("Enter customer id:"))
        if cid in customers:
            print("customer already exist !!")
        else:
            name=input("name:")
            email=input("email:")
            status=input("status:")
            existing_email=set()
            for c in customers.values():
                existing_email.add(c["email"])
            if email in existing_email:
                print("email already exist !!")
            else:
                customers[cid]={"name":name,"email":email,"status":status}
                print("Customer added")
    elif ch==3:
        cid=int(input("Enter your id:"))
        if cid not in customers:
            print("customer does not exist")
        else:
            if customers[cid]["status"]=="Lead":
                customers[cid]["status"]="Customer"
                print("Updated status to",customers[cid]["status"],"!")
            elif customers[cid]["status"]=="Customer":
                customers[cid]["status"]="Client"
                print("Updated status to",customers[cid]["status"],"!")
            else:
                print("Client cannot be changed !")
    elif ch==4:
        s=int(input("Enter id to search:"))
        for cid in customers:
            if cid==s or customers[cid]["email"]==s:
                print(customers[cid])
                break
        else:
            print("Not found")
    elif ch==5:
        d=int(input("Enter id to delete:"))
        if d in customers:
            if customers[d]["status"]=="Lead":
                del customers[d]
                print("Customer",d,"deleted")
            else:
                print("Cannot delete customer !")
        else:
            print("Customer not found")
    elif ch==6:
        s=input("Enter status(Lead/Customer/Client):")
        for cid in customers:
            if customers[cid]["status"]==s:
                print(customers[cid])
            else:
                print("No customer with this status")
    elif ch==7:
        lead=client=customer=0
        for cid in customers:
            if customers[cid]["status"]=="Lead":
                lead+=1
            elif customers[cid]["status"]=="Client":
                client+=1
            elif customers[cid]["status"]=="Customer":
                customer+=1
        print("Lead:",lead)
        print("Customer:",customer)
        print("Client:",client)
    elif ch==8:
        print("Exiting...")
        break
    else:
        print("Invalid choice")