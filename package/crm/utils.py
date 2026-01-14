def validate_email(email):
    return "@" in email

def validate_status(status):
    return status in ["Lead","Customer","Client"]