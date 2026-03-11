# src/modules/utils.py

def validate_email(email: str) -> bool:
    """Validate the format of an email address."""
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_password(password: str) -> bool:
    """Validate the strength of a password."""
    return len(password) >= 8


def handle_error(error_message: str) -> None:
    """Handle errors by logging or displaying them."""
    print(f"Error: {error_message}")