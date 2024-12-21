import time
from random import choice

class Benchmark:
    def __init__(self, max=100_000, step=1000):
        self.max = max
        self.step = step
        self.arrays = self.generate_arrays()

    def generate_arrays(self):
        arrays = dict()
        current_count = 0
        while current_count < self.max:
            current_count += self.step
            arrays[f"{current_count}"] = list(range(0, current_count))
        return arrays
    
    def benchmark(self, function):
        data = dict()
        for i, key in enumerate(self.arrays):
            arr = self.arrays[key]
            # mid = (len(arr) - 1)//2
            # to_find = arr[0]
            to_find = choice(arr)
            start = time.perf_counter_ns()
            result = function(arr, to_find)
            end = time.perf_counter_ns()
            time_taken = end-start
            data[key] = time_taken
        return data
