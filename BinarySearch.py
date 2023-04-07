import math


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    mid = math.ceil((low + high) / 2)

    # 首先判断low与high值大小
    if len(list) == 1 or 2:
        if len(list) == 1:
            if list[low] == item:
                print("查找到了，数值位于数组首位")
                return low
            else:
                print("未查找到！")
                return None
        if len(list) == 2:
            if list[low] == item:
                print("查找到了，数值位于数组首位")
                return low
            if list[high] == item:
                print("查找到了，数值位于数组末位")
                return high
            else:
                return None
    if len(list) > 2:  # 考虑使用do-while语句；
        while item != list[mid]:
            mid = (low + high) // 2
            if item > list[mid]:
                low = mid + 1
                # mid = math.ceil((low + high) / 2)

            if item < list[mid]:
                high = mid - 1
                # mid = math.ceil((low + high) / 2)
        return mid


def binary_search_iterative(elements, value):

    left, right = 0, len(elements)-1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return middle
        elif elements[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return None


if __name__ == '__main__':
    list_test = [1, 2, 3, 4, 5, 6]
    result = binary_search(list=list_test, item=2)
    print("******------------------******")
    print("结果为", result)
    test = binary_search_iterative(list_test, 2)
    print(test)
    # a, b = 1, 2
    # mid = (a+b) // 2
    # print(mid)
