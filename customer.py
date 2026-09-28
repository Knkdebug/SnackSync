# SnackSync - Customer Management

def get_customer_name():
    name = input("Enter your name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    return name