import timeit
import DZ
import random
from item import Item
from Backpack import Backpack
from util import powers_of

def make_header(func_names):
    return " ".join(["{0:<12}".format(s) for s in ["N"] + func_names])

def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])

def time_us(ns):
    """Prints time table for given functions and inputs.
    functions - dictionary of {func name: func(input)} - functions to time,
    ns - list of n for which generate input,
    generator - func(n) - input generation function,
    repeats - number of times to call functions for each given input."""
    print(make_header(['standart', 'greedy_algorithm']))

    for n in ns:
        list_of_items = [Item("item " + str(i), random.randint(1, 100), random.randint(1, 100)) for i in range(10**n)]
        W = [list_of_items[i].weight for i in range(10**n)]
        P = [list_of_items[i].price for i in range(10**n)]
        bp = Backpack(10000)
        times = []
        timer = timeit.Timer(lambda: DZ.standart(W, P, bp, list_of_items))
        times.append(timer.timeit(1))
        timer = timeit.Timer(lambda: DZ.greedy(list_of_items, bp))
        times.append(timer.timeit(1))
        print(make_line(n, times))



if __name__ == "__main__":
    time_us(powers_of(1, 0 , 5))




