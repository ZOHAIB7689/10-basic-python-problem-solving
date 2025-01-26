# Check if a password id "Weak" ,"Medium","Strong" criteria <6 chars (weak),"Medium" 6-10,"Strong" >10

password = input("Enter your password -> ")

if len(password)< 6:
    strength = "Weak"
elif len(password) > 6:
    strength = "Medium"
elif len(password) > 10:
    strength = "Strong"

print("Your password strngth is ", strength)