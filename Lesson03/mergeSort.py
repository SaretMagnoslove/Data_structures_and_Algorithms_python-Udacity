def mergeSort(x):

    if len(x) < 2: return x

    result, mid = [], int(len(x)/2)

    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])

    while len(y) > 0 and len(z) > 0:
        if y[0] > z[0]: result.append(z.pop(0))
        else: result.append(y.pop(0))
        
    result.extend(y+z)
    return result

print(mergeSort([21,4,1,3,9,20,25]))