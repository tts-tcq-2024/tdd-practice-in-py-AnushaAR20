def add_numbers(input_str):
    # Handle null input
    if not input_str or input_str.strip() == "":
        return 0

    # Split the input string by comma or newline character
    numbers = input_str.replace('\n', ',').split(',')

    # Convert the split strings to integers
    try:
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
    except (ValueError, IndexError):
        return "Invalid input. Please enter two numbers separated by a comma or a newline."

    # Ensure both numbers are within the range of 0 to 999
    if 0 <= num1 <= 999 and 0 <= num2 <= 999:
        return num1 + num2
    else:
        return "Both numbers must be between 0 and 999."

# Example usage
input_str = "123, 456"  # or "123\n456"
result = add_numbers(input_str)
print(result)  # Output should be 579

# Example with null input
input_str = ""
result = add_numbers(input_str)
print(result)  # Output should be 0










