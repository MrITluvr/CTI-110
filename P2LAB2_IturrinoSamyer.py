# Samyer Iturrino
# October 10 2024
# P2LAB1
# Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user



# Create the dictionary with vehicles and their MPG values

vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,

    }


# keys
keys = vehicle_mpg.keys()

# Print
print(keys)
print()

# Prompt the user to enter a vehicle
selected_vehicle = input("\nEnter a vehicle to see its MPG: ")

# Check if the vehicle exists in the dictionary
if selected_vehicle in vehicle_mpg:

# Get the MPG for the selected vehicle
    mpg = vehicle_mpg[selected_vehicle]
print(f"\nThe {selected_vehicle} gets {mpg} MPG.")
print()

# Ask the user how many miles they plan to drive
miles = float(input(f"How many miles will you drive the {selected_vehicle}? "))
print()

# Calculate the gallons of gas needed
gallons_needed = miles / mpg
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {selected_vehicle} {miles} miles.")
