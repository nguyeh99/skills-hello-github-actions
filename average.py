def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def calculate_maximum(numbers):
    if not numbers:
        return None

    return max(numbers)

if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))
    print(calculate_maximum([10, 20, 30]))
