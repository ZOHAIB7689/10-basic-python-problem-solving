# Prompt the user to enter their age
user_age = input("Your age please")
# Convert the entered age to an integer
user_age = int(user_age)

# Prompt the user to enter the day of the week for the movie
day = input("Enter the day for the movie -> ").lower()
# Determine the price of the ticket based on the user's age
price = 12 if user_age >= 18 else 8

# If the day is Wednesday, apply a discount of $2
if day == "wednesday":
    price -= 2

# Display the price of the movie ticket
print("The price of the movie ticket is $", price)

# Prompt the user to confirm the ticket
user_agree = input("Do you want to confirm the ticket sir?").lower()

# Check if the user's response indicates agreement
if user_agree in ["yes", "ok", "okay", "yeah", "yup", "y", "yea", "sure", "why not"]:
    # If the user agrees, confirm the ticket
    print("Your ticket is confirmed, sir")
    print("Enjoy the movie!")
else:
    # If the user does not agree, thank them for visiting
    print("Thank you for visiting us, sir")
    print("Have a nice day!")