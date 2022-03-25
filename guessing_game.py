#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a guessing game

import constants


def main():
    # this function shows formatting output

    # input
    number_from_user = int(input("Enter a number between 0-9: "))

    # process & output
    print("")
    if number_from_user == constants.number:
        print("You guessed correctly!")
    if number_from_user != constants.number:
        print("You guessed incorrectly :(")

    print("\nDone.")


if __name__ == "__main__":
    main()
