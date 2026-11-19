# 10 Healthy Food Items
healthy_food = {
    "apple": 1.50,
    "banana": 0.75,
    "broccoli": 2.00,
    "carrot": 1.25,
    "spinach": 2.50,
    "oats": 3.50,
    "almonds": 5.00,
    "yogurt": 2.25,
    "salmon": 8.50,
    "avocado": 2.00,
}

# 10 Junk Food Items
junk_food = {
    "chips": 2.50,
    "soda": 1.75,
    "burger": 5.50,
    "pizza": 4.00,
    "candy": 1.25,
    "donut": 1.50,
    "ice cream": 4.50,
    "cookies": 3.00,
    "fries": 2.75,
    "chocolate": 2.00,
}

# Combine both dictionaries so we can easily look up prices later
all_products = {}
all_products.update(healthy_food)
all_products.update(junk_food)

# Stock for all 20 items
stock = {
    "apple": 10, "banana": 15, "broccoli": 8, "carrot": 12, "spinach": 7,
    "oats": 10, "almonds": 6, "yogurt": 9, "salmon": 5, "avocado": 10,
    "chips": 12, "soda": 20, "burger": 8, "pizza": 10, "candy": 25,
    "donut": 15, "ice cream": 8, "cookies": 14, "fries": 12, "chocolate": 18,
}

promo_codes = {"SAVE10": 0.10, "STUDENT": 0.15}
cart = []
total = 0.0

print("Welcome to my Python Grocery Store!")
print("Special Deal: Spend $15+ to save $2 | Spend $30+ to save $5!")

while True:
    print("\n--- MENU ---")
    print("1. Show Healthy Food")
    print("2. Show Junk Food")
    print("3. Add to cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    # 1. Show Healthy Food
    if choice == "1":
        print("\n--- HEALTHY FOOD ---")
        for item in healthy_food:
            print(item, "- $", healthy_food[item], "| Stock:", stock[item])

    # 2. Show Junk Food
    elif choice == "2":
        print("\n--- JUNK FOOD ---")
        for item in junk_food:
            print(item, "- $", junk_food[item], "| Stock:", stock[item])

    # 3. Add item to cart
    elif choice == "3":
        item_name = input("Enter item name: ").lower()
        if item_name in all_products:
            qty_input = input("How many? ")
            if qty_input.isdigit():
                qty = int(qty_input)
                if qty > 0 and qty <= stock[item_name]:
                    for i in range(qty):
                        cart.append(item_name)
                    stock[item_name] = stock[item_name] - qty
                    total = total + (all_products[item_name] * qty)
                    print("Added", qty, item_name, "to your cart!")
                else:
                    print("Not enough in stock or invalid amount.")
            else:
                print("Please enter a valid number.")
        else:
            print("Sorry, we don't have that item.")

    # 4. View current cart
    elif choice == "4":
        print("\nYour Cart:", cart)
        print("Current Total: $", round(total, 2))
        # Let the user know how close they are to a discount
        if total < 15:
            print("Spend $", round(15 - total, 2), "more to save $2.00!")
        elif total < 30:
            print("You unlocked $2.00 off! Spend $", round(30 - total, 2), "more to save $5.00!")
        else:
            print("You unlocked the maximum $5.00 bulk discount!")

    # 5. Checkout with bulk discounts and promo code
    elif choice == "5":
        if len(cart) == 0:
            print("Your cart is empty!")
        else:
            print("\nItems in cart:", cart)
            print("Subtotal: $", round(total, 2))

            # Apply spending-based dollar discounts
            if total >= 30:
                total = total - 5.00
                print("Bulk Discount Applied: You saved $5.00 for spending $30 or more!")
            elif total >= 15:
                total = total - 2.00
                print("Bulk Discount Applied: You saved $2.00 for spending $15 or more!")

            # Apply promo code on top of the discounted total
            code = input("Enter promo code (or press Enter to skip): ").upper()
            if code in promo_codes:
                discount = total * promo_codes[code]
                total = total - discount
                print("Promo code applied! You saved $", round(discount, 2))
            elif code != "":
                print("Invalid promo code.")

            print("Final Total to pay: $", round(total, 2))
            print("Thank you for shopping!")
            break

    # 6. Exit program
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
