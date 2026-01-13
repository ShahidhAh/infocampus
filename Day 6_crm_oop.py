class CRMSystem:
    
    def __init__(self):
        self.customers=[]
        
    def add_customer(self):
        id=int(input("ID:"))
        name=input("Name:")
        email=input("Email:")
        status=input("Status:")
        customer={
            "id":id,
            "name":name,
            "email":email,
            "status":status
        }
        self.customers.append(customer)
        print("Customer added successfully")
        
    def display_all(self):
        for i in self.customers:
            print(i)
            
    def search_customer(self):
        s=input("Enter email or ID to search:")
        for i in self.customers:
            if str(i["id"])==s or i["email"]==s:
                print(i)
     
    def update_customer(self):
        u=int(input("Enter ID of customer to update:"))
        for i in self.customers:
            if i["id"]==u:
                if i["status"]=="Lead":
                    i["status"]="Customer"
                    print(i)
                elif i["status"]=="Customer":
                    i["status"]="Client"
                    print(i)
                else:
                    print("Cannot downgrade")
                    print(i)
                
    def delete_customer(self):
        d=int(input("Enter ID to delete:"))
        for i in self.customers:
            if i["id"]==d:
                if i["status"]=="Lead":
                    self.customers.remove(i)
                    print("Customer with ID",i["id"],"removed")
                else:
                    print("Cannot delete customer with status customer or client !!")
                    
    def count_by_status(self):
        lead=customer=client=0
        for i in self.customers:
            if i["status"] == "Lead":
                lead += 1

            elif i["status"] == "Customer":
                customer += 1

            elif i["status"] == "Client":
                client += 1


        print("\n Count of the Status")

        print("Lead",lead)
        print("Customer",customer)
        print("Cleint",client)
            
crm=CRMSystem()
while True:
    print("\n--- MENU ---")
    print("1. Add Customer")
    print("2. Display All Customers")
    print("3. Search Customer")
    print("4. Update Customer Status")
    print("5. Delete Customer")
    print("6. Count Customers by Status")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        crm.add_customer()
    elif choice == 2:
        crm.display_all()
    elif choice == 3:
        crm.search_customer()
    elif choice == 4:
        crm.update_customer()
    elif choice == 5:
        crm.delete_customer()
    elif choice == 6:
        crm.count_by_status()
    elif choice == 7:
        print("Exiting CRM System...")
        break
    else:
        print("Invalid choice! Try again.")