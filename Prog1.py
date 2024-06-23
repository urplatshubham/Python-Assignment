"""Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password.  

"""
import re

feedback = []
def check_password_strength(password):
   
        strength = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$&])[A-Za-z\d!@#$&]{8,}$")
        if re.search(strength, password):
            return True
        else:
            if len(password)<8:
                 feedback.append("Password length is less than 8 characters")
            if not re.findall(r"\d",password):
                 feedback.append("Digit is missing")
            if not re.findall(r"[a-z]",password):
                 feedback.append("Lower case letter is missing")
            if not re.findall(r"[A-Z]",password):
                 feedback.append("Upper case letter is missing")
            if not re.findall(r"[!@#$&]",password):
                 feedback.append("Special character is missing eg !, @, #, $, &")
            return False
        
while True:
        
    password = input("Enter your password : ")

    if check_password_strength(password):
        print("Password strength is good!")
        break
    else:
        print("Password strength is bad! \n")
        print("These are feedbacks! Please change your password accordingly")
        i=1
        for f in feedback:
            print(i, ". ", f, "\n")
            i = i+1

    