# בס״ד

def add(*args):
    """
    *args - creates a tuple of uniform values to loop through
    :param args:
    :return:
    """
    return sum(args)


print(add(2, 5, 9, 10))


class Car:
    def __init__(self, **kw):
        """
        **kwargs - creates a dictionary of the properties that can be used by using .get()
        :param kw:
        """
        self.model = kw.get('model')
        self.make = kw.get('make')


my_car = Car(make='BMW', model='X4')
my_car.owners = 3

print(my_car.model, my_car.owners)
