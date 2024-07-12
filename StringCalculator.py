def handle_null_input(input_str):
    return not input_str or input_str.strip() == ""

def split_and_strip_input(input_str):
    return [num.strip() for num in input_str.replace('\n', ',').split(',')]

def convert_to_ints(numbers):
    try:
        return int(numbers[0]), int(numbers[1])
    except (ValueError, IndexError):
        raise ValueError("Invalid input. Please enter two numbers separated by a comma or a newline.")

def validate_numbers(num1, num2):
    if 0 <= num1 <= 999 and 0 <= num2 <= 999:
        return num1, num2
    else:
        raise ValueError("Both numbers must be between 0 and 999.")

def prepare_numbers(input_str):
    if handle_null_input(input_str):
        return 0, 0

    numbers = split_and_strip_input(input_str)
    num1, num2 = convert_to_ints(numbers)
    return validate_numbers(num1, num2)

def add(num1, num2):
    return num1 + num2














