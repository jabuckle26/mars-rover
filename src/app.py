import os

from rover.input_reader import extract_file_data
from rover.rover import Rover

file_1: str = os.path.join(os.getcwd(), 'src', 'input', 'input1.txt')
file_2: str = os.path.join(os.getcwd(), 'src', 'input', 'input2.txt')

gridsize_1, location_1, orientation_1, commands1 = extract_file_data(file_1)
gridsize_2, location_2, orientation_2, commands2 = extract_file_data(file_2)


rover_1: Rover = Rover(int(gridsize_1), location_1, orientation_1)
rover_2: Rover = Rover(int(gridsize_2), location_2, orientation_2)

print(commands1)
for command in commands1:
    rover_1.navigate(command)
print(rover_1.orientation)
print(rover_1.location)

print(commands2)
for command in commands2:
    rover_2.navigate(command)
print(rover_2.orientation)
print(rover_2.location)
