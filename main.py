def hello_world():
    return "Hello, World!"


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_largest_element(numbers):
    if not numbers:
        return None
    return max(numbers)


if __name__ == "__main__":
    print(hello_world())
