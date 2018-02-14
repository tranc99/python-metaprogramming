import types

def notify(fn, *args, **kwargs):

    def fncomposite(*args, **kwargs):
        # normal notify functionality
        print("running %s" % fn.__name__)
        rt = fn(*args, **kwargs)
        return rt
    # return the composite function
    return fncomposite

class Notifies(type):

    def __new__(cls, name, bases, attr):
        # replace all functions with wrappers
        # or create a new dict that replaces each function with
        # a print statement of the function name
        # followed by running the computation with the provided args and returning the computation result
        for name, value in attr.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                print(type(value))
                print(value)
                print(value.__name__)
                attr[name] = notify(value)

        return super(Notifies, cls).__new__(cls, name, bases, attr)

# test the metaclass

class Math(metaclass=Notifies):

    def multiply(a, b):
        product = a * b
        print(product)
        return product

Math.multiply(5, 6)
# running Math.multiply
# 30


class Shouter(metaclass=Notifies):

    def intro(self):
        print("I shout!")

s = Shouter()
s.intro()

def divide(a, b):
    result = a / b
    print(result)
    return result

div = notify(divide)

div(9, 3)
