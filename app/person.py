from .room import Room

class Person(object):
    '''
    Models the informtion of a person that the the
    class Fellow and Staff will inherit from
    '''
    staffs = []
    male_fellows = []
    female_fellows = []

    def __init__(self, person_id, firstname, lastname, gender='', position=''):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.position = position

    @staticmethod
    def add_person(person_id, firstname, lastname, gender, position):
        '''
        Add person details to the system
        '''
        pass

    @staticmethod
    def allocate_office():
        '''
        Allocates office to the people once they are added to the list
        at rand1om. Allocates offices that are not full yet.
        '''
        pass

    @staticmethod
    def allocate_living_space(want_accomodation = 'N'):
        '''
        Allocates the fellows a living space if they want one.
        Have a default value of No.
        '''
        pass


class Fellow(Person):

    def __init__(self, *args, **kwargs):
        super(Fellow, self).__init__(*args, **kwargs)


class Staff(Person):

    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)
