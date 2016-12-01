class Person(object):
    '''
    Models the informtion of a person that the the
    class Fellow and Staff will inherit from
    '''

    def __init__(self, person_id, firstname, lastname, gender='', position=''):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.position = position

class Fellow(Person):

    def __init__(self, person_id, firstname,lastname):
        super(Fellow, self).__init__(person_id, firstname, lastname) #position='fellow')


class Staff(Person):

    def __init__(self, person_id, firstname, lastname):
        super(Staff, self).__init__(person_id, firstname, lastname) #position='staff')
