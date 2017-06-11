import random


def powers_of(num, min_power, max_power):
    """Returns list of powers of number 'num', from 'min_power' to 'max_power'"""
    return [num+p for p in range(min_power, max_power + 1)]
