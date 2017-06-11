from DZ import insertion_sort, bucket_sort
from timer import time_us
from util import powers_of
from generate import main

if __name__ == "__main__":
    time_us({
        "Std": sorted,
        "insertion_sort": insertion_sort,
        "bucket_sort": bucket_sort

    }, ns=powers_of(1, 0, 5), generator=main, repeats=1)