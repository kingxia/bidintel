from enum import IntEnum

class Term(IntEnum):
    FALL = 0
    WINTER = 1
    SPRING = 2

class CourseType(IntEnum):
    GENERAL_ELECTIVE = 0
    MULTISECTION = 1
    CLINIC = 2
    INTERNATIONAL = 3

class NextId(IntEnum):
    PROFESSOR = 0
    COURSE = 1
    FULL_COURSE = 2
    USER = 3
    BID = 4

class User():
    def __init__(self, u_id, bids=[], bid_string=''):
        self.id = u_id
        self.bids = bids if len(bids) > 0 else self.bid_string_to_bids(bid_string)

    def has_bids(self):
        return len(self.bids) > 0

    def bid_string(self):
        return ','.join([str(bid) for bid in self.bids])

    def bid_string_to_bids(self, s):
        return [int(bid) for bid in s.split(',')]

class Course():
    def __init__(self, c_id, name, course_type):
        self.id = c_id
        self.name = name
        self.type = course_type

class FullCourse():
    def __init__(self, _id, c_id, p_id):
        self.id = _id
        self.c_id = c_id
        self.p_id = p_id

class Term():
    def __init__(self, year, term):
        self.year = year ## int
        self.term = term ## Term

class Bid():
    def __init__(self, b_id, term, year, position):
        self.id = b_id ## int:    unique course id
        self.term = term ## Term
        self.year = year ## int
        self.position = position ## int

class Professor():
    def __init__(self, p_id, name):
        self.id = p_id ## int:    unique professor id
        self.name = name ## string: full professor name
