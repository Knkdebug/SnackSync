# SnackSync - Canteen Management System

sidequest = {
    "Classic Veg Burger": 80,
    "Peri Peri Fries": 70,
    "Paneer Wrap": 75,
    "White Sauce Pasta": 110,
    "Veg Pizza": 120,
    "Cold Drink": 40
}

brew_bloom = {
    "Cappuccino": 90,
    "Cold Coffee": 80,
    "Masala Tea": 40,
    "Chocolate Cake": 100,
    "Chocolate Cheesecake": 120,
    "Chocolate Chip Cookies": 50
}

print("=" * 45)
print("                 SNACKSYNC")
print("             Your Campus Food, Synced.")
print("=" * 45)

customer_name = input("Enter your name: ")

while True:

    print("\nChoose a Cafe:")
    print("1. SideQuest")
    print("2. Brew & Bloom")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        cafe_name = "SideQuest"
        menu = sidequest

    elif choice == 2:
        cafe_name = "Brew & Bloom"
        menu = brew_bloom

    elif choice == 3:
        print("\nThank you for using SnackSync!")
        break

    else:
        print("\nInvalid choice. Please try again.")
        continue

    print("\nWelcome to", cafe_name)
    print("-" * 35)
    print("              MENU")
    print("-" * 35)

    items = list(menu.keys())

    for i in range(len(items)):
        item = items[i]
        print(i + 1, ".", item, "₹", menu[item])

    item_choice = int(input("\nEnter item number: "))

    if item_choice >= 1 and item_choice <= len(items):

        selected_item = items[item_choice - 1]
        price = menu[selected_item]

        quantity = int(input("Enter quantity: "))

        total = price * quantity

        print("\n" + "=" * 35)
        print("             ORDER SUMMARY")
        print("=" * 35)
        print("Customer :", customer_name)
        print("Cafe     :", cafe_name)
        print("Item     :", selected_item)
        print("Quantity :", quantity)
        print("Price    : ₹", price)
        print("Total    : ₹", total)
        print("=" * 35)
        print("       Thank you for ordering!")
        print("=" * 35)

    else:
        print("\nInvalid item number.")# SnackSync - Canteen Management System

