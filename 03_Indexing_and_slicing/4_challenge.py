# Input an email address (like "student123@gmail.com")
email = input("Enter your email address: ")
# Slice out the username (everything before '@')
username = email[:email.index('@')]
# Remove the first and last character from that username
trimmed_username = username[1:-1]
# Print both: original username and trimmed username
print("Original username:", username)
print("Trimmed username:", trimmed_username)
