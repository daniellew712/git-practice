def max_value(numbers):
<<<<<<< HEAD
    """ This function returns the largest number
        in the list.
    """

    max = numbers[0]
    for num in numbers:
        if num > max:
            max =num
    return max
=======
    return max(numbers)
>>>>>>> dc32106ffafc688cf8108cf4a905d4a09121b144


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
