# if 
# elif
# else

# Voting Eligibility Checker
age = int(input("Please enter your age"))

if age > 18:
    print("You are a adult.")
else :
    print("You are a minor and are not elgible to vote.")

#Student Grade Checker

marks = int(input("Please enter your marks"))
if marks >= 90:
    print("You have received A++ grade.")
elif marks >= 85:
    print("You have received A grade.")
elif marks >= 79:
    print("You have received B grade.")
elif marks >= 69:
    print("You have received C grade.")
elif marks >= 59:
    print("You have received D grade.")
elif marks >= 49:
    print("You have received E grade.")
else:
    print("You have done horrible in your exams. Your grade is equal to F.")
    
#Voting Eligibity Checker with elif

age1 = int(input("Please enter your age"))
citizenship = input("Are you a citizen of this country? (yes/no)")
if age1 >= 18:
    if citizenship.upper() == "YES":
        print("You are eligible to vote.")
        if age1 >= 75:
            print("You are too old to vote.")
        else:
            print("Thank you for your service.")
    else:
        print("You must be a passport holder of this counrty to vote here.")
else:
    print("Thank you for your enthusiasm but you are young for the voting process.")
    
# Simple Login System
username1 = "yyy"
password1 = "1234"
username = input("Enter your username: ")
password = input("Enter your password: ")

if username1 == username:
    if password1 == password:
        print("Login is successful.")
    else:
        print("incorrect password please try again.")
else:
    print("Username is not correct please try again.")
    
