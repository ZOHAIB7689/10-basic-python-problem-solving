# Age Group Categorization
# classify a person's age group child(<13), teenager(13-19), young adult(20-30), senior(65+)


# get age from the user with this input field
while True:
    # get age from the user with this input field
    user_age = input("Give me your age: ")
    
    # Try to convert the user input to an integer
    try:
        user_age = int(user_age)
        if user_age > 150:
            print("Please enter a valid age")
            continue
    except ValueError:
        print("Please enter a valid number")
        continue

    # now handle the user given age and categorize the user age group
    if user_age < 13:
        print("User is a child")
    elif user_age < 20:
        print("User is a teenager")
    elif user_age < 31:
        print("User is a young adult")
    elif user_age < 65:
        print("User is  adult")
    else:
        print("User is a senior")
    break