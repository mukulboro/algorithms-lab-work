from quick_sort import quicksort
from merge_sort import merge_sort
from benchmark import Benchmark
from plot import plot_benchmark_results
import sys

sys.setrecursionlimit(2000)


if __name__ == "__main__":
    qs_bm = Benchmark(function=quicksort, max=990, step=5)
    ms_bm = Benchmark(function=merge_sort, max=1990, step=5)

    qs_results = qs_bm.benchmark()

    ms_results = ms_bm.benchmark()
    plot_benchmark_results(results=ms_results, sorting_name="Merge Sort")
    plot_benchmark_results(results=qs_results, sorting_name="Quick Sort")