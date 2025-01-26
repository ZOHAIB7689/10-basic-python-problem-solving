# Choose a mode of transportaion based on the distance (e.g., <3km - walk, <10km - bike, <50km - car)


# Prompt the user to enter the distance

distance  = input("Enter the distance in km -> ")
distance = int(distance)

if distance < 3:
    transport = "walk"
elif distance < 10:
    transport = "bike"
elif distance < 50:
    transport = "car"
elif distance > 50:
    transport = "bus or train"
elif distance >= 1000:
    transport = "plane"

print("You should take a ", transport)