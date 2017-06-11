import timeit
from graph import Graph
from generate import main
from util import powers_of
def make_header(func_names):
    return " ".join(["{0:<12}".format(s) for s in ["N"]+ func_names])


def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])


def time_us(ns, generator):
    generator()
    print(make_header(['Krascal algorithm']))
    G=Graph()
    for n in ns:
        G = G.input_Graph("records_1e{0}.txt".format(n))
        times = []
        timer = timeit.Timer(lambda: G.krascal_alg())
        times.append(timer.timeit(1))
        print(make_line(10 ** (n - 1), times))

if __name__ == "__main__":
    time_us(ns=powers_of(1, 0, 5), generator=main)