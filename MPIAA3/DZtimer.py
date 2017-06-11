from bstree import BSTree
from timer import time_us
from util import shuffled_ints, random_ints, powers_of
import DZ
from generate import main

if __name__ == "__main__":
    time_us({
        "CreateTree": DZ.CreateTree,
        "Search": DZ.AVLTree.TreeSearch,
    }, ns=powers_of(10, 0, 5), generator=main, repeats=10)