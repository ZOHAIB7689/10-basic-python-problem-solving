user_age = input("Your age please")
user_age = int(user_age)

day = input("Enter the day for the movie -> ").lower()
price = 12 if user_age >= 18 else 8

if day == "wednesday":
    # price = price - 2
    price -= 2

print("The price of the movie ticket ticket is $", price)
 
user_agree = input(" Do you want to confirm the ticket sir?").lower()

if user_agree in ["yes", "ok", "okay", "yeah", "yup", "y", "yea", "sure", "why not"]:
    print("Your ticket is confirmed, sir")
    print("Enjoy the movie!")
else:
    print("Thank you for visiting us, sir")
    print("Have a nice day!")