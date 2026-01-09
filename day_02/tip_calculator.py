print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
bill = int(bill)

tip = input("How much tip would you like to give? 10, 12, or 15? ")
tip = 1 + (int(tip) / 100)

people = input("How many people to split the bill? ")
people = int(people)

pay =bill * tip / people
pay = round(pay, 2)

print("Each person should pay: $" + str(pay))