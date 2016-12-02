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



class Fellow(Person):

    def __init__(self, person_id, firstname,lastname):
        super(Fellow, self).__init__(person_id, firstname, lastname) #position='fellow')


class Staff(Person):

    def __init__(self, person_id, firstname, lastname):
        super(Staff, self).__init__(person_id, firstname, lastname) #position='staff')
