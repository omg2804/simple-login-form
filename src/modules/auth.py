# src/modules/auth.py

from src.modules.database import Database
from src.modules.utils import validate_email, validate_password

class Auth:
    def __init__(self):
        self.db = Database()

    def signup(self, email, password):
        if not validate_email(email):
            raise ValueError("Invalid email format.")
        if not validate_password(password):
            raise ValueError("Password does not meet criteria.")
        
        if self.db.user_exists(email):
            raise ValueError("User already exists.")
        
        self.db.save_user(email, password)
        return "User signed up successfully."

    def login(self, email, password):
        if not self.db.user_exists(email):
            raise ValueError("User does not exist.")
        
        if not self.db.check_password(email, password):
            raise ValueError("Incorrect password.")
        
        return "User logged in successfully."