from crm.customer import Customer
from crm.utils import validate_email,validate_status

id=int(input("Enter id:"))
name=input("Enter name:")
email=input("Enter email:")
status=input("Enter status:")

if validate_email(email) and validate_status(status):
    c1=Customer(id,name,email,status)
    c1.display()
else:
    print("Invalid email or status")