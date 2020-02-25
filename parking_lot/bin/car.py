class Car(object):
    """
    Set and Get Car Detail
    """

    def __init__(self):
        self._reg_no = None
        self._colour = None

    @property
    def reg_no(self):
        return self._reg_no.upper()

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value.lower()

    @property
    def colour(self):
        return self._colour.title()

    @colour.setter
    def colour(self, value):
        self._colour = value.lower()

    @classmethod
    def create(cls, reg_no, colour):
        car_obj = cls()
        car_obj.reg_no = reg_no.lower()
        car_obj.colour = colour.lower()
        return car_obj
