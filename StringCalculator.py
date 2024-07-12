def handle_null_input(input_str):
    return 0 if not input_str or input_str.strip() == "" else None

def split_and_strip_input(input_str):
    return [num.strip() for num in input_str.replace('\n', ',').split(',')]

def convert_to_ints(numbers):
    try:
        return int(numbers[0]), int(numbers[1])
    except (ValueError, IndexError):
        return None, None

def validate_numbers(num1, num2):
    return 0 <= num1 <= 999 and 0 <= num2 <= 999

def add(input_str):
    # Check for null input
    null_result = handle_null_input(input_str)
    if null_result is not None:
        return null_result

    # Split and strip input
    numbers = split_and_strip_input(input_str)

    # Convert to integers
    num1, num2 = convert_to_ints(numbers)
    if num1 is None or num2 is None:
        return "Invalid input. Please enter two numbers separated by a comma or a newline."

    # Validate numbers
    if validate_numbers(num1, num2):
        return num1 + num2
    else:
        return "Both numbers must be between 0 and 999."













