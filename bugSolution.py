def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle lists with only non-numeric elements
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_mixed_list = [10, 20, 'a', 40, 50]
average_mixed = calculate_average(my_mixed_list)
print(f"The average of a mixed list is: {average_mixed}")

my_non_numeric_list = ['a', 'b', 'c']
average_non_numeric = calculate_average(my_non_numeric_list)
print(f"The average of a non-numeric list is: {average_non_numeric}") 