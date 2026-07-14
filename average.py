def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))

def calculate_maximum(numbers):
    if not numbers:
        return None

    return max(numbers)

print(calculate_maximum([10, 20, 30]))
