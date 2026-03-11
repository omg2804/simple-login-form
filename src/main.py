# src/main.py

import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules.ui import UI
from src.modules.auth import Auth

def main():
    ui = UI()
    auth = Auth()
    while True:
        choice = input("Welcome! Please choose an option:\n1. Login\n2. Signup\n3. Exit\n")
        if choice == '1':
            credentials = ui.display_login_form()
            if credentials:
                username, password = credentials
                if auth.login(username, password):
                    print("Login successful!")
                else:
                    print("Login failed. Please try again.")
        elif choice == '2':
            credentials = ui.display_signup_form()
            if credentials:
                username, password = credentials
                if auth.signup(username, password):
                    print("Signup successful!")
                else:
                    print("Signup failed. Please try again.")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()