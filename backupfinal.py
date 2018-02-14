# final.py

class Final(type):
    def __new__(cls, name, bases, attr):
        # Final cannot be subclassed
        # check that a Final class has not been passed as a base
        # if so, raise error, else, create the new class with Final attributes
        type_arr = [type(x) for x in bases]
        for i in type_arr:
            print(i)
            print(isinstance(i, Final))
            if i is Final:
                raise RuntimeError("You cannot subclass a Final class")
        return super(Final, cls).__new__(cls, name, bases, attr)


# use the metaclass to create a Cop class that is final

class Cop(metaclass=Final):

    def exit():
        print("Exiting...")
        quit()

# attempt to subclass the Cop class, this should idealy raise an exception!
class FakeCop(Cop):

    def scam():
        print("This is a hold up!")



# more tests, another Final class
class Goat(metaclass=Final):
    location = "Goatland"

# subclassing a final class should fail
class BillyGoat(Goat):
    location = "Billyland"
