import sys
import os
import unittest

path = os.getcwd()
sys.path.append(os.path.join(*[path, "bin"]))

from source.parking import Parking  # NOQA


class TestCreateParking(unittest.TestCase):
    """
    These test cases are for create the parking space.
    Checking with valid slots, invalid(0 or negative value)
    """

    def setUp(self):
        self.parking = Parking()

    def test_create_parking_lot(self):
        slots = 6
        self.parking.create_parking_lot(slots)
        self.assertEqual(len(self.parking.slots), slots)

    def test_create_zero_parking_lot(self):
        slots = 0
        self.parking.create_parking_lot(slots)
        self.assertEqual(len(self.parking.slots), slots)

    def test_create_negative_parking_lot(self):
        slots = -3
        self.parking.create_parking_lot(slots)
        self.assertEqual(len(self.parking.slots), 0)


class TestParking(unittest.TestCase):
    def setUp(self):
        self.parking = Parking()
        self.parking.create_parking_lot(2)

    def park_two_car_default(self):
        reg_no1 = "MH-03-WS-1214"
        success, reg_num = self.parking.park(reg_no1, "White")
        self.assertTrue(success)
        self.assertEqual(reg_num, reg_no1)

        reg_no2 = "MH-03-WS-1215"
        success, reg_num = self.parking.park(reg_no2, "White")
        self.assertTrue(success)
        self.assertEqual(reg_num, reg_no2)

    def test_park(self):
        """
        Check if parking allowed or not.
        After parking check the status whether car is in parking slot or not.
        """
        test_name = "Car Park -- Start -- "
        print(test_name.center(200, "*"))

        self.park_two_car_default()

        reg_no3 = "MH-03-WS-1216"
        success, reg_num = self.parking.park(reg_no3, "White")
        self.assertFalse(success)
        self.assertIsNone(reg_num)

        car_regs = self.parking.status()
        self.assertIn("MH-03-WS-1214", car_regs)
        self.assertIn("MH-03-WS-1215", car_regs)
        self.assertNotIn(reg_no3, car_regs)
        test_name = "Car Park -- End -- "
        print(test_name.center(200, "*"))

    def test_leave(self):
        """
        check status once car left.
        """
        test_name = "Car Leave -- Start -- "
        print(test_name.center(200, "*"))

        self.park_two_car_default()

        self.parking.leave(2)
        self.parking.leave(1)

        reg_no3 = "MH-03-WS-1218"
        success, reg_num = self.parking.park(reg_no3, "White")
        self.assertTrue(success)
        self.assertEqual(reg_num, reg_no3)

        test_name = "Car Leave -- End -- "
        print(test_name.center(200, "*"))

    def test_registration_numbers_for_cars_with_colour(self):
        """
        Count the car by given colour
        """
        test_name = "Car Colour Test -- Start -- "
        print(test_name.center(200, "*"))
        self.park_two_car_default()
        reg_nos = self.parking.registration_numbers_for_cars_with_colour("White")
        self.assertEqual(len(reg_nos), 2)
        reg_nos = self.parking.registration_numbers_for_cars_with_colour("Black")
        self.assertEqual(len(reg_nos), 0)
        test_name = "Car Colour Test -- Start -- "
        print(test_name.center(200, "*"))

    def test_slot_number_for_registration_number(self):
        """
        Get the slot number where given car parked
        """
        test_name = "Car Slot Test -- Start -- "
        print(test_name.center(200, "*"))
        self.park_two_car_default()
        slot_no1 = self.parking.slot_number_for_registration_number("MH-03-WS-1215")
        self.assertEqual(slot_no1, 2)
        slot_no2 = self.parking.slot_number_for_registration_number("GJ-03-WS-1215")
        self.assertIsNone(slot_no2)
        test_name = "Car Slot Test -- Start -- "
        print(test_name.center(200, "*"))

    def tearDown(self):
        self.parking.slots = {}


if __name__ == "__main__":
    unittest.main()
