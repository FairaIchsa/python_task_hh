# Найти индекс первого нуля
def find_zero(array):    # в задании сказано найти индекс первого нуля, а в примере находится индекс последней единицы
    left = 0; right = len(array)-1
    if array[right] == '1':
        return -1   # решение отсутствует
    if array[left] == '0':
        return 0
    while right - left > 1:
        mid = left + (right-left) // 2
        if array[mid] == '0':
            right = mid
        else:
            left = mid
    return right


print(find_zero("111111111110000000000000000"))
