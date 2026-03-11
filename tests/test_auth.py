import pytest
from src.modules.auth import Auth

class TestAuth:
    def setup_method(self):
        self.auth = Auth()

    def test_signup_success(self):
        result = self.auth.signup('unique_user@example.com', 'SecurePass123')
        assert result == 'User signed up successfully.'

    def test_signup_user_exists(self):
        self.auth.signup('existing_user@example.com', 'SecurePass123')
        with pytest.raises(ValueError, match='User already exists.'):
            self.auth.signup('existing_user@example.com', 'AnotherPass456')

    def test_signup_invalid_email(self):
        with pytest.raises(ValueError, match='Invalid email format.'):
            self.auth.signup('invalid_email', 'SecurePass123')

    def test_signup_weak_password(self):
        with pytest.raises(ValueError, match='Password does not meet criteria.'):
            self.auth.signup('new_user@example.com', 'short')

    def test_login_success(self):
        self.auth.signup('login_user@example.com', 'SecurePass123')
        result = self.auth.login('login_user@example.com', 'SecurePass123')
        assert result == 'User logged in successfully.'

    def test_login_user_not_exist(self):
        with pytest.raises(ValueError, match='User does not exist.'):
            self.auth.login('nonexistent_user@example.com', 'SomePass123')

    def test_login_incorrect_password(self):
        self.auth.signup('login_user2@example.com', 'SecurePass123')
        with pytest.raises(ValueError, match='Incorrect password.'):
            self.auth.login('login_user2@example.com', 'WrongPass456')