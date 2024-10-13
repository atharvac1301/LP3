class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    finalValue = 0.0
    for item in arr:
        if item.weight <= W:
            finalValue += item.profit
            W -= item.weight
        else:
            finalValue += (W / item.weight) * item.profit
            W = 0
            return finalValue
    
    return finalValue
    

W = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

max_val = fractKnapsack(W, arr)
print(max_val)

