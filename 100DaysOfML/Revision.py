
"""
Given two sorted integer arrays arr1 and arr2,
 return a new array that combines both of them and is also sorted
"""
def combine(arr1, arr2):
    n = len(arr1);m=len(arr2)
    output=[0 for _ in range(n+m)]
    first=0;second=0;third=0

    while first<n and second<m:
        if arr1[first]<arr2[second]:
            output[third]=arr1[first]
            first+=1
        elif arr1[first]>arr2[second]:
            output[third]=arr2[second]
            second+=1
        else:
            output[third]=arr1[first]
            third+=1
            output[third]=arr1[first]
            first+=1
            second+=1
        third+=1
    #print(output)
    while first<n:
        output[third]=arr1[first]
        third+=1;first+=1
    while second<m:
        output[third]=arr2[second]
        third+=1;second+=1
    return output

a=list(range(1,10))
b=list(i for i in range(1,10) if i%2==0)
print(combine(a,b))
