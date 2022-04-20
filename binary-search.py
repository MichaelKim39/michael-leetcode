from typing import list


def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1

    while(right >= left):
        mid = left+right // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        elif arr[mid] < target:
            left = mid+1
