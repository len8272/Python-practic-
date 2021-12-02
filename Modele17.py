def sort_inserts(list_in):
    for i in range(1, len(list_in)):
        x = list_in[i]
        idx = i
        while idx > 0 and list_in[idx-1] > x:
            list_in[idx] = list_in[idx-1]
            idx -= 1
        list_in[idx] = x
    return list_in


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

number_string = input("Введите неповторяющиеся целые числа через пробел: ")
element1 = int(input("Введите одно число из указанных выше: "))

number_list = list(map(int, number_string.split()))

sequence_sorted = sort_inserts(number_list)
print("Сортировка списка по возрастанию в нем элементов: ", sequence_sorted)

# запускаем алгоритм на левой и правой границе
element_index = binary_search(sequence_sorted, element1, 0, len(sequence_sorted))
print("Индекс элемента в отсортированном списке: ", element_index)
