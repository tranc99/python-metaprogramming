class AttributeInitType(type):
    def __call__(self, *args, **kwargs):
        """Create a new instance"""

        # create the object in the normal default way
        obj = type.__call__(self, *args)

        # set attributes on the new object
        for name, value in kwargs.items():
            setattr(obj, name, value)

        # return the new object
        return obj

class Car(object, metaclass=AttributeInitType):

    @property
    def description(self):
        """Return a description of this car"""
        return " ".join(str(value) for value in self.__dict__.values())
