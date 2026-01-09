
import re

def validate_signup_data(data):
    if not data:
        return "No input data provided"
    
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return "Missing required fields: name, email, password"

    if " " in name:
        return "Username cannot contain spaces"
    
    if " " in password:
        return "Password cannot contain spaces"
        
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        return "Invalid email format"
        
    return None

def validate_login_data(data):
    if not data:
        return "No input data provided"

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return "Missing required fields: email, password"

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        return "Invalid email format"
    
    return None

    
