def selection_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        minIndex = i
        min = arr[i]
        for j in range(i+1, l):
            if arr[j] < min:
                min = arr[j]
                minIndex = j
        temp = arr[i]
        arr[i] = min
        arr[minIndex] = temp


arr = [4,2,3,4,5,7,56]
selection_sort(arr)
print(arr)
