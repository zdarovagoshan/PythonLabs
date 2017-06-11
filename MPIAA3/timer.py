import timeit
import DZ
from generate import read_file
from generate import main
from util import shuffled_ints, random_ints, powers_of

def make_header(func_names):
    return " ".join(["{0:<12}".format(s) for s in ["N"] + func_names])


def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])


def time_us(ns, generator, repeats=int(1e6)):
    """Prints time table for given functions and inputs.
    functions - dictionary of {func name: func(input)} - functions to time,
    ns - list of n for which generate input,
    generator - func(n) - input generation function,
    repeats - number of times to call functions for each given input."""
    generator()
    print(make_header(['TreeSearch']))
    for n in ns:
        data = read_file("records_1e{0}.txt".format(n))
        data_surnames= read_file("records_2e{0}.txt".format(n))
        times = []
        a=DZ.CreateTree(data)
        timer = timeit.Timer(lambda: a.TreeSearch(data_surnames))
        times.append(timer.timeit(repeats))
        print(make_line(10**(n-1), times))



if __name__ == "__main__":
    time_us(ns=powers_of(1, 0, 5), generator=main, repeats=10)




