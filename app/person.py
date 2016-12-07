from .room import Room

class Person(object):
    '''
    Models the informtion of a person that the the
    class Fellow and Staff will inherit from
    '''

    def __init__(self, person_id, firstname, lastname, position=''):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.position = position


class Fellow(Person):

    def __init__(self, *args, **kwargs):
        super(Fellow, self).__init__(*args, **kwargs)


class Staff(Person):

    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)
