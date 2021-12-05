import os
from typing import List

def extract_file_data(file_path: str):
    with open(file_path) as f:
        grid_size = parse_grid(f.readline())
        location_info: list[str] = parse_start_position_and_orientation(f.readline())
        location: List[int] = [int(x) for x in location_info[:2]]
        orientation: str = location_info[-1]
        commands: List[str] = [command for command in list(f.readline())]
        f.close()
    return grid_size, location, orientation, commands

def parse_grid(grid_line: str) -> int:
    return grid_line[0]


def parse_start_position_and_orientation(location_info: list[str]):
    return location_info.strip().split(' ')
