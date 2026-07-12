user_age =int(input("Enter your age: "))
if user_age > 100:
    print("Sorry, you're dead.")
elif user_age >= 40:
    print("You're over the hill.")
elif user_age >= 65:
    print("enjoy your retirement.")
elif user_age < 13:
    print("You qualify for a kiddie discount.")
else:
    print("Age is but a number.")
