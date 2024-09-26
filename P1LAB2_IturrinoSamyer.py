# Samyer Iturrino

# 9/26/24

# P1LAB2

# This code will get base value and exponent and return the answer


# Display output to user
print("------Calculating Exponents------")
print()
print()

# Get Info from user
base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()
print()

# Calculate the value of the exponent math
result = base_value ** exponent

# Display results of the math
print(base_value, "raised to the power of", exponent, "is", result, "!!")


# Display next output to user
print()
print()
print("------Addition and Subtraction------")
print()
print()

# Get info for addition and subtraction
start_int = int(input("Enter a starting integer: "))
add_int = int(input("Enter an integer to add: "))
minus_int = int(input("Enter an integer to subtract: "))
print()
print()
print()
print()

# Calculate equation
answer = start_int + add_int - minus_int

print(start_int, "+", add_int, "-", minus_int, "is equal to ", answer)
