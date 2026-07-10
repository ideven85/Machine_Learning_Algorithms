
def edit_distance(str1, str2):
    # Write your code here
    """
    Edit Distance between two words
    """
    s1 = len(str1)
    s2 = len(str2)
    matrix = [[0]*s1]*s2
    for i in range(1,s1+1):
        matrix[i][0]=i
    for j in range(1,s2+1):
        matrix[0][j]=j
    for i in range(1,s1):




def edit_distance(str1, str2):

    m = len(str1)
    n = len(str2)
    L = [[i for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        L[i][0] = L[i - 1][0] + 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                L[i][j] = L[i - 1][j - 1]
            elif j < n and i < m and str1[i - 1] == str2[j] and str1[i] == str2[j - 1]:
                L[i][j] = L[i - 1][j - 1]
            else:
                L[i][j] = 1 + min(L[i - 1][j], L[i - 1][j - 1], L[i][j - 1])

    return L[-1][-1]


def edits_one(word,word2="."):
    "Create all edits that are one edit away from `word`."
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [left + right[1:] for left, right in splits if right]
    inserts = [left + c + right for left, right in splits for c in alphabets]
    replaces = [
        left + c + right[1:] for left, right in splits if right for c in alphabets
    ]
    transposes = [
        left + right[1] + right[0] + right[2:]
        for left, right in splits
        if len(right) > 1
    ]
    return set(deletes + inserts + replaces + transposes)