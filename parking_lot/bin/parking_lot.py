import os
import sys
import parking

class VehicleParking(object):

    def __init__(self):
        # Parking inherites singleton so it will initiate once.
        self.parking = parking.Parking()

    def read_file(self, input_file="parking_lot file_inputs.txt"):
        file_path = os.path.join(os.getcwd(), input_file)
        if not os.path.exists(file_path):
            print("Given file %s does not exist" % file_path)
        file_obj = open(file_path)

        try:
            while True:
                line = file_obj.__next__()

                if line.endswith('\n'):
                    line = line.strip()

                if not line:
                    continue

                self.do_process(line)
        except StopIteration:
            pass
        except Exception as e:
            print("Error occured while processing file %s" % e)

        file_obj.close()

    def do_process(self, args):
        inputs = args.split()
        command = inputs[0]
        value = inputs[1:]
        if hasattr(self.parking, command):
            bound_method = getattr(self.parking, command)
            bound_method(*value)
        else:
            print("Sorry..!! I can not understand %s." % command)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        obj = VehicleParking()
        obj.read_file(args[1])
    else:
        obj = VehicleParking()
        obj.read_file()
