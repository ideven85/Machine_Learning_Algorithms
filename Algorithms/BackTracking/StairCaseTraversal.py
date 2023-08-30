def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return recursiveStaircaseTraversal(height,maxSteps,{0:1,1:1})

# Top down Approach
def  recursiveStaircaseTraversal(height,maxSteps,memo):
    if height in memo:
        return memo[height]
    numberOfWays=0
    for i in range(1,maxSteps+1):
        if i<=height:
            numberOfWays+=recursiveStaircaseTraversal(height-i,maxSteps,memo)
    memo[height]=numberOfWays
    return numberOfWays

if __name__ == "__main__":
    print(staircaseTraversal(4,2))
            