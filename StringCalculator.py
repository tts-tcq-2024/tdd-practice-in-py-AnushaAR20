def handle_null_input(input_str):
    return not input_str or input_str.strip() == ""

def split_and_strip_input(input_str):
    return [num.strip() for num in input_str.replace('\n', ',').split(',')]

def convert_to_ints(numbers):
    try:
        return int(numbers[0]), int(numbers[1])
    except (ValueError, IndexError):
        return None, None

def validate_numbers(num1, num2):
    return 0 <= num1 <= 999 and 0 <= num2 <= 999

def add_valid_numbers(num1, num2):
    return num1 + num2 if validate_numbers(num1, num2) else "Both numbers must be between 0 and 999."

def add(input_str):
    if handle_null_input(input_str):
        return 0
    
    numbers = split_and_strip_input(input_str)
    num1, num2 = convert_to_ints(numbers)
    if num1 is None or num2 is None:
        return "Invalid input. Please enter two numbers separated by a comma or a newline."
    
    return add_valid_numbers(num1, num2)










