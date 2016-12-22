from .person import *
from .room import *
import random
from db.models import (Base, AmityPersons, AmityRooms, DatabaseCreator, UnAllocated,
                          OfficeAllocations, LivingSpaceAllocations)
from sqlalchemy.sql import select



class Amity(object):
    office_rooms = defaultdict(list)
    ls_rooms = defaultdict(list)
    all_rooms  = {}
    staffs = []
    fellows = []
    all_people = {}
    unallocated_person = {}


    @staticmethod
    def create_room(room_name, room_type):
        '''
        Check that the room does not exist and determine what type of room it is
        '''
        if room_name in Amity.all_rooms:
            print('Room already exists')
            return 'Room already exists'
        elif room_type.upper() == 'O':
            current_room = Office(room_name)
            Amity.all_rooms[current_room.room_name.upper()] = current_room.room_type
            Amity.office_rooms[current_room.room_name.upper()]
            print('%s created succesfully' % room_name)

        elif room_type.upper() == 'L':
            current_room = LivingSpace(room_name)
            Amity.all_rooms[current_room.room_name.upper()] = current_room.room_type
            Amity.ls_rooms[current_room.room_name.upper()]
            print('%s created succesfully' % room_name)
        else:
            print('%s is an invalid room type' % room_type)

    @staticmethod
    def add_person(firstname, lastname, position, wants_accomodation='N'):
        '''
        Add person details to the system
        '''
        full_name = firstname + " " + lastname
        person_id = len(list(Amity.all_people)) + 1

        if full_name.upper() in Amity.all_people:
            print ('Person with %s id already exist.' % full_name)

        elif position.upper() == 'F' and wants_accomodation.upper() == 'Y':
            new_fellow = Fellow(person_id, firstname, lastname)
            Amity.all_people[new_fellow.full_name.upper()] = position
            Amity.fellows.append(new_fellow.full_name.upper())
            random_office = Amity.generate_random_office()
            random_ls = Amity.generate_random_living_space()
            if not random_office and not random_ls:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            elif not random_office and random_ls:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Amity.ls_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to a living space %s: " % (new_fellow.full_name, random_ls))
            elif not random_ls and random_office:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Amity.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to an office %s: " % (new_fellow.full_name, random_office))

            else:
                Amity.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))
                Amity.ls_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_ls))

        elif position.upper() == 'F':
            new_fellow = Fellow(person_id, firstname, lastname)
            Amity.all_people[new_fellow.full_name.upper()] = position
            Amity.fellows.append(new_fellow.full_name.upper())
            random_office = Amity.generate_random_office()
            if not random_office:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            else:
                Amity.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))

        elif position.upper() == 'S' and wants_accomodation.upper() == 'Y':
            new_staff = Staff(person_id, firstname, lastname)
            Amity.all_people[new_staff.full_name.upper()] = position
            Amity.staffs.append(new_staff.full_name)
            random_office = Amity.generate_random_office()
            if not random_office:
                Amity.unallocated_person[new_staff .full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
                print('Staff cannot be llocated a living space')
            else:
                Amity.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))
                print('Staff cannot be llocated a living space')

        elif position.upper() == 'S':
            new_staff = Staff(person_id, firstname, lastname)
            Amity.all_people[new_staff.full_name.upper()] = position
            Amity.staffs.append(new_staff.full_name.upper())
            random_office = Amity.generate_random_office()
            if not random_office:
                Amity.unallocated_person[new_staff.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
            else:
                Amity.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))

        else:
            print('%s is not a valid position.' % position)

    @staticmethod
    def load_people(filename):
        '''
        Loads people to the system from a text file.
        '''
        if filename:
            with open(filename) as people_file:
                for line in people_file:
                    people_details = line.split()
                    if len(people_details) == 4:
                        Amity.add_person(firstname=people_details[0], lastname=people_details[1],
                        position=people_details[2], wants_accomodation=people_details[3])
                    elif len(people_details) == 3:
                        Amity.add_person(firstname=people_details[0], lastname=people_details[1],
                        position=people_details[2], wants_accomodation='N')
                    else:
                        print('Cannot process the data provided')
        else:
            print('Provide a file, please')

    @staticmethod
    def generate_random_office():
        '''
        Generates a random office that is not full
        '''
        available_offices = [room for room in Amity.office_rooms if len(Amity.office_rooms[room]) < 6]

        if len(available_offices) > 0:
            random_office = random.choice(available_offices)
            return random_office
        else:
            print('No offices availble')

    @staticmethod
    def generate_random_living_space():
        '''
        Generate a random living space that is not full_occupied
        '''
        available_ls = [room for room in Amity.ls_rooms if len(Amity.ls_rooms[room]) < 4]

        if len(available_ls) > 0:
            random_ls = random.choice(available_ls)
            return random_ls
        else:
            print('No living space available')

    @staticmethod
    def reallocate_person_to_office(full_name, new_room_name):
        '''
        use the person full name to remove the person from one office
        to another
        '''
        full_name = full_name.upper()
        if not full_name in Amity.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Amity.office_rooms[new_room_name]) == 6:
            return '%s is already full' % new_room_name

        if full_name in Amity.office_rooms[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Amity.office_rooms.items()):
            if full_name in members:
                Amity.office_rooms[room].remove(full_name)
                Amity.office_rooms[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))

    @staticmethod
    def reallocate_person_to_ls(full_name, new_room_name):
        '''
        use the person full name to remove the person from one livingspace
        to another, should not reallocate to the same room or a room that is full
        '''
        full_name = full_name.upper()
        if not full_name in Amity.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Amity.ls_rooms[new_room_name]) == 4:
            return '%s is already full' % new_room_name

        if full_name in Amity.ls_rooms[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Amity.ls_rooms.items()):
            if full_name in members:
                Amity.ls_rooms[room].remove(full_name)
                Amity.ls_rooms[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))


    @staticmethod
    def print_room(room_name):
        '''
        prints a room and all the people allocated to that room
        '''
        if room_name.upper() in Amity.office_rooms.keys():
            print(room_name.upper())
            print('-' * 50)
            print(', '.join(Amity.office_rooms[room_name.upper()]))

        elif room_name.upper() in Amity.ls_rooms.keys():
            print(room_name.upper())
            print('-' * 50)
            print(' ,'.join(Amity.ls_rooms[room_name.upper()]))
        else:
            print('There is no room called %s in Amity' % room_name)

    @staticmethod
    def print_allocations(filename=''):
        '''
        prints a list of all the people that have been allocated a room
        '''

        if filename:
            with open(filename, 'w') as allocation:
                print("\nWriting to the file .., \n")
                response = 'People in offices \n'
                for room, name in Amity.office_rooms.items():
                    response = response + (room + '\n')
                    response = response + '-' * 50 + '\n'
                    response = response + (', '.join(name) + '\n')
                    allocation.write(response)

                response = 'People in living space \n'
                for room, name in Amity.ls_rooms.items():
                    response = response + (room + '\n')
                    response = response + '-' * 50 + '\n'
                    response = response + (', '.join(name) + '\n')
                    allocation.write(response)
        else:
            print('People in office')
            for room, name in Amity.office_rooms.items():
                print(room)
                print('-' * 50)
                print(', '.join(name))
                print('=' * 50)

            print('People in Living space rooms')
            for room, name in Amity.ls_rooms.items():
                print(room)
                print('-' * 50)
                print(', '.join(name))
                print('=' * 50)

    @staticmethod
    def print_unallocated(filename=''):
        '''
        prints a list of people that have not been allocated to a room yet
        '''
        if filename:
            with open(filename, 'w') as unallocated:
                print("\nWriting to the file .., \n")
                response = 'People who are not allocated a living space \n'
                response = response + '-' * 50 + '\n'
                response = response + ', '.join(Amity.unallocated_person)
                unallocated.write(response)
        else:
            print('People not in an room')
            print(', '.join(Amity.unallocated_person))

    @staticmethod
    def load_state(db_name):
        '''
        loads the data from database to the app
        '''
        if db_name:
            db = DatabaseCreator(db_name)
        else:
            db = DatabaseCreator('default_db')

        Base.metadata.bind = db.engine

        db_session = db.session

        #load people from database
        people_in_db = select([AmityPersons])
        result = db.session.execute(people_in_db)
        for person in result.fetchall():
            name = person.name
            position = person.position
            Amity.all_people[name] = position

        db_session.close()

        #load rooms from database
        rooms_in_db = select([AmityRooms])
        result = db.session.execute(rooms_in_db)
        for room in result.fetchall():
            name = room.name
            room_type = room.room_type
            Amity.all_rooms[name] = room_type

        db_session.close()

        #load office allocations from database
        people_in_offices = select([OfficeAllocations])
        result = db.session.execute(people_in_offices)
        for room in result.fetchall():
            room_name = room.room_name
            member = room.members
            Amity.office_rooms[room_name]
            if member not in Amity.office_rooms[room_name]:
                Amity.office_rooms[room_name].append(member)

        db_session.close()

        #load living space allocations from database
        people_in_ls = select([LivingSpaceAllocations])
        result = db.session.execute(people_in_ls)
        for person in result.fetchall():
            room_name = person.room_name
            member = person.members
            Amity.ls_rooms[room_name]
            if member not in Amity.ls_rooms[room_name]:
                Amity.ls_rooms[room_name].append(member)

        db_session.close()

        #load unalloccated people from database
        unallocated_people = select([UnAllocated])
        result = db.session.execute(unallocated_people)
        for person in result.fetchall():
            name = person.name
            if name not in Amity.unallocated_person:
                Amity.unallocated_person.append(name)

        db_session.close()

    @staticmethod
    def save_state(db_name='default_db'):
        '''
        Saves the data in the app to the database
        '''
        if db_name:
            db = DatabaseCreator(db_name)
        else:
            db = DatabaseCreator('default_db')

        Base.metadata.bind = db.engine

        db_session = db.session

        #save people to database
        people_in_db = select([AmityPersons])
        result = db_session.execute(people_in_db)
        people_list = [item.name for item in result]

        for full_name, position in Amity.all_people.items():
            if full_name not in people_list:
                new_person = AmityPersons(name = full_name,
                                          position=position)
                db.session.add(new_person)
                db.session.commit()

        # saves the rooms to database
        rooms_in_db = select([AmityRooms])
        result = db.session.execute(rooms_in_db)
        rooms_list = [item.name for item in result]

        for room, r_type in Amity.all_rooms.items():
            if room not in rooms_list:
                new_room = AmityRooms(name=room,
                                      room_type=r_type)
                db.session.add(new_room)
                db.session.commit()

        #saves the people in offices
        peopl_in_office = select([OfficeAllocations])
        result = db.session.execute(peopl_in_office)
        office_people_list = [person.members for person in result]
        for room, members in Amity.office_rooms.items():
            for member in members:
                if member not in office_people_list:
                    new_room = OfficeAllocations(room_name=room,
                                                 members=member)
                    db.session.add(new_room)
                    db.session.commit()

        #saves the people in livingspace
        peopl_in_ls = select([LivingSpaceAllocations])
        result = db.session.execute(peopl_in_ls)
        ls_people_list = [person.members for person in result]
        for room, members in Amity.ls_rooms.items():
            for member in members:
                if member not in ls_people_list:
                    new_room = LivingSpaceAllocations(room_name=room,
                                                 members=member)
                    db.session.add(new_room)
                    db.session.commit()

        #saves the fellow who are not allocated a livingspace
        unallocated_people = select([UnAllocated])
        result = db.session.execute(unallocated_people)
        unallocated_people_list = [person.name for person in result]
        for person in Amity.unallocated_person:
            if person not in unallocated_people_list:
                new_room = UnAllocated(name=person)

                db.session.add(new_room)
                db.session.commit()
