class Slot(object):
    """
    This is class which represents parking slot and
    operation related to it.
    """

    def __init__(self, slot_no=None, available=None):
        self.car = None
        self.slot_no = slot_no
        self.available = available

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        self._car = value

    @property
    def slot_no(self):
        return self._slot_no

    @slot_no.setter
    def slot_no(self, value):
        self._slot_no = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    def __repr__(self):
        return "<RegNo: %s & Colour: %s>" % (self.car.reg_no, self.car.colour)


class Car(object):
    """
    This is class which represents details of a car.
    """

    def __init__(self):
        self._reg_no = None
        self._colour = None

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = value

    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    @classmethod
    def create(cls, reg_no, colour):
        car_obj = cls()
        car_obj.reg_no = reg_no
        car_obj.colour = colour
        return car_obj
