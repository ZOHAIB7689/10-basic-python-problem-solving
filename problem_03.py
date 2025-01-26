# Problem Assign a letter grade based on student's score A(90-100) B(80-89) C(70-79) D(50-69) F(50)

# get the score from user 
score = input("Enter your score:  ")
score = int(score)

if score > 100:
    print("Please enter a valid score")
    exit()

# now handle the user given score and categorize the user score group
if score >= 90:
    grade = "A"
elif score  >= 80:
    grade ="B"
elif score >= 70:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"


print("Your grade is: ", grade.upper())