import sys


class City:
    """ Represents a city in an input file.

    Properties:
        grid (int, int): (number of rows, number of columns)
        vehicles_num: number of vehicles
        ride_num: number of rides
        bonus: per-ride bonus for starting ride on time
        step_num: number of steps in the simulation
    """
    def __init__(self, grid, vehicles_num, ride_num, bonus, step_num):
        self.grid = grid
        self.vehicles_num = vehicles_num
        self.ride_num = ride_num
        self.bonus = bonus
        self.step_num = step_num


class Ride:
    """ Represents a requested ride in the input file.

    Properties:
        start_intersection (int, int): (row, column)
        finish_intersection (int, int): (row, column)
        earliest_start: earliest time ride may start
        latest_finish: earliest time ride may finish

    """
    def __init__(self, start_intersection, finish_intersection,
                 earliest_start, latest_finish):
        self.start_intersection = start_intersection
        self.finish_intersection = finish_intersection
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish


def generate_city(file):
    """ Returns a City object given an input file.
    """
    return


def generated_rides_list(file):
    """ Returns a list of Ride objects.
    """
    return
