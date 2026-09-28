# SnackSync - Input Validation

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(prompt):
    while True:
        value = get_integer(prompt)

        if value > 0:
            return value

        print("Please enter a number greater than 0.")