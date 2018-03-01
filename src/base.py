"""
"""


# Classes

class City:
    """ Represents a city in an input file.

    Properties:
        grid (int, int): (number of rows, number of columns)
        vehicles (list of Vehicle): list of all available vehicles
        rides (list of Ride): list of all rides
        ride_num: number of rides
        bonus: per-ride bonus for starting ride on time
        step_num: number of steps in the simulation
    """
    def __init__(self, file):
        with open(file) as f:
            line = f.readline()
            values = line.strip('\n').split(' ')
        self.grid = (int(values[0]), int(values[1]))
        self.ride_num = int(values[3])
        self.bonus = int(values[4])
        self.step_num = int(values[5])
        self.vehicles = self.get_vehicles(int(values[2]))
        self.rides = self.get_rides(file)

    def __repr__(self):
        return ('grid: ' + str(self.grid) +
                '\nnumber of vehicles: ' + str(len(self.vehicles)) +
                '\nnumber of rides: ' + str(self.ride_num) +
                '\nper-ride bonus: ' + str(self.bonus) +
                '\nnumber of steps: ' + str(self.step_num)
                )

    def get_rides(self, file):
        rides = []
        with open(file) as f:
            next(f)
            cur_ride = 0
            for line in f:
                values = line.split(' ')
                values[-1] = values[-1][-2]
                r = Ride(cur_ride,
                         (int(values[0]), int(values[1])),
                         (int(values[2]), int(values[3])),
                         int(values[4]),
                         int(values[5])
                         )
                rides.append(r)
                cur_ride += 1
        return rides

    def get_vehicles(self, n):
        vehicles = []
        for i in range(0, n):
            vehicles.append(Vehicle(i))
        return vehicles

    def get_free_vehicles(self, current_step):
        free = []
        for v in self.vehicles:
            if (v.step_busy_until <= current_step):
                free.append(v)
        return free

    def get_waiting_rides(self):
        waiting = []
        for r in self.rides:
            if (not r.is_taken):
                waiting.append(r)
        return waiting


class Ride:
    """ Represents a requested ride in the input file.

    Properties:
        start_intersection (int, int): (row, column)
        finish_intersection (int, int): (row, column)
        earliest_start (int): earliest time ride may start
        latest_finish (int): earliest time ride may finish
        is_taken (boolean): false if the journey has not yet been taken, true
            otherwise

    """
    def __init__(self, r_id, start_intersection, finish_intersection,
                 earliest_start, latest_finish):
        self.id = r_id
        self.start_intersection = start_intersection
        self.finish_intersection = finish_intersection
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.distance = get_distance_between_points(start_intersection,
                                                    finish_intersection)
        self.is_taken = False

    def __repr__(self):
        return ('id: ' + str(self.id) +
                '\nstart intersection: ' + str(self.start_intersection) +
                '\nfinish intersection: ' + str(self.finish_intersection) +
                '\nearliest start: ' + str(self.earliest_start) +
                '\nlatest finish: ' + str(self.latest_finish) +
                '\ndistance: ' + str(self.distance) +
                '\nhas been taken: ' + str(self.is_taken)
                )


class Vehicle:
    """ Represents a vehicle in the input file.

    Properties:
        current_position (int, int): current postion of the vehicle
        ride (Ride): ride object assigned to this vehicle
    """
    def __init__(self, v_id):
        self.id = v_id
        self.current_position = (0, 0)
        self.ride = None
        self.step_busy_until = 0

    def __repr__(self):
        return ('[' + str(self.id) + ', ' + str(self.current_position) +
                ', ' + str(self.ride) + ']'
                )


# Functions

def get_distance_between_points(pos1, pos2):
    return (
        abs(pos1[0] - pos2[0]) +
        abs(pos1[1] - pos2[1])
    )


def create_matrix(r, c):
    road_matrix = []
    for i in range(0, r):
        road_matrix.append([0 for i in range(0, c)])
    return road_matrix


def print_file_info(file):
    city = City(file)
    print(city)

    print('\n---\n')

    for r in city.rides:
        print(r, '\n')
