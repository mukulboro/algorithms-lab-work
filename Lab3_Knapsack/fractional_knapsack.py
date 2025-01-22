class FractionalKnapsack:
    def __init__(self, items:tuple, weights:tuple, capacity:float):
        self.items = items
        self.weights = weights
        self.capacity = capacity

        if not len(self.items) == len(self.weights):
            raise "Invalid configuration"

    def brute_force(self):
        n = len(self.items)
        items_with_ratio = [(self.items[i], self.weights[i], self.items[i]/self.weights[i], i) 
                           for i in range(n)]
        items_with_ratio.sort(key=lambda x: x[2], reverse=True)
        
        total_value = 0
        remaining_capacity = self.capacity
        config = ['0'] * n
        
        for value, weight, ratio, idx in items_with_ratio:
            if remaining_capacity >= weight:
                config[idx] = '1'
                total_value += value
                remaining_capacity -= weight
            else:
                fraction = remaining_capacity / weight
                config[idx] = str(fraction)
                total_value += value * fraction
                remaining_capacity = 0
                break
        
        return float(total_value), tuple(config)

    def greedy(self):
        n = len(self.items)
        items_with_ratio = [(self.items[i], self.weights[i], self.items[i]/self.weights[i], i) 
                           for i in range(n)]
        items_with_ratio.sort(key=lambda x: x[2], reverse=True)
        
        total_value = 0.0
        remaining_capacity = self.capacity
        config = ['0'] * n
        
        for value, weight, ratio, idx in items_with_ratio:
            if remaining_capacity >= weight:
                config[idx] = '1'
                total_value += value
                remaining_capacity -= weight
            else:
                fraction = remaining_capacity / weight
                config[idx] = str(fraction)
                total_value += value * fraction
                break
        
        return float(total_value), tuple(config)