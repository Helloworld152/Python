# quick sort
def QuickSort(L, low, high):
    i = low
    j = highreturn L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[i] = L[j]
    L[i] = key
    QuickSort(L, low, i - 1)
    QuickSort(L, j + 1, high)
    return L