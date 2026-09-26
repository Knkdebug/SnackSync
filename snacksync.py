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

print("1. SideQuest")
print("2. Brew & Bloom")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Welcome to SideQuest!")
elif choice == 2:
    print("Welcome to Brew & Bloom!")
elif choice == 3:
    print("Thank you for using SnackSync!")
else:
    print("Invalid choice. Please try again.")
