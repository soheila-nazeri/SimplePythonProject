def hello_world():
    return "Hello, World!"


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(hello_world())
