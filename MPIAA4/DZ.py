import timeit
from graph import Graph
from generate import main
from util import powers_of
def make_header(func_names):
    return " ".join(["{0:<12}".format(s) for s in func_names])


def make_line(times):
    return " ".join(["{0:<12.5f}".format(t) for t in times])


def time_us():
    print(make_header(['Krascal algorithm']))
    G=Graph()
    G = G.input_Graph("v12.txt")
    times = []
    timer = timeit.Timer(lambda: G.krascal_alg())
    times.append(timer.timeit(1))
    print(make_line(times))

if __name__ == "__main__":
    G=Graph()
    G=G.input_Graph("v12.txt")
    h=G.krascal_alg()
    print(G.get_weight())
