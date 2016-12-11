class Trial(object):
    """docstring for ."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.full_name = ''


    def try1(self, name):
        full_name = name
        return full_name


    def try2(self):
        return Trial.try1(self, self.full_name)
one = Trial('steve' , 24)
print(one.try1('stve'))
