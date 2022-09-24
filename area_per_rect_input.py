#!/usr/bin/env python
# Copyright(c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Sept. 24, 2022
# calculates area and perimeter of rectangle with user input


def main():
    # variables with user input
    unit_of_measurement = input(
        "Please enter a unit of measurement (i.e, cm, mm, etc.): "
    )
    length = int(input("Enter length value: "))
    width = int(input("Enter width value: "))

    # area and perimeter calculations
    area = length * width
    perimeter = 2 * (length + width)

    # output results of area and perimeter with desired units of measurement
    print(f"Area = {area}{unit_of_measurement}^2")
    print(f"Perimeter = {perimeter}{unit_of_measurement}")


if __name__ == "__main__":
    main()
