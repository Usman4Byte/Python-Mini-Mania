email = input("Enter your email address: ")
k = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            k = 1
                    elif i.isdigit() or i in ["_", ".", "@"]:
                        continue
                    else:
                        k = 1
                if k == 1:
                    print("Email is invalid: Contains invalid characters or uppercase letters.")                   
                else:
                    print("Email is valid.")
            else:
                print("Email is invalid: Incorrect domain format.")
        else:
            print("Email is invalid: Missing or multiple '@' symbols.")
    else:
        print("Email is invalid: First character must be a letter.")