def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))