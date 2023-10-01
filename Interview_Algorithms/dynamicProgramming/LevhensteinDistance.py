
# O(nm) time O(nm) space
def levenshteinDistance(str1, str2):
    # Write your code here.
    m = len(str1)
    n = len(str2)
    L = [[i for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        L[i][0]=L[i-1][0]+1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                L[i][j]=L[i-1][j-1]
            else:
                L[i][j]=1+min(L[i-1][j],L[i-1][j-1],L[i][j-1])
    for row in L:
        print(row)


    return L[-1][-1]

# O(nm) time O(min(n,m) space
def levenshteinDistanceV2(str1, str2):
    n = len(str1)
    m = len(str2)
    small = str1 if n<m else str2
    big = str1 if n>=m else str2
    evenEdits = [i for i in range(len(small)+1)]
    oddEdits = [None for _ in range(len(small)+1)]
    for i in range(1,len(big)+1):
        if i%2==1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits=evenEdits
            previousEdits=oddEdits
        currentEdits[0]=i
        for j in range(1,len(small)+1):
            if big[i-1]==small[j-1]:
                currentEdits[j]=previousEdits[j-1]
            else:
                currentEdits[j]=1+min(previousEdits[j-1],previousEdits[j],currentEdits[j-1])
        print(currentEdits)
    return evenEdits[-1] if len(big)%2==0 else oddEdits[-1]




a = "yabd"
b = "abc"
print(levenshteinDistanceV2(a,b))