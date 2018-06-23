def quickSort(x):
    if not x or len(x) <= 1: return x
    else:
        pivot = x[0]
        low = [i for i in x[1:] if i <= pivot]
        high = [i for i in x[1:] if i > pivot]
    return quickSort(low) + [pivot] + quickSort(high)



print(quickSort([6,5,4,8,3,5,6,7,8]))
