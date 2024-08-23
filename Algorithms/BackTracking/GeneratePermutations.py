def generatePermutations(array):
    series = []

    def helper(array):
        if len(array) == 1:
            if array not in series:
                series.append(array)
            yield array

        for index, element in enumerate(array):
            remaining = array[:index] + array[index + 1 :]
            for permutations in helper(remaining):
                yield [element] + permutations

    return list(helper(array))


def getPermutations(array):
    # Write your code here.
    answer = []
    if len(array) == 1:
        return [array]
    for i in range(len(array)):
        for element in getPermutations(array[:i] + array[i + 1 :]):
            answer.append([array[i]] + element)
    return answer


class Solution:

    series = []

    def generatePermutations(self, arr):
        answer = []
        if len(arr) == 0:

            return [answer]
        else:
            for i in range(len(arr)):
                for element in self.generatePermutations(arr[i + 1 :] + arr[:i]):
                    answer.append([arr[i]] + element)
            return answer

    def uniquePerms(self, arr, n):
        arr = sorted(arr)
        # print(self.generatePermutations(arr))
        self.series = self.generatePermutations(arr)
        print(self.series)
        sorted(self.series)
        answer = []
        for e in self.series:
            if e not in answer:
                answer.append(e)

        return answer


print(generatePermutations([1, 2, 1]))
print(getPermutations([1, 2, 1]))
sol = Solution()
print(sol.uniquePerms([1, 2, 1], 3))
