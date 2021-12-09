from src.navigation.location import Location
from src.rover.collision_detector import CollisionDetector

grid_size = 10


def test_can_check_if_not_facing_border_while_at_border():
    location: Location = Location(1, 1)
    orientation: str = 'E'
    detector: CollisionDetector = CollisionDetector(grid_size)

    assert detector.will_collide_with_border(location, orientation) == False


def test_can_identify_collision_with_northern_border():
    location: Location = Location(1, grid_size)
    orientation: str = 'N'
    detector: CollisionDetector = CollisionDetector(grid_size)

    assert detector.will_collide_with_border(location, orientation)


def test_western_border_identified():
    location: Location = Location(0, 2)
    orientation: str = 'W'
    detector: CollisionDetector = CollisionDetector(grid_size)

    assert detector.will_collide_with_border(location, orientation)


def test_southern_border_identified():
    location: Location = Location(2, 0)
    orientation: str = 'S'
    detector: CollisionDetector = CollisionDetector(grid_size)

    assert detector.will_collide_with_border(location, orientation)


def test_eastern_border_identified():
    location: Location = Location(grid_size, 2)
    orientation: str = 'E'
    detector: CollisionDetector = CollisionDetector(grid_size)

    assert detector.will_collide_with_border(location, orientation)