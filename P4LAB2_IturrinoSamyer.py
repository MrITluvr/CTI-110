def display_multiplication_table(number):
    """Displays the multiplication table for the given number from 1 to 12 using a for loop."""
    for i in range(1, 13):
        print(f"{number} * {i} = {number * i}")

def main():
    while True:
        # Ask the user to enter an integer
        user_input = input("Please enter an integer: ")
        
        # Try to convert the input to an integer
        try:
            number = int(user_input)
            
            # If the number is negative, inform the user and ask for a new number
            if number < 0:
                print("You cannot enter negative values. Please try again.")
                continue  # Go back to the start of the loop
                
            # Display the multiplication table using a for loop
            print(f"\nMultiplication table for {number}:")
            display_multiplication_table(number)
            
            # Ask the user if they want to run the program again
            run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
            
            # Check if the user wants to continue or exit
            if run_again == "no":
                print("Thank you for using the multiplication table program!")
                break  # Exit the while loop and end the program
            elif run_again != "yes":
                print("Invalid input! Exiting the program.")
                break  # Exit if the user enters anything other than "yes" or "no"
        
        except ValueError:
            # Handle the case where the user doesn't enter a valid integer
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
