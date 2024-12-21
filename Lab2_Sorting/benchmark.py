import random
import time

class Benchmark:
    def __init__(self, function, max=900, step=50):
        self.function = function
        self.max = max
        self.step = step
        self.sorted_list = list(range(0, max))
        self.reversed_list = list(range(max, 0, -1))
        self.random_list = [random.randint(0, max) for x in range(max)]

    def __generate_arrays(self):
        count = 0
        arrays = dict()
        while count <= self.max:
            count += self.step
            sorted_list = list(range(0, count))
            rev_list = list(range(count, 0, -1))
            rand_list = [random.randint(0,self.max) for x in range(count)]
            arrays[f"{count}"] = {
                "sorted": sorted_list,
                "reversed": rev_list,
                "random": rand_list
            }
        return arrays
    
    def __calculate_time(self, data):
        start = time.perf_counter_ns()
        self.function(data, 0, len(data)-1)
        end = time.perf_counter_ns()

        return end - start
    
    def benchmark(self):
        all_arrays = self.__generate_arrays()
        lengths = all_arrays.keys()
        results = dict()
        for length in lengths:
            sorted = all_arrays[f"{length}"]["sorted"]
            rev = all_arrays[f"{length}"]["reversed"]
            rand = all_arrays[f"{length}"]["reversed"]
            results[f"{length}"] = {
                "sorted": self.__calculate_time(sorted),
                "reversed": self.__calculate_time(rev),
                "random": self.__calculate_time(rand)
            }
        return results