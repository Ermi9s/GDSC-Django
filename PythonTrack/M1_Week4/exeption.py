def basic_operations(a, b):
    results = {}
    try:
        results['addition'] = a + b
        results['subtraction'] = a - b
        results['multiplication'] = a * b
        results['division'] = a / b if b != 0 else 'Error: Division by zero is not allowed'
    except Exception as e:
        return str(e)

    return results

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            result %= kwargs['modulo']
    except Exception as e:
        return str(e)

    return result

def apply_operations(operation_list):
    try:
        return list(map(lambda operation: operation[0], operation_list))
    except Exception as e:
        return str(e)
