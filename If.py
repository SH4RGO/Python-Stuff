#-Data

Names1 = "Amine"
Names2 = "Neo"
Names3 = "Andrew"
Pass1 = "Lp09"
Pass2 = "Pl89"
Pass3 = "Lm09"
#-Operation
Attempt = input("Enter your Name: ")
if Attempt == Names1:
    Amine1 = input("Enter Your Password Amine : ")
    if Amine1 == Pass1:
        print("Welcome Amine")
        Question = input("What Do You Want: News / Mission / Meetup: ")
        if Question == "News":
            print("Theres Is No New News")
        elif Question == "Mission":
            print("Destroy The Matrix")
        elif Question == "Meetup":
            print("Check The Telegram:)")
elif Attempt == Names2:
    Neo1 = input("Enter Your Password Neo: ")
    if Neo1 == Pass2:
        print("Welcome Neo :)")
        Question = input("What Do You Want: News / Mission / Meetup: ")
        if Question == "News":
            print("Theres Is No New News")
        elif Question == "Mission":
            print("Destroy The Matrix")
        elif Question == "Meetup":
            print("Check The Telegram:)")
elif Attempt == Names3:
    Andrew1 = input("Enter Your Password Andrew: ")
    if Andrew1 == Pass3:
        print("Welcome Mr Producer")
        Question = input("What Do You Want: News / Mission / Meetup: ")
        if Question == "News":
            print("Theres Is No New News")
        elif Question == "Mission":
            print("Destroy The Matrix")
        elif Question == "Meetup":
            print("Check The Telegram:)")
    else:
        print("Incorrect, The Program will stop now")
else:
    print("Try Again")