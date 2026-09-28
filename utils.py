# SnackSync - Utility Functions

import random


def generate_order_id():
    return "SNK" + str(random.randint(1000, 9999))


def show_header():
    print("=" * 45)
    print("                 SNACKSYNC")
    print("             Your Campus Food, Synced.")
    print("=" * 45)