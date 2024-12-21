from benchmark import Benchmark
from linear_search import linear_search
from binary_search import binary_search
from plot import plot_benchmark

if __name__ == "__main__":
    bm = Benchmark(max=2_00_000, step=200)
    linear_search_data = bm.benchmark(linear_search)
    binary_search_data = bm.benchmark(binary_search)
    plot_benchmark(title="Binary Search: Random Element", data=binary_search_data)
    plot_benchmark(title="Linear Search: Random Element", data=linear_search_data)