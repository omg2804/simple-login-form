import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file=':memory:'):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=()):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(e)

    def fetch_all(self, query, params=()):
        """Fetch all results from a query."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def fetch_one(self, query, params=()):
        """Fetch a single result from a query."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def user_exists(self, email):
        """Check if a user exists in the database."""
        query = 'SELECT * FROM users WHERE email = ?'
        result = self.fetch_one(query, (email,))
        return result is not None

    def save_user(self, email, password):
        """Save a new user to the database."""
        query = 'INSERT INTO users (email, password) VALUES (?, ?)'
        self.execute_query(query, (email, password))

    def check_password(self, email, password):
        """Check if the provided password matches the stored password for the user."""
        query = 'SELECT password FROM users WHERE email = ?'
        result = self.fetch_one(query, (email,))
        return result[0] == password if result else False