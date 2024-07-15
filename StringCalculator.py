def handle_null_or_zero_input(input_str):
    return not input_str or input_str.strip() == "" or input_str.strip() == "0"

def parse_input_string(input_str):
    delimiter = determine_delimiter(input_str)
    numbers_str = extract_numbers_string(input_str)

    return split_numbers(numbers_str, delimiter)

def determine_delimiter(input_str):
    if input_str.startswith("//"):
        delimiter_end_idx = input_str.find("\n")
        if delimiter_end_idx != -1:
            return input_str[2:delimiter_end_idx]
    return ","

def extract_numbers_string(input_str):
    if input_str.startswith("//"):
        delimiter_end_idx = input_str.find("\n")
        if delimiter_end_idx != -1:
            return input_str[delimiter_end_idx + 1:]
    return input_str

def split_numbers(numbers_str, delimiter):
    return [num.strip() for num in numbers_str.replace('\n', delimiter).split(delimiter)]

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

