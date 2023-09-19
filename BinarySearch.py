def binary_search(array, begin_index, end_index, key, step):
    if array[end_index] == key:
        return step
    if begin_index > end_index:
        return -1
    middle = (begin_index + end_index) // 2
    if array[middle] == key:
        return step
    elif array[middle] < key:
        return binary_search(array, middle + 1, end_index, key, step + 1)
    else:
        return binary_search(array, begin_index, middle - 1, key, step + 1)

size = int(input("Введите размер массива: "))
array = [a + 1 for a in range(size)]
#можно задать или ввести массив вручную
#array = [1, 2, 3, 4, 19, 30, 31, 33]
key = int(input("Введите искомый элемент: "))
print(binary_search(array, 0, len(array)  - 1, key, 1))
