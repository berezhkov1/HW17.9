def binary_search(array, element, left, right):
   # if left > right:  # если левая граница превысила правую,
    #    return print("Введенный элемент не входит в рамки списка")  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] < element <= array[middle+1]:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
def sort(text):
    a = True
    while a:
        a = False
        for i in range(len(text) - 1):
            if text[i] > text[i + 1]:
               text[i], text[i + 1] = text[i + 1], text[i]
               a = True

string = input("Введите числа через пробел:")
x = int(input("Введите число:"))


list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

sort(list_of_numbers)
print("Упорядоченный список введенных чисел:", list_of_numbers)
if(list_of_numbers[0]<x<list_of_numbers[-1]):
    print("Установленный индекс элемента:", binary_search(list_of_numbers, x, 0, len(list_of_numbers)-1))
elif (x == list_of_numbers[0] or x == list_of_numbers[len(list_of_numbers)-1]):
    print("Ошибка. Введенное число является границей введенного списка")
else:
   print("Ошибка. Введенное число не входит в рамки введенного списка")
