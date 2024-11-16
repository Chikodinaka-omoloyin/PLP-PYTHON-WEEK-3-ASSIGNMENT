def calculate_discount(price, discount_percent):
    # If discount is 20% or more, calculate the discounted price
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    # Otherwise, return the original price
    return price

# Step 1: Get the original price and discount percentage from the user
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 2: Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Step 3: Display the result
if discount_percent >= 20:
    print(f"Final price after discount: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
