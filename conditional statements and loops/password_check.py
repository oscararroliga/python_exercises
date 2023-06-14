for i in range(3):
    password=str(input("Enter a password: "))

    if password == "secret":
        print("you guessed the password :)  ")
        break
    else:
        print("That's not your password, try again")
        continue

else:
    print("3 incorrect password attempts, try again tomorrow.")