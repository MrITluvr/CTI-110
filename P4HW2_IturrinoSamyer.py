# Samyer Iturrino
# Nov 12 2024
# P4HW2
# Employee payroll Calculator



def main():
    employees = []
    
    while True:
        # Input employee's name
        name = input("Enter employee's name or 'Done' to terminate: ")
        if name.lower() == "done":
            break
            
        # Input hours worked and pay rate
        hours_worked = float(input(f"How many hours did {name} work? "))
        pay_rate = float(input(f"What is {name}'s pay rate? "))
        
        # Calculate regular and overtime pay
        if hours_worked > 40:
            regular_hours = 40
            overtime_hours = hours_worked - 40
        else:
            regular_hours = hours_worked
            overtime_hours = 0
        
        reg_hour_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * pay_rate * 1.5
        gross_pay = reg_hour_pay + overtime_pay
        
        # Store employee data
        employees.append({
            "name": name,
            "hours_worked": hours_worked,
            "pay_rate": pay_rate,
            "overtime_hours": overtime_hours,
            "overtime_pay": overtime_pay,
            "reg_hour_pay": reg_hour_pay,
            "gross_pay": gross_pay
        })
        
        # Display individual employee's payroll information in a formatted table
        print("\nEmployee name:", name)
        print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'Overtime':<10} {'Overtime Pay':<15} {'RegHour Pay':<15} {'Gross Pay'}")
        print("--------------------------------------------------------------------------------")
        print(f"{hours_worked:<15.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} ${overtime_pay:<14.2f} ${reg_hour_pay:<14.2f} ${gross_pay:.2f}\n")
    
    # Calculate totals
    total_employees = len(employees)
    total_overtime_pay = sum(emp["overtime_pay"] for emp in employees)
    total_reg_hour_pay = sum(emp["reg_hour_pay"] for emp in employees)
    total_gross_pay = sum(emp["gross_pay"] for emp in employees)
    
    # Display summary information in the specified format
    print("\nEnter employee's name or 'Done' to terminate: Done")
    print(f"\nTotal number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_reg_hour_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

if __name__ == "__main__":
    main()
