print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road.")

first = input('Where do you want to go?  Type "left" or "right"\n')
if first == "left":
    print("You turned left")
else:
    print("You turned right")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")

else:
    print("Sorry, you have to grow a little")
