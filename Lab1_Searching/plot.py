import matplotlib.pyplot as plt

def plot_benchmark(title:str, data:dict):
    keys = data.keys()
    values = [data[x] for x in keys]
    keys = [int(x) for x in keys]

    plt.title(title)
    plt.plot(keys, values, "r")
    # plt.axis((0,200000, 0, 500))
    plt.xlabel("Number of array elements")
    plt.ylabel("Time Taken (nano seconds)")
    plt.savefig(f"{title}.png")
    plt.clf()