# decorators.py

from functools import wraps

# create a new decorator named notifyfunc
def notifyfunc(fn):
    """prints out the function name before executing it"""
    @wraps(fn)
    def composite(*args, **kwargs):
        print("running %s" % fn.__name__)
        # run the original function and return the result, if any
        rt = fn(*args, **kwargs)
        return rt
    # return our composite function
    return composite

# apply our decorator to a normal function that prints out the result of multiplying its arguments
@notifyfunc
def multiply(a, b):
    product = a * b
    print(product)
    return product

# test the decorator
multiply(5, 6)
# test the decorator
multiply(89, 5)
