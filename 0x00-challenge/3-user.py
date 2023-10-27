class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_password(self, input_password):
        return input_password == self.password

# Test case
if __name__ == "__main__":
    user = User("Test User", "password123")

    # Test is_valid_password
    if user.is_valid_password("password123"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("is_valid_password should return False if it's the wrong password")

