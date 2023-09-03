class BTree:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
        self.currentSmallerThan=0
        

def rightSmallerThan(array):
    # Write your code here.
    """ 
    Find the number of items in the array which are smaller than it and  right to 
    the current element's index 

    Args:
        array (integer) 
    Return:
        array(integer)
    """
    output = []
    n = len(array)
    if n ==1:
        return [0]
    for i in range(n-1):
        current = array[i]
        temp = array[i+1:]
        temp.sort(reverse=True)
        count = 0
        for j in range(len(temp)):
            if temp[j]>current:
                continue
            else:
                count=len(temp)-j
                break
        output.append(count)
    output.append(0)
    return output

arr = [8, 5, 11, -1, 3, 4, 2]
print(rightSmallerThan(arr))
        
    
    
    
    
