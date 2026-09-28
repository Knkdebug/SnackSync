# SnackSync - Billing Management


def calculate_total(orders):
    total = 0

    for order in orders:
        total += order["total"]

    return total


def display_bill(customer_name, cafe_name, orders, order_id):

    total = calculate_total(orders)

    print("\n" + "=" * 45)
    print("                 SNACKSYNC")
    print("              ORDER RECEIPT")
    print("=" * 45)

    print("Order ID :", order_id)
    print("Customer :", customer_name)
    print("Cafe     :", cafe_name)

    print("-" * 45)

    for order in orders:
        print(
            order["item"],
            "x", order["quantity"],
            "= ₹", order["total"]
        )

    print("-" * 45)
    print("TOTAL    : ₹", total)

    print("=" * 45)
    print("       Thank you for ordering!")
    print("=" * 45)

    return total