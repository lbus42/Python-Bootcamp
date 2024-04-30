print("Welcome to the tip calculator!")

bill = input("How much is the total bill?\n")
bill_float = float(bill)

tip_percentage = input("What percentage do you want to tip? 10, 12, or 15?\n")
tip_float = float(tip_percentage)

number_of_split = input("How many people to split the bill?\n")
split_float = float(number_of_split)

tip = bill_float * tip_float / 100

total_bill = bill_float + tip


share = total_bill / split_float

print(f"Each person should pay: ${share:.2f}")
