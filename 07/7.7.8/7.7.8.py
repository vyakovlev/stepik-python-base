"""
Великий подвиг 8. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и сохранить
в списке. Затем, выполнить сортировку этого списка по возрастанию с помощью алгоритма сортировки слиянием. Функция
должна возвращать новый отсортированный список.

Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде
последовательности чисел, записанных через пробел.

Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.

P. S. Теория сортировки в видео предыдущего шага.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.7.8

Sample Input:

8 11 -6 3 0 1 1
Sample Output:

-6 0 1 1 3 8 11

"""


def get_pairs(input_nums, output_nums=[]):
    input_len = len(input_nums)
    if input_len > 2:
        nums = (input_nums[:input_len // 2], input_nums[input_len // 2:])
        return get_pairs(nums[0]) + get_pairs(nums[1])
    else:
        output_nums.append(input_nums)
        return [input_nums]


def merge_pairs(pairs):
    # len_pairs = len(pairs)
    # nps = []
    # # if len_pairs == 1:
    # #     nps = sorted(pairs)
    # # else:
    # if len_pairs == 1:
    #     nps = sorted(pairs)
    # # elif len_pairs == 0:
    # #     return []
    # else:
    #     # max_length = 2 * (len_pairs // 2) if len_pairs > 1 else len_pairs
    #     max_len = len_pairs - 1 if len_pairs % 2 != 0 else len_pairs
    #     for i in range(0, max_len, 2):
    #         nps.append(sorted((*pairs[i], *pairs[i + 1])))
    #     nps[-1] = sorted((*nps[-1], *pairs[-1]))
    # len_nps = len(nps)
    # if len_nps < 4:
    #     if len_nps % 2 != 0:
    #         return merge_pairs(nps[1:len_nps])
    #     else:
    #         return merge_pairs(nps[:len_nps // 2:2]) + merge_pairs(nps[len_nps // 2::2])
    # elif len_nps == 2:
    #     return merge_pairs(nps[:len_nps])
    # else:
    #     return nps[0]
    # if len_pairs > 2:
    #     len_nps = len(nps)
    #     return [*merge_pairs(nps[:len_nps // 2]), *merge_pairs(nps[len_nps // 2:])]
    # elif len_pairs == 1:
    #     return sorted(*pairs)
    # else:
    #     sorted_pairs.append(pairs)
    #     return pairs
    # sorted_pairs = sorted([i for i in pairs])
    new_pairs = []
    for i in pairs:
        if isinstance(i, list):
            new_pairs += i
        else:
            new_pairs.append(i)

    return sorted(new_pairs)
    # while len_pairs := len(pairs) > 1:



# numbers = list(map(int, "5 3 3 6 8 5 3 -10 343 53 7".split()))
numbers = list(map(int, input().split()))
new_pairs = get_pairs(numbers)
merged = merge_pairs(new_pairs)
print(*merged)


