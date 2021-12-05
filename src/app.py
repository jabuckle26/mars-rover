import os

from rover.input_reader import extract_file_data
from rover.rover import Rover

file_1: str = os.path.join(os.getcwd(), 'src', 'input', 'input1.txt')
file_2: str = os.path.join(os.getcwd(), 'src', 'input', 'input2.txt')

location_1, orientation_1, gridsize_1 = extract_file_data(file_1)
location_2, orientation_2, gridsize_2 = extract_file_data(file_2)


rover_1: Rover = Rover(location_1, orientation_1, gridsize_1)
rover_2: Rover = Rover(location_2, orientation_2, gridsize_2)
