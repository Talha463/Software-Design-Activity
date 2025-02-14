def find_number(lst, target):
    for i, num in enumerate(lst):
        if num == target:
            return f"Number {target} found at index {i}"
    return f"Number {target} not found"

# Example usage
numbers = [10, 3, 7, 2, 8, 15, 6]
target = int(input("Enter a number to search for: "))
print(find_number(numbers, target))
