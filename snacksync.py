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

print("========================================")
print("              SNACKSYNC")
print("        Your Campus Food, Synced.")
print("========================================")

print("\n1. SideQuest")
print("2. Brew & Bloom")
print("3. Exit")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    print("\nWelcome to SideQuest!")
    
    print("\n---------- SIDEQUEST MENU ----------")
    for item, price in sidequest.items():
        print(item, "₹", price)

elif choice == 2:
    print("\nWelcome to Brew & Bloom!")
    
    print("\n------- BREW & BLOOM MENU -------")
    for item, price in brew_bloom.items():
        print(item, "₹", price)

elif choice == 3:
    print("\nThank you for using SnackSync!")

else:
    print("\nInvalid choice. Please try again.")
