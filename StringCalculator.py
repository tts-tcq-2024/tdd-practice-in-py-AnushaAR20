def add(input_str):
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










