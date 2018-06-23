def bubbleSort(a):
    for times in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

print (bubbleSort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
