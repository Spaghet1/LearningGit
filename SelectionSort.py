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


if __name__ == '__main__':
    arr = []
    while True:
        try:
            num = int(input("Enter an integer (else to quit): "))
            arr.append(num)
            print(f"Current array: {arr}\n")
        except ValueError:
            print(f"Final array: {arr}\n")
            break
    selection_sort(arr)
    print(f"Sorted array: {arr}")


