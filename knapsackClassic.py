from item import Item

def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        value = val[n-1]
        knapSackWithout = knapSack(W - wt[n - 1], wt, val, n - 1)
        fullKnapSack = knapSack(W, wt, val, n - 1)
        return max(value + knapSackWithout, fullKnapSack)

    # end of function knapSack



def run(items, capacity):
    val = []
    wt = []
    for item in items:
        val.append(item.value)
        wt.append(item.weight)
    n = len(val)
    return knapSack(capacity, wt, val, n)


