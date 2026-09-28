# SnackSync - Canteen Management System

from menu import show_cafes, get_menu, display_menu
from customer import get_customer_name
from ordering import create_order
from billing import display_bill
from validation import get_integer
from utils import generate_order_id, show_header


def main():

    show_header()

    customer_name = get_customer_name()

    while True:

        show_cafes()

        choice = get_integer(
            "\nEnter your choice: "
        )

        if choice == 3:
            print("\nThank you for using SnackSync!")
            break

        if choice != 1 and choice != 2:
            print("\nInvalid cafe choice. Please try again.")
            continue

        cafe_name, menu = get_menu(choice)

        print("\nWelcome to", cafe_name)

        items = display_menu(menu)

        orders = create_order(menu, items)

        order_id = generate_order_id()

        display_bill(
            customer_name,
            cafe_name,
            orders,
            order_id
        )


if __name__ == "__main__":
    main()