def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(val, arr):
    first = 0
    last = len(arr) - 1
    result_ok = False
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == val:
            result_ok = True
            pos = middle
            break
        elif arr[middle] < val:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print("Элемент найден:", pos)
    else:
        print("Элемент не найден")


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Неотсортированный список:", unsorted_list)


sorted_list = bubble_sort(unsorted_list)
# sorted_list = selection_sort(unsorted_list)

print("Отсортированный список:", sorted_list)

search_value = 22
binary_search(search_value, sorted_list)
