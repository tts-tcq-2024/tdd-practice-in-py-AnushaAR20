def handle_null_or_zero_input(input_str):
    return not input_str or input_str.strip() == "" or input_str.strip() == "0"

def parse_input_string(input_str):
    delimiter = ","
    numbers_str = input_str.strip()

    if numbers_str.startswith("//"):
        delimiter_end_idx = numbers_str.find("\n")
        if delimiter_end_idx != -1:
            delimiter = numbers_str[2:delimiter_end_idx]
            numbers_str = numbers_str[delimiter_end_idx + 1:]

    numbers = [num.strip() for num in numbers_str.replace('\n', delimiter).split(delimiter)]
    return numbers

def convert_to_ints(numbers):
    try:
        return [int(num) for num in numbers]
    except ValueError:
        raise ValueError("Invalid input. Please enter valid numbers separated by the delimiter.")

def validate_numbers(numbers):
    return [num for num in numbers if num <= 1000]

def add(input_str):
    if handle_null_or_zero_input(input_str):
        return 0

    numbers = parse_input_string(input_str)
    numbers = convert_to_ints(numbers)
    numbers = validate_numbers(numbers)
    
    return sum(numbers)

