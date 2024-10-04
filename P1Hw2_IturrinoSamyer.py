# Samyer Iturrino
# 10/01/24
# P1HW2
# This program will get info from the user and diplay the amount they will spend


print("This program calculates and displays travel expenses")
print()

# Get inputs from the user

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

fuel = float(input("How much do you think you will spend on gas? "))

accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))

food = float(input("Last, how much do you need for food? "))
print()
print()
print()

# Calculate remaining balance

remaining_balance = budget - (fuel + accommodation + food)
# Display the travel expenses

print("------------Travel Expenses------------")
print()
print("Location: ", destination)
print()
print("Initial Budget: ", budget)
print()
print("Fuel: ", fuel)
print()
print("Accommodation: ", accommodation)
print()
print("Food: ", food)
print()
print("Remaining Balance: ", remaining_balance)
print()
