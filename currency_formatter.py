"""Currency Formatter

This example demonstrates how to converts a float value to currency.

The function car_value_without_fees is just an example about how to use to_currency as a decorator.
"""

def decorator_to_currency(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return to_currency(value)
    return wrapper

def to_currency(value):
    # The first line converts to currency, but it converts to USA format
    formatted_value = f'{value:,.2f}'

    # The next lines convert the USA format to BR format
    formatted_value = formatted_value.replace('.', '_')
    formatted_value = formatted_value.replace(',', '.')
    formatted_value = formatted_value.replace('_', ',')
    return formatted_value

@decorator_to_currency
def car_value_without_fees(value):
    """Return car price without fees, using discount for 
    
    Arguments:
        value {float} -- This parameter should be int or float
    
    Returns:
        float -- Returns a net value
    """
    return value - (value * 0.22)


if __name__ == "__main__":
    # Python ignore the underscore, so we can use to improve code readability
    value = 69_999.99

    print(car_value_without_fees(value))

