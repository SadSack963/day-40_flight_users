import sheety

print("Welcome to John's Flight Club.\n \
We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    email2 = input("Please verify you email : ")

print("OK. You're in the club!")

sheety.post_new_row(first_name, last_name, email1)
