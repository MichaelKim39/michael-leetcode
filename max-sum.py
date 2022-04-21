"""
Sliding Window Technique
"""


def max_sum(arr, window_size):
    if (len(arr) < window_size):
        return -1

    window_sum = sum([arr[i] for i in range(window_size)])
    max_sum = window_sum

    # Window can start upto point len - window, otherwise end-index out of bounds
    for i in range(len(arr) - window_size):
        window_sum = window_sum - arr[i] + arr[i + window_size]
        max_sum = max(window_sum, max_sum)

    return max_sum
