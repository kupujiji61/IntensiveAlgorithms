from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(1, n):
        while i > 0:
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array


# https://leetcode.com/problems/sort-colors/
