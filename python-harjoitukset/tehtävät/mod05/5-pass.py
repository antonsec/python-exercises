usr = "python"
passwd = "rules"
tries = 0

print ("Please enter your Username and Password to login.")

while True:
    new_usr = input(f"Username: ")
    new_passwd = input(f"Password: ")
    tries += 1
    
    if usr == new_usr and passwd == new_passwd:
        print ("Welcome!")
        break
    elif tries > 5:
        print ("Failed too many times... Try again later.")
        break
    print ("Incorrect Username and Password. Please try again.")