from .room import Room


class Person(object):
    '''
    Models the informtion of a person that the the
    class Fellow and Staff will inherit from
    '''
    staffs = []
    male_fellows = []
    female_fellows = []
    all_people = {}

    def __init__(self, person_id, firstname, lastname, position=''):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.position = position

    @staticmethod
    def add_person(person_id, firstname, lastname, position):
        '''
        Add person details to the system
        '''
        pass

    @staticmethod
    def load_people(filename):
        '''
        Loads people to the system from a text file.
        '''
        pass

    @staticmethod
    def allocate_office(room_name):
        '''
        Allocates office to the people once they are added to the list
        at random. Allocates offices that are not full yet.
        '''
        pass

    @staticmethod
    def allocate_living_space(room_name, want_accomodation = 'N'):
        '''
        Allocates the fellows a living space if they want one.
        Have a default value of No.
        '''
        pass

    @staticmethod
    def reallocate_person(person_id, new_room_name):
        '''
        use the person id to remove the person from one office
        to another
        '''
        pass


class Fellow(Person):

    def __init__(self, *args, **kwargs):
        super(Fellow, self).__init__(*args, **kwargs)


class Staff(Person):

    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)
