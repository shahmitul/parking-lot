import car
from slot import Slot


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance
        raise Exception("Can not initiate %s multiple times" % cls._instance.__class__)


class Parking(Singleton):
    """
        Main logic written in this class
        This store the slot data and allocate / deallocate the space
    """

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, allow_slots):
        """
        Helps to create a parking lot
        input: 
            allow_slots - int
        """
        allow_slots = int(allow_slots)

        if len(self.slots) > 0:
            print("Parking Lot is already created")
            return

        if allow_slots < 1:
            print("Number of slot: %s provided is incorrect." % allow_slots)
            return

        for i in range(1, allow_slots + 1):
            self.slots[i] = Slot(slot_no=i, available=True)
        print("Created a parking lot with %s slots" % allow_slots)

    def find_nearest_slot(self):
        """
            Method to find nearest available slot to the entry point
        """
        available_slots = [pslot for pslot in self.slots.values() if pslot.available]
        if not available_slots:
            return None

        return sorted(available_slots, key=lambda x: x.slot_no)[0]

    def park(self, reg_no, colour):
        """
        Helping to park car with recording reg number and colour
        
        input:
            reg_no - String
            colour - String
        """
        if not self._is_valid():
            return

        available_slot = self.find_nearest_slot()
        if available_slot:
            # create car object and save in the available slot
            available_slot.car = car.Car.create(reg_no, colour)
            available_slot.available = False
            print("Allocated slot number: %s" % (available_slot.slot_no))
        else:
            print("Sorry, parking lot is full")

    def leave(self, slot_no):
        """
            deallocate the slot once car left
        input:
            slot_no - Integer Type
        """
        slot_no = int(slot_no)
        if not self._is_valid():
            return

        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car:
                pslot.car = None
                pslot.available = True
                print("Slot number %s is free" % slot_no)
            else:
                print("No car is present at slot number %s" % slot_no)
        else:
            print("Sorry, slot number does not exist in parking lot.")

    def status(self):
        """
            Show the current situation of partking lot
        """

        if not self._is_valid():
            return

        print("Slot No\tRegistration No\tColour")
        for i in self.slots.values():
            if not i.available and i.car:
                print("%s\t%s\t%s" % (i.slot_no, i.car.reg_no, i.car.colour))

    def _is_valid(self):
        """
            Validation before doing any change in parking
        """
        if len(self.slots) == 0:
            print("Parking Lot not created")
            return False
        return True

    def registration_numbers_for_cars_with_colour(self, colour):
        """
        Find registration numbers of car with given colour in parking
        input: 
            colour - String
        """

        if not self._is_valid():
            return

        colour = colour.lower()

        reg_nos = []

        for pslot in self.slots.values():
            if not pslot.available and pslot.car and pslot.car.colour.lower() == colour:
                reg_nos.append(pslot.car.reg_no)

        if reg_nos:
            print(", ".join(reg_nos))
        else:
            print("Not found")

    def slot_numbers_for_cars_with_colour(self, colour):
        """
        Find slot numbers for cars with given colour in parking.
        input:
            colour - String
        """

        if not self._is_valid():
            return

        colour = colour.lower()

        slot_nos = []

        for pslot in self.slots.values():
            if not pslot.available and pslot.car and pslot.car.colour.lower() == colour:
                slot_nos.append(str(pslot.slot_no))

        if slot_nos:
            print(", ".join(slot_nos))
        else:
            print("Not found")

    def slot_number_for_registration_number(self, reg_no):
        """Method to find slot numbers in parking with given registration
        number.
        Input: reg_no - String Type
        """

        if not self._is_valid():
            return

        slot_no = ""
        for pslot in self.slots.values():
            if not pslot.available and pslot.car and pslot.car.reg_no == reg_no:
                slot_no = pslot.slot_no
                break

        if slot_no:
            print(slot_no)
        else:
            print("Not found")
