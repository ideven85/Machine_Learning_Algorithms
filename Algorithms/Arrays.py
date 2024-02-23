import math
from collections import deque
from typing import List, Optional

def moveElementToEnd(array, toMove):
    # Write your code here.
    count = 0
    for i in range(len(array)):
        if array[i]!=toMove:
            array[i],array[count]=array[count],array[i]
            count+=1
    return array

def divide(self,dividend: int, divisor: int) -> int:
    answer = 0
    flag = False
    if dividend==0:
        return 0

    if dividend<0 and divisor<0:
        if divisor==-1 and dividend<=-pow(2,31):
            return pow(2,31)-1
    if dividend > 0 > divisor or dividend < 0 < divisor:
        flag = True



    dividend = abs(dividend)
    divisor = abs(divisor)
    flag2 = False
    if divisor==1:
        flag2=True
    a = divisor
    if divisor!=1:
        while divisor<=dividend:
            divisor+=a
            answer+=1
    print("Hi hello deven here")
    print(divisor)
    if not flag:
        if answer>=pow(2,31)-1:
            answer=pow(2,31)-1

    else:
        answer=-answer
        if answer<-pow(2,31):
            answer=-pow(2,31)
    if flag2:
        if flag:
            dividend=-dividend
            if dividend>=pow(2,31)-1:
                dividend=pow(2,31)-1
            elif dividend<-pow(2,31):
                dividend=-pow(2,31)
        return dividend


    return answer

def findMaxAverage( nums: List[int], k: int) -> float:
    n = len(nums)
    left=0;right=n-1
    total=nums[0]
    maximum = 0
    curr = 1

    for i in range(1,n):
        for j in range(i,k):
            total+=nums[k]



    print(total,maximum)  
    return maximum/k


    
        






def nonConstructibleChange(coins:List[int])->int:
    # Write your code here.
    coins.sort()
    change= 0
    for coin in coins:
        if coin>change+1:
            break
        change+=coin
    return change+1





def insert(nums1: List[int],m:int,nums2:List[int],n:int,position):
        pass

def threeSum( nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        first=0;second=0;third=0;total=0
        low=0;high=n-1
        while low<=high:
            first = low
            for i in range(first,high):
                second = high
                total = nums[first]+nums[second]
                if total>0:
                    s = high
                    while total+nums[s]>0:
                        s-=1
                    if total+nums[s]==0:
                        answer.append([nums[first],nums[second],nums[s]])
        return answer

    # Accepted after 10 months
def threeSumV2( nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        for i in range(n-2):
            if i == 0 or (i>0 and nums[i]!=nums[i-1]):
                ans = -nums[i]
                low = i+1
                high = n-1
                while low<high:
                    if nums[low]+nums[high]==ans:
                        answer.append([nums[i],nums[low],nums[high]])
                        print(answer,end=' ')
                        while nums[low]==nums[low+1] and low<n-2:
                            low+=1

                        while nums[high]==nums[high-1] and high>1:
                            high-=1

                        low+=1;high-=1
                    else:
                        if nums[low]+nums[high]>ans:
                            high-=1
                        else:
                            low+=1
        return answer

def subArraySum(arr:list,n:int,s:int)->list:
    """

    :param arr: Unsorted array but positive elements
    :param n: size of arr
    :param s: sum to check
    :return: list of indices for which subarray sums to s
    """
    answer = list()
    x = 0
    first = 0; second = 0
    if n < 2:
        return [-1]

    for i in range(n):
        second = i
        x+=arr[i]
        if x == s:
            return [first,second]
        elif x > s:
            first+=1;x = arr[first]
def firstMissingPositiveforContinousN(nums: List[int]) -> int:
    print(nums)
    n = len(nums)
    aux = [-1 for _ in range(n)]
    maxi = 1;j=0
    for i in range(n):
        if maxi <=nums[i]:
            maxi = nums[i]
        if nums[i]>0:
            aux[j]=min(maxi,nums[i])
            j+=1
    print("Aux=",aux)
    if maxi == 1:
        return 1

    for i in range(j-1):
        if aux[i]!=aux[i+1]:
            return aux[i+1]
    return maxi+1


def removeElement( nums: List[int], val: int) -> int:
    answer = len(nums)
    i = 0
    while i < len(nums):
        if nums[i]==val:
            j = i
            answer-=1
            for j in range(i+1,len(nums)):
                if nums[j]!=val:
                    break
                else:
                    answer-=1
            nums[i]=nums[j]
            i = j
        else:
            i+=1


    return answer




def reverse(arr,k):
    for i in range(k//2):
        temp = arr[i]
        arr[i]=arr[k-i]
        arr[k-i]=temp
def rotateByK(arr:List[int],n:int,k:int)->None:
    for i in range(k):
        arr.insert(0,arr.pop())









def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        length = len(nums1)
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2[0] > nums1[m - n]:
            nums1[length-m:] = nums2
            return
        elif nums2[n - 1] > nums1[m - n - 1]:
            nums1[length-m - n] = nums2[n - 1]
            merge(nums1, m, nums2, n - 1)
        elif nums2[n] == nums1[m - n - 1]:
             insert(nums1, nums2, n, m, m - n - 1)
             merge(nums1, m, nums2, n - 1)
        else:
             insert(nums1, nums2, n, m, m - n)
             merge(nums1, m, nums2, n)

def binarySearch(nums, low, high, target,answer):
        if low>=high:
            return answer
        mid = math.floor((low+high)//2)
        if target<nums[mid]:
           return binarySearch(nums,low,mid-1,target,answer)
        elif target == nums[mid]:
            print(mid)
            answer.append(mid)
            mid+=1
            while nums[mid]==target:
                answer.append(mid)
                mid+=1
            return answer
        else:
           return binarySearch(nums,mid+1,high,target,answer)

def searchRange(self,nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        low = 0; high = len(nums)-1;answer = []
        answer = []
        answer=self.binarySearch(nums,low,high,target,answer)
        if len(answer)==0:
             return [-1,-1]
        else:
             return answer

def searchRangeV2(nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        low = 0; high = len(nums)-1;answer = []
        while low<=high:
            mid = math.floor((low+high)//2)
            if nums[mid]==target:
                answer.append(mid)
                tmp = mid
                if tmp-1>=0:
                    while nums[tmp-1]==target:
                        answer.append(tmp-1)
                        tmp-=1
                    tmp = mid
                if tmp+1<len(nums):
                    while nums[tmp+1] == target:
                        answer.append(tmp+1)
                        tmp+=1
                    return [min(answer),max(answer)]
            elif target<nums[mid]:
                high=mid-1

            else:
                low=mid+1
        return [-1,-1]

def searchInsert( nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            if nums[0]==target:
                return 0
            else:
                return 1
        else:
            low = 0; high = n-1
            while low<=high:

                mid = math.floor((low+high)/2)

                if (mid+1<n) and nums[mid]<target<nums[mid+1]:
                    return mid+1
                elif (mid-1)>=0 and nums[mid-1]<target<nums[mid]:
                    return mid
                elif target == nums[mid]:
                    return mid
                elif target<nums[mid]:
                    high=mid-1
                elif target>nums[mid]:
                    low=mid+1
            return low



def canBeIncreasing( nums: List[int]) -> bool:
        possible = False
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1] and not possible:
                possible=True
            elif nums[i]>=nums[i-1] and possible:
                possible=False
        return possible



def search( nums: List[int], target: int) -> int:
    """
    An array rotated at a pivot
    Find whether the target exists in the num in O(log(n)) time
    """
    def binarySearch(nums:List[int],target,low,high):
        while low<=high:
            mid = (low+high)//2
            #print(nums[mid],end=' ')
            if target==nums[mid]:
                return mid
            if nums[low]<= nums[mid]:
                if nums[low]<=target<=nums[mid]:
                   high=mid-1
                else:
                    low=mid+1

            else:
               if nums[mid]<=target<=nums[high]:
                    low=mid+1
               else:
                   high=mid-1

            #}





    answer = binarySearch(nums,target,0,len(nums)-1)
    return -1 if answer is None else answer

def factorial(n):
    return 1 if n<2 else n*factorial(n-1)


#todo
def threeSumClosest( nums: List[int], target: int) -> int:
    """


    :param nums:  Given an integer array nums of length n
    :param target: an integer target,
    :return:  find three integers in nums such that the sum is closest to target.
    """
    nums.sort()
    low = 0;n = len(nums);high=n-1;total=0
    return 0













def isSortedIncreasing(array):
    if len(array)<=1:
        return True
    return array[0]<=array[1]  and isSortedIncreasing(array[1:])

def isSortedDecreasing(array):
    if len(array)<=1:
        return True
    return array[0]>=array[1] and isSortedDecreasing(array[1:])

def isMonotonic(array):
    # Write your code here.
    """if array is None or len(array)==1:
        return True
    increasing = False;decreasing=False
    for i in range(len(array)-1):
        if array[i]<array[i+1]or array[i]==array[i+1]:
            decreasing=True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1] or array[i] == array[i + 1]:
            increasing= True
    return increasing or decreasing
    """
    return isSortedDecreasing(array) or isSortedIncreasing(array)


def pascal_triangle(rows, col):
    if col == 0:
        return 1
    elif rows == 0:
        return 0
    else:
        return pascal_triangle(rows -1, col) + pascal_triangle(rows -1, col -1)

def generate(numRows: int) -> List[List[int]]:
    return pascal_triangle(5,2)


def findMin(nums: List[int]) -> int:
    n = len(nums)-1
    for i in reversed(range(n)):
        if nums[i]>nums[i-1]:
            return nums[i-1]
    return nums[0]

def sortedSquaredArray(array):
    # Write your code here.

    output = []

    for e in array:
        output.append(e*e)
    output.sort()
    return output


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    minimum = 1234556
    n = len(arrayOne)
    m = len(arrayTwo)
    output = []

    first=0;second=0
    while first<n and second<m:
        if arrayOne[first]==arrayTwo[second]:
            return [arrayOne[first],arrayTwo[second]]
        difference = abs(arrayOne[first]-arrayTwo[second])
        if difference<minimum:
            minimum=difference
            output=[arrayOne[first],arrayTwo[second]]
        if arrayOne[first]<arrayTwo[second]:
            first+=1
        else:
            second+=1


    return output
def rotate( nums: List[int], k: int) ->List[int]:
        n = len(nums)
        if n==1:
            return nums
        k = k%n
        for _ in range(k):
            nums.insert(n-1,nums.pop(0))
        return nums


if __name__ == "__main__":
   print(moveElementToEnd([1,2,3,4,5,2,3,4,2,2,4,5,2],2))
   print(searchRangeV2([5, 7, 7, 8, 8, 10], 2))

   print(searchInsert([1,3,5,6],0))
   nums = [0,1,1]

   print("3 Sum:",threeSumV2(nums))
   print(generate(1))
   a = [3,4,5,1,2]
   a2= list(range(3,10))
   print(findMin(a))
   print(sortedSquaredArray(sorted(nums)))
   print(smallestDifference(a,a2))
   a = list(range(1,6))
   rotate(a,4)
   print(a)
   nums1 = [1, 2, 3, 0, 0, 0]; m = 3; nums2 = [2, 5, 6]; n = 3
   print("Pascal Triangle:",end=' ')
   print(generate(10))
   #a = [1,1,2,3,3,4,5]
   #print(isMonotonic(a))
   array=[5, 2, [7, -1], 3, [6, [-13, 8], 4]]
   print("Searching:")
   print(a)
   print(search(a,1))
   b = [1,4,5,6,7,8,1,2,3]
   print(search(b,9))

   change = [1,2,5]
   print(nonConstructibleChange(b))
   nums = [1,12,-5,-6,50,3]; k = 4
   print(findMaxAverage(nums=nums,k=k))
   print(majorityElement([3,3,3,1,2,2,2,2,1,1,1,1,1,1,2,2,2]))

