# Parking Lot using Python 3

One of the most popular problem statement solved with Python. Written in Python 3 without using any external library.
Code structure is object oriented.

## Problem
- Create *n* car parking slots. 
- Slots are starting from 1.
- On entering the car, record colour and registration number
- Allot the slot number near to the entry point
- On leaving, deallocate the slot
- Now, Car should be indetifying through registration number / colour


## Solution
- **Not required to install/setup to execute the script**
- takes a input txt file and expecting commands
- commands are fixed and list of commands are:
	- create_parking_lot
	- park
	- status
	- leave
	- registration_numbers_for_cars_with_colour
	- slot_numbers_for_cars_with_colour
	- slot_number_for_registration_number
- Initially  **Singleton** concept was introduced for Parking class. So Parking class can not be initiate multiple times. (Note: later I removed inheritance of singleton by considering it may break your test cases.)

## Run the script
```sh 
$ ./bin/parking_lot
```

- It will looking for input file where the commands are written. If the file location is different, you can provide the absolute path of txt file.

####  Input file (e.g. /bin/parking_lot file_inputs.txt)

| Input File |
| ------ |
| create_parking_lot 6 |
| park KA-01-HH-1234 White |
| park KA-01-HH-9999 White |
| park KA-01-BB-0001 Black |
| park KA-01-HH-7777 Red |
| park KA-01-HH-2701 Blue |
| park KA-01-HH-3141 Black |
| leave 4 |
| status |
| park KA-01-P-333 White |
| park DL-12-AA-9999 White |
| registration_numbers_for_cars_with_colour White |
| slot_numbers_for_cars_with_colour White |
| slot_number_for_registration_number KA-01-HH-3141 |
| slot_number_for_registration_number MH-04-AY-1111 |


#### Output for the above example command
```sh
Created a parking lot with 6 slots
Allocated slot number: 1
Allocated slot number: 2
Allocated slot number: 3
Allocated slot number: 4
Allocated slot number: 5
Allocated slot number: 6
Slot number 4 is free
Slot No	Registration No	Colour
1	KA-01-HH-1234	White
2	ka-01-HH-9999	White
3	KA-01-BB-0001	Black
5	KA-01-HH-2701	Blue
6	KA-01-HH-3141	Black
Allocated slot number: 4
Sorry, parking lot is full
KA-01-HH-1234, ka-01-HH-9999, KA-01-P-333
1, 2, 4
6
Not found
```



--------------------------------------------------------------------------------------END--------------------------------------------------------------------------------------
