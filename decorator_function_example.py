import unicodedata
"""Decorator function example

This example demonstrates how to use a decorator as a function
"""

def normalize_strings(func):
    """Converts accents to the closest possible ascii representation
    
    Arguments:
        func {str} -- String with accents
    
    Returns:
        str -- ascii representation of input string
    """
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        return ''.join((c for c in unicodedata.normalize('NFD', r) if unicodedata.category(c) != 'Mn'))
    return wrapper

@normalize_strings
def get_name():
    return "Andrew Aragão Scancari"

if __name__ == "__main__":
    print(get_name())
