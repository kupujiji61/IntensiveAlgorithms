from typing import List

def bubble_sort(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(n):
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


# https://leetcode.com/problems/sort-colors/description/
