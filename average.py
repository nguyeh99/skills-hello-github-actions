def calculate_average(numbers):
    """Return the arithmetic mean of a sequence of numbers.

    If ``numbers`` is empty, return 0 to match the existing behavior.

    Parameters:
        numbers (iterable of numbers): The values to average.

    Returns:
        float: The average of the numbers, or 0 if the input is empty.
    """
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def calculate_maximum(numbers):
    """Return the maximum value from a sequence of numbers.

    If ``numbers`` is empty, return ``None`` to match the existing behavior.

    Parameters:
        numbers (iterable): The values to examine.

    Returns:
        The maximum value from ``numbers``, or ``None`` if the input is empty.
    """
    if not numbers:
        return None

    return max(numbers)


if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))
    print(calculate_maximum([10, 20, 30]))
