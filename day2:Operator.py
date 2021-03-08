#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip=((meal_cost *tip_percent)/100)
    tax=((meal_cost *tax_percent)/100)
    total=tip+tax+meal_cost
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)