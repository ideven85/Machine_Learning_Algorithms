def max_subarray(nums):

    sum_so_far = 0
    max_ending_here = float("-inf")

    if all(nums) < 0:
        return max(nums)
    current_length = 0
    max_length = 0
    left = 0
    for num in nums:
        sum_so_far += num
        if max_ending_here < sum_so_far:
            max_ending_here = sum_so_far
        if sum_so_far < 0:
            sum_so_far = 0
    return max_ending_here


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = [-1, -2, -3, -4]
print(max_subarray(nums))
print(max_subarray(a))
