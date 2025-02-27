"""Starter Code for Milk Tea CC Problem"""


# Complete the count_complaints function
def count_complaints(preferences, forbiddens):
    complaints = 0
    min_complaints = 0
    # TODO: Add logic to count the number of complaints
    p = [[0 for _ in range(num_friends)] for _ in range(num_options)]
    j = 0
    for e in preferences:

        for i in range(len(e)):
            p[j].append(int(e[i]))
        j += 1

    print(p)

    possibilities = [[0 for _ in range(num_options)] for _ in range(num_friends)]
    # TODO: Generate possibilities in increasing order of number of complaints
    for i in range(num_options):
        for j in range(num_friends):

            possibilities[i][j] = 1 if sum(p[i]) > num_friends - sum(p[i]) else 0

        if possibilities[i] not in forbiddens:
            complaints = sum(possibilities[i])
            if min_complaints <= complaints:
                min_complaints = complaints

    return min_complaints


if __name__ == "__main__":
    # Read number of test cases
    num_cases = int(input())

    for tc in range(1, num_cases + 1):
        # Read number of friends, number of forbidden teas, and number of options
        num_friends, num_forbidden, num_options = map(int, input().split())

        # Read the friends' preferences
        preferences = [input() for _ in range(num_friends)]

        # Read the forbidden teas
        forbiddens = [input() for _ in range(num_forbidden)]

        print("Case #%d: %d" % (tc, count_complaints(preferences, forbiddens)))
