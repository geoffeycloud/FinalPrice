# This function calculates the final price after a discount is applied
def calculate_discount(original_price, discount_percentage):
    # Check if the discount is 20% or more
    if discount_percentage >= 20:
        # Calculate how much the discount is in dollar amount
        discount_amount = original_price * (discount_percentage / 100)
        # Subtract the discount from the original price to get the final price
        final_price = original_price - discount_amount
        # Return the final price after discount
        return final_price
    else:
        # If discount is less than 20%, just return the original price
        return original_price

# Ask the user for the original price of the item
user_original_price = float(input("What is the original price of the item? "))

# Ask the user for the discount percentage
user_discount_percentage = float(input("What is the discount percentage? "))

# Call the function with the user-provided values
calculated_final_price = calculate_discount(user_original_price, user_discount_percentage)

# Print the final price
print("The final price after the discount is:", calculated_final_price)