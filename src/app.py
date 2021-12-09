import os

from src.input.input_reader import extract_file_data
from src.rover.rover import Rover

file_1: str = os.path.join(os.getcwd(), 'input', 'input1.txt')
file_2: str = os.path.join(os.getcwd(), 'input', 'input2.txt')

grid_size_1, location_1, orientation_1, commands1 = extract_file_data(file_1)
grid_size_2, location_2, orientation_2, commands2 = extract_file_data(file_2)


rover_1: Rover = Rover(int(grid_size_1), location_1, orientation_1)
rover_2: Rover = Rover(int(grid_size_2), location_2, orientation_2)

print(commands1)
for command in commands1:
    rover_1.navigate(command)
print(rover_1.orientation)
print(rover_1.location.coordinate())

print(commands2)
for command in commands2:
    rover_2.navigate(command)
print(rover_2.orientation)
print(rover_2.location.coordinate())
