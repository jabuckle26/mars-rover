from src.rover import Rover


def test_first_test():
    assert True

def test_can_create_rover():
    location = [0,0]
    rover = Rover(location)
    assert rover.location == location


