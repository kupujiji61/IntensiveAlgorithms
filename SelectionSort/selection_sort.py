from typing import List


from typing import List


def selection_sort(array: List[int]) -> List[int]:
    n = len(array)
    
    for i in range(0, n - 1):
        current_minimum = i + 1
        for j in range(i + 1, n):
            if array[j] < array[current_minimum]:
                current_minimum = j
        if current_minimum < array[i]:
            array[i], array[current_minimum] = array[current_minimum], array[i]
    
    return array
            

# https://leetcode.com/problems/sort-colors/


# https://leetcode.com/problems/sort-colors/
