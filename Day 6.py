class Customer:
    def __init__(self):
        cid=int(input("Enter id:"))
        name=input("Enter name:")
        email=input("Enter email:")
        status=input("Enter status:")
        self.cid = cid
        self.name = name
        self.email = email
        self.status = status
    def display(self):
        print(self.cid,self.name,self.email,self.status)
    def update(self):
        if self.status=="Lead":
            self.status="Customer"
        elif self.status=="Customer":
            self.status="Client"
        else:
            print("Cannot change status")
    def is_deletable(self):
        if self.status=="Lead":
            return True
        else:
            return False
    
    
c1=Customer()
#c2=Customer()
c1.display()
print(c1.is_deletable())
c1.display()
#c2.display()
c1.update()
#c2.update()
print(c1.is_deletable())
c1.display()
#c2.display()
        