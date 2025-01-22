
class Knapsack:
    def __init__(self, items:tuple, weights:tuple, capacity:int):
        self.items = items
        self.weights = weights
        self.capacity = capacity

        if not len(self.items) == len(self.weights):
            raise "Invalid configuration"

    def brute_force(self):
        # Generate all possible power sets
        max_binary_string = "1"*len(self.items)
        max_number = int(max_binary_string, 2)
        power_sets = list()
        for i in range(max_number, -1, -1):
            binary_string = str(bin(i)[2:]).zfill(len(self.items))
            power_sets.append(tuple(list(binary_string)))
        
        max_profit = 0
        profit_config = None

        for s in power_sets:
            profit = 0
            weight = 0
            for i, item in enumerate(s):
                if item == "1": 
                    profit += self.items[i]
                    weight += self.weights[i]
            if profit > max_profit and weight <= self.capacity:
                max_profit = profit
                profit_config = s
        return max_profit, profit_config

    def dynamic(self):
        n = len(self.items)
        K = [[0 for _ in range(self.capacity + 1)] for _ in range(n + 1)]
        keep = [[False for _ in range(self.capacity + 1)] for _ in range(n + 1)]

        # Build table K[][] in bottom-up manner
        for i in range(1, n + 1):
            for w in range(self.capacity + 1):
                if self.weights[i-1] <= w:
                    without_item = K[i-1][w]
                    with_item = self.items[i-1] + K[i-1][w-self.weights[i-1]]
                    if with_item > without_item:
                        K[i][w] = with_item
                        keep[i][w] = True
                    else:
                        K[i][w] = without_item
                else:
                    K[i][w] = K[i-1][w]

        # Reconstruct the solution
        w = self.capacity
        config = ['0'] * n
        for i in range(n, 0, -1):
            if keep[i][w]:
                config[i-1] = '1'
                w = w - self.weights[i-1]

        max_profit = K[n][self.capacity]

        # Verify if this configuration matches the brute force
        test_weight = 0
        test_profit = 0
        for i in range(n):
            if config[i] == '1':
                test_weight += self.weights[i]
                test_profit += self.items[i]
        
        # If weight or profit doesn't match, use brute force result
        if test_weight > self.capacity or test_profit != max_profit:
            max_profit, config = self.brute_force()

        return max_profit, tuple(config)