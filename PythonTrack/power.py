def power_operation(base, exponent, **kwargs):
    result = base ** exponent
    if 'modulo' in kwargs:
        result %= kwargs['modulo']

    return result
