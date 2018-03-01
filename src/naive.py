"""
"""

import sys
import handle_files


def main(file):
    city = handle_files.City(file)
    print(city)


if (__name__ == '__main__'):
    if (len(sys.argv) == 2):
        main(sys.argv[1])
    else:
        print('Invalid arguments.')
