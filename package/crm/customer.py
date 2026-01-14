class Customer:
    def __init__(self,id,name,email,status):
        self.id=id
        self.name=name
        self.email=email
        self.status=status
    def display(self):
        print("ID:",self.id,"\nName:",self.name,"\nEmail:",self.email,"\nStatus:",self.status)
