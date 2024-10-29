# Samyer Iturrino
# 10/29/24
# P3HW2 - Salary Calculation
# Calculate and display an employee's regular pay, overtime pay, and gross pay.

# Input: Employee name, hours worked, and pay rate

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Define the threshold for regular hours and overtime multiplier

REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

# Calculate regular hours, overtime hours, and pay

if hours_worked > REGULAR_HOURS:
    regular_hours = REGULAR_HOURS
    overtime_hours = hours_worked - REGULAR_HOURS
else:
    regular_hours = hours_worked
    overtime_hours = 0

# Calculate pay based on regular and overtime hours

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * OVERTIME_MULTIPLIER
gross_pay = regular_pay + overtime_pay

# Display the result

print("\n-------------------------------------------")
print(f"Employee name: {employee_name}")
print("-------------------------------------------")
print(f"Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
print(f"{hours_worked:<15}  {pay_rate:<10}  {overtime_hours:<10}  {overtime_pay:<15.2f}  {regular_pay:<12.2f}  {gross_pay:<10.2f}")
print("----------------------------------------------------------------------------------------------------")
