print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percent = tip / 100
tip_amount = bill * percent
total = bill + tip_amount
amount = total / people

print(f"Each person should pay: {'%.2f' %amount}")
