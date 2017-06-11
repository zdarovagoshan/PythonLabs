import DZ
from timer import time_us
from util import powers_of
from generate import read_file, generate_records, main

names = read_file("names.txt")
surnames = read_file("surnames.txt")

if __name__ == "__main__":
    """find(file1)"""
    time_us({
        "Find": DZ.find,
    }, ns=powers_of(1, 0, 5), generator=main, repeats=10)