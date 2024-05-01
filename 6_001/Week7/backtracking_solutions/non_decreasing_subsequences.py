from collections import deque


def increasing_subsequences(arr):
    def dfs(last, current=None, start=0):

        if current is None:
            current = list()
        if len(current) >= 2:
            output.append(current[:])

        for i in range(start, len(arr)):
            # print(i,end=' ')
            if not current or arr[i] >= current[-1]:
                # print(current)
                current.append(arr[i])
                dfs(last, current, i + 1)
                current.pop()

    output = []
    dfs(len(arr))
    return output



if __name__ == "__main__":
    nums = [2, 4, 5, 4]

    result = increasing_subsequences(nums)
    print(result)
#
# if __name__ == "__main__":
#     inp = [2, 4, 5, 4]
#     print(increasing_subsequences(inp))
#
#
# """
# Input: [2, 4, 5, 4]
# Output: [[2, 4, 5], [2, 5], [2, 4], [4, 5]]
# """
