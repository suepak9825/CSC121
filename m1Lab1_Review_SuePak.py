# Program that takes as input the number of items, determines cost per item and displays cost per item and total order cost
# 5/31/2024
# CSC121 m1Lab1-Review
# Sue Pak

# Pseudocode:
# 1. Start an infinite loop.
# 2. Prompt the user to enter the number of items they want to purchase.
# 3. Convert the input to an integer.
# 4. If the number of items is less than 1:
#    a. Print an error message indicating the number must be greater than 0.
#    b. Continue to the next iteration of the loop.
# 5. Determine the cost per item based on the number of items.
# 6. Calculate the total cost by multiplying the number of items by the cost per item.
# 7. Print the cost per item.
# 8. Print the total cost.
# 9. Ask the user if they want to run the program again.
# 10. If the user responds with 'Yes' (case-insensitive), repeat from step 2.
# 11. If the user responds with anything other than 'Yes', break the loop and end the program.
# 12. Print a termination message.

while True:
    num_items = int(input("Enter the number of items you want to purchase: "))

    if num_items < 1:
        print("Invalid number of items. Please enter a number greater than 0.")
        continue

    if num_items <= 19:
        cost_per_item = 4.75
    elif num_items <= 49:
        cost_per_item = 4.50
    elif num_items <= 99:
        cost_per_item = 4.25
    else:
        cost_per_item = 4.00

    total_cost = num_items * cost_per_item

    print(f"The cost per item is ${cost_per_item:.2f}.")
    print(f"The total cost of your order is ${total_cost:.2f}.")

    response = input("Would you like to run the program again? (Yes/No): ")

    if response.lower() != 'yes':
        break

print("Program terminated.")
