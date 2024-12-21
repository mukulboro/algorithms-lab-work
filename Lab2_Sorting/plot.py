from matplotlib import pyplot as plt

def plot_benchmark_results(results:dict, sorting_name:str):
    lengths = results.keys()
    random_times = []
    reversed_times = []
    sorted_times = []
    for length in lengths:
        random_times.append(results[f"{length}"]["random"])
        reversed_times.append(results[f"{length}"]["reversed"])
        sorted_times.append(results[f"{length}"]["sorted"])
    lengths = [int(x) for x in lengths]

    # Plot sorted
    plt.title(f"{sorting_name}: Sorted List")
    plt.plot(lengths, sorted_times, 'r')
    plt.savefig(f"{sorting_name}SORTEDLIST.png")
    plt.clf()

    # Plot Random
    plt.title(f"{sorting_name}: Random List")
    plt.xlabel("Number of array elements")
    plt.ylabel("Time taken (ns)")
    plt.plot(lengths, random_times, 'r')
    plt.savefig(f"{sorting_name}RANDLIST.png")
    plt.clf()

    # Plot reversed
    plt.title(f"{sorting_name}: Reversed List")
    plt.plot(lengths, reversed_times, 'r')
    plt.savefig(f"{sorting_name}REVLIST.png")
    plt.clf()
