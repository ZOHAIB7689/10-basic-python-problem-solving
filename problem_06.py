# Problem : suggest an activity based on the weather (e.g. sunny - Go for a walk , rainy - Read a book, snowy- Build a snowman, cloudy- Watch a movie)


# Prompt the user to enter the weather
print("How is the weather today?")
print("Sunny ,Rainy , Snowy , Cloudy")

weather = input("Enter the weather condition -> ").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book" 
elif weather == "snowy":
    activity = "Build a snowman"
elif weather == "cloudy":
    activity = "enjoy the weather with a cup of tea and samosa"

print("You should ", activity)