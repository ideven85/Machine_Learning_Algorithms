def generatePermutations(array):

    def helper(array):
        if len(array)==1:
            yield array

        for index,element in enumerate(array):
            remaining = array[:index]+array[index+1:]
            for permutations in helper(remaining):
                yield [element]+permutations
    return list(helper(array))
def getPermutations(array):
    # Write your code here.
    answer = []
    if len(array)==1:
        return [array]
    for i in range(len(array)):
        for element in getPermutations(array[:i]+array[i+1:]):
            answer.append([array[i]]+element)
    return answer


print(generatePermutations([1,2,3]))
print(getPermutations([1,2,3]))