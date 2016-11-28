class Person(object):
    staffs = []
    male_fellows = []
    female_fellows = []
    '''
    Models the informtion that the the class Fellow and Staff will inherit from
    '''

    def __init__(self, firstname, lastname, gender, position):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.position = position

    def add_person(self):
        '''
        Add person details to the system
        '''
        pass

    def validate_position(self):
        '''
        Validate that the person being added on the system is either
        a fellow or Staff
        '''
        pass

    def validate_gender(self):
        '''
        For living space alloction for the fellows, we use gender to group them
        '''
        pass

    def allocate_office(self):
        '''
        Allocates office to the people once they are added to the list
        at random. Allocates offices that are not full yet.
        '''
        pass

    def allocate_living_space(self):
        '''
        Allocates the fellows a living space if they want one.
        Have a default value of No.
        Allocates guys to the male wing and ladies to the female wing
        '''
        pass

    def load_people(self):
        '''
        Loads people to the system from a file.
        '''
        pass


class Fellow(Person):
    '''
    Inherits all the attribute of the Person.
    Can be allocated both office and living space but only if they want the living space
    '''
    pass

class Staff(Person):
    '''
    Inherits all the attributes of the Person.
    Can only be allocate office
    '''
    pass
kanyi = Person('steve', 'kanyi', 'M', 'fellow')
tonny = Person('Kip', 'Ngeno', 'M', 'Staff')
print(kanyi.position)
print(tonny.position)
