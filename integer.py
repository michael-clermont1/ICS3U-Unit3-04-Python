#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a guessing game



def main():
    # this function shows formatting output

    # input
    integer = int(input("Enter an integer: "))

    # process & output
    print("")
    if integer > 0:
        print("{0} is a positive number.".format(integer))
    elif integer == 0:
        print("{0} is just zero.".format(integer))
    elif integer < 0:
        print("{0} is a negative number.".format(integer))

    print("\nDone.")


if __name__ == "__main__":
    main()
