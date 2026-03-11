# src/modules/ui.py

from src.modules.utils import validate_input, display_error

class UI:
    def display_login_form(self):
        print("Please enter your login details:")
        username = input("Username: ")
        password = input("Password: ")
        
        if not validate_input(username) or not validate_input(password):
            display_error("Invalid input. Please try again.")
            return None
        
        return username, password

    def display_signup_form(self):
        print("Please enter your signup details:")
        username = input("Username: ")
        password = input("Password: ")
        
        if not validate_input(username) or not validate_input(password):
            display_error("Invalid input. Please try again.")
            return None
        
        return username, password

    def display_message(self, message):
        print(message)