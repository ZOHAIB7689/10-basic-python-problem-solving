# Customize  a  coffee order : "small", "medium", "large", with an option of extra shot of expresso.
order_size = input("What size coffee would you like? (small, medium, large) ")
extra_shot = input("Would you like an extra shot of espresso? (yes, no) ")

if extra_shot == "yes":
         coffee = order_size + " with an extra shot of espresso"
else:
         coffee = order_size + "coffee"

print("Your order has been placed for a ", coffee)