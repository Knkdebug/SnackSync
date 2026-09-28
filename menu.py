# SnackSync - Menu Management

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


def show_cafes():
    print("\nChoose a Cafe:")
    print("1. SideQuest")
    print("2. Brew & Bloom")
    print("3. Exit")


def get_menu(choice):
    if choice == 1:
        return "SideQuest", sidequest
    elif choice == 2:
        return "Brew & Bloom", brew_bloom
    else:
        return None, None


def display_menu(menu):
    print("\n" + "-" * 35)
    print("              MENU")
    print("-" * 35)

    items = list(menu.keys())

    for i, item in enumerate(items, start=1):
        print(i, ".", item, "₹", menu[item])

    return items