"""
"""

import sys
import base


def main(file):
    city = base.City(file)
    print(city)


if (__name__ == '__main__'):
    if (len(sys.argv) == 2):
        main(sys.argv[1])
    else:
        print('Invalid arguments.')
