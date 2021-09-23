from collections import namedtuple

# let's define a prototype hotelroom
from collections import namedtuple
HotelRoom = namedtuple("Hotelroom", ['beds', 'floor', 'cost', 'view'])

# create the first room
my_hotel_room = HotelRoom(beds=4, floor=2, cost=49.99, view='seaside')

# how to access the fields? ... like attributes
my_hotel_room.beds
my_hotel_room.view

# how to access the fields? ... also with positions
my_hotel_room[0]
my_hotel_room[3]

# which fields are there?
my_hotel_room._fields

# are there more rooms?
raw_data = [(1, 2, 49.99, 'streetside'),
            (2, 2, 39.99, 'streetside'),
            (3, 4, 29.99, 'seaside'),
            (4, 5, 49.99, 'seaside')]
my_rooms = [HotelRoom._make(row) for row in raw_data]


