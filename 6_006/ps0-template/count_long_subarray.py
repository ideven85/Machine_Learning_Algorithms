def count_long_subarray(A):
    """
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    """
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    # prev,current,length = 0,0,0
    dp = [0 for _ in range(len(A))]
    dp[0] = 1
    for index in range(1, len(A)):
        if A[index] > A[index - 1]:
            dp[index] = 1 + dp[index - 1]
            # print(dp)
        else:
            dp[index] = 1

    maximum = max(dp)
    for el in dp:
        if el == maximum:
            count += 1

    # print(dp)
    return count


def count_long_subarray_memoised(A, index=0):
    """
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    """

    count = [0]
    ##################
    # YOUR CODE HERE #
    ##################
    # prev,current,length = 0,0,0
    length = 0
    if index == len(A) - 1:
        return len(count)
    if A[index + 1] > A[index]:
        length += 1

    return count
