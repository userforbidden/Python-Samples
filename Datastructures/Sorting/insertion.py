from random import randint
from typing import List
def sort_list(unsorted_list: List[int]) -> List[int]:
    print(','.join(map(str,unsorted_list)))
    for i, entry in enumerate(unsorted_list):
        current = i 
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current-1] = unsorted_list[current-1], unsorted_list[current]
            current -= 1

    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [randint(1,99) for _ in range(10)]
    res = sort_list(unsorted_list)
    print(','.join(map(str,res)))
