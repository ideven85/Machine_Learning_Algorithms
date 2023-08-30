def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
    return array

if __name__ == '__main__':
    a = [1,3,4,10,2]
    print(bubbleSort(a))
    print(a)