def basic_operations(a, b):
    results = {}

    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b

    if b != 0:
        results['division'] = a / b
    else:
        results['division'] = 'Error: Division by zero is not allowed'

    return results
