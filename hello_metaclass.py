# hello_metaclass.py
# a simple metaclass
# this metaclass adds a 'hello' method to classes that use the metaclass
# meaning, those classes get a 'hello' method with no extra effort
# the metaclass takes care of the code generation for us
class HelloMeta(type):
    # a hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls

# try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

# create an instance of the metaclass. It should automatically have a hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()
greeter.greet() # greetings from <class '__main__.TryHello'>, a HelloMeta type class
