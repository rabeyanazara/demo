def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(number) / len(number)


def login(password):
    if password == "admin123":
        return True
    return False
