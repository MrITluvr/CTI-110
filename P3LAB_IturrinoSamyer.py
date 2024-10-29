# Samyer Iturrino
# 10/25/24
# P3LAB3
# This will get a total of money and show the change


amount = float(input("Enter the amount of money as a float: $"))

#See if the amount is zero
if amount == 0:
    print("No change")
else:
    #Break down the amount into dollars, quarters, dimes, nickels, and pennies
    dollars = int(amount)
    cents = round((amount - dollars) * 100)

    quarters = cents // 25
    remaining_cents = cents % 25

    dimes = remaining_cents // 10
    remaining_cents %= 10

    nickels = remaining_cents // 5
    pennies = remaining_cents % 5

    # Show Results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else ''}")
