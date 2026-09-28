# SnackSync - Order Management

from validation import get_positive_integer


def create_order(menu, items):
    orders = []

    while True:

        item_choice = get_positive_integer(
            "\nEnter item number: "
        )

        if item_choice < 1 or item_choice > len(items):
            print("Invalid item number. Please try again.")
            continue

        selected_item = items[item_choice - 1]
        price = menu[selected_item]

        quantity = get_positive_integer(
            "Enter quantity: "
        )

        order = {
            "item": selected_item,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        }

        orders.append(order)

        print("\nItem added to your order!")

        more = input(
            "Do you want to add another item? (y/n): "
        ).lower()

        if more != "y":
            break

    return orders