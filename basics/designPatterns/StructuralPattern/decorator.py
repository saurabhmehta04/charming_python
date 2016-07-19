from functools import wraps


def make_blink(function):
    ''' Defines the decorator'''

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator():
        ret = function()

        return "<blink>" + ret + "</blink>"

    return decorator


# Apply the decorator here !
@make_blink
def hello_world():
    ''' Original function'''

    return "hello World !"


# check the result of decorating
print(hello_world())

# check if the function name is still the name of the function being decorated
print(
    hello_world.__name__)  # => prints name of the function, (otherwise "decorator") since we use @wraps(func), docstring is also passed.

# check if the decorating is still the same as that of the function being decorated
print(
    hello_world.__doc__)  # => prints the doc string "Original function" doc string, otherwise None, because of wraps(func)
