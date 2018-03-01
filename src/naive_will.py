"""
"""

import sys
import base_will as base

# Global vars
CITY = None
OUTPUT = None


def order_waiting_rides(waiting_rides):
    """ Sorts waiting rides, in-place, by their earliest start time.
    """
    waiting_rides.sort(key=lambda r: r.latest_finish)


def assign_vehicle_to_ride(ride, free_vehicles):
    """ Returns Vehicle object which is closest to ride in distance.
    """
    free_vehicles.sort(key=lambda v: base.get_distance_between_points(
        v.current_position, ride.start_intersection))
    return free_vehicles[0]


def assign_rides(free_vehicles, waiting_rides):
    """ Returns a list of tuples; where the first item is a Vehicle and the
    second item is a Ride.
    """
    assignments = []
    order_waiting_rides(waiting_rides)
    for ride in waiting_rides:
        if (len(free_vehicles) == 0):
            break
        v = assign_vehicle_to_ride(ride, free_vehicles)
        assignments.append((v, ride))
        free_vehicles.remove(v)
        v.step_busy_until += base.get_distance_between_points(
            v.current_position, ride.start_intersection) + ride.distance
        print('Vehicle', v.id, 'is now busy until step', v.step_busy_until)
        ride.is_taken = True
        OUTPUT[v.id].append(ride.id)
    return assignments


def output_file(file):
    filename = file[6:-3]
    contents = ''
    for item in OUTPUT:
        line = str(len(item))
        for a in item:
            line += ' ' + str(a)
        contents += line + '\n'
    with open('output/' + filename + '.out', 'w') as f:
        f.write(contents)


def main(file):
    global CITY
    global OUTPUT
    CITY = base.City(file)
    OUTPUT = [[] for v in CITY.vehicles]
    print('THIS CITY IS:')
    print('---')
    print(CITY)
    print('---')
    for step in range(0, CITY.step_num):
        print('\nSTEP', step, 'BEGIN')
        free_vehicles = CITY.get_free_vehicles(step)
        waiting_rides = CITY.get_waiting_rides()
        if (len(free_vehicles) > 0 and len(waiting_rides) > 0):
            assignments_to_make = assign_rides(free_vehicles, waiting_rides)
            print('Assignments made this step:')
            for a in assignments_to_make:
                print('(' + str(a[0].id) + ', ' + str(a[1].id) + ')')
    output_file(file)


if (__name__ == '__main__'):
    if (len(sys.argv) == 2):
        main(sys.argv[1])
    else:
        print('Invalid arguments.')
