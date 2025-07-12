from black.trans import defaultdict


def house_robber(arr):
    """
    Given an array of consecutive houses containing the money
    contained in each house, a house robber decides to rob houses non consecutive
    Give the maximum money he can rob
    Args:
        arr: array of numbers
    returns: the maximum amount of money house robber can rob

    """
    def helper_recursive(m):
        if m<=0:
            memo[0]=arr[0]
            return memo[0]
        elif m==1:
            memo[1]=max(arr[0],arr[1])
            return memo[1]
        elif m in memo:
            return memo[m]
        else:
            memo[m]=max(helper_recursive(m-1),arr[m]+helper_recursive(m-2))
            return memo[m]
    n = len(arr)
    #dp = [0]*n
    memo = defaultdict(int)
    maxi=helper_recursive(n-1)
    return maxi

def main():
    arr = [1,2,3,5,4]
    print(house_robber(arr))

if __name__ == '__main__':
    main()