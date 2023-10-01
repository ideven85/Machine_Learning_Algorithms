  Example 1770. Maximum Score from Performing Multiplication Operations
Report Issue
For this problem, we will again start by looking at a top-down approach.
In this article, we're going to be looking at the problem Maximum Score from Performing Multiplication Operations. We can tell this is a DP problem because it is asking for a maximum score, and every time we choose to use a number from 
nums
nums, it affects all future possibilities. Let's solve this problem with the framework:

# 1. A function or array that answers the problem for a given state

In the following discussion, we will use 0-index, since it is more convienient for thinking and coding.
Since we're doing top-down, we need to decide on two things for our function 
dp
dp. What state variables we need to pass to it, and what it will return. We are given two input arrays: 
nums
nums and
multipliers
multipliers. The problem says we need to do m operations, and on the ith operation, we gain score equal to 
multipliers[i] times a number from either the left or right end of nums ,which we remove after the operation. That means we need to know 3 things for each operation:

How many operations have we done so far; this tells us what number from multipliers
 we will be using?
The index of the leftmost number remaining in nums.
The index of the rightmost number remaining in nums

We can use one state variable, i, to indicate how many operations we have done so far, which means 
multipliers[i] is the current multiplier to be used. 
For the leftmost number remaining in nums we can use another state variable, left,
that indicates how many left operations we have done so far. 
If we have done, say 3 left operations, if we were to do another left operation we would use nums[3].
We can say the same thing for the rightmost remaining number - let's use a state variable right that indicates how many right operations we have done so far.
It may seem like we need all 3 of these state variables,
but we can formulate an equation for one of them using the other two. 
If we know how many elements we have picked from the leftside, left, and we know how many elements we have picked in total, i, then we know that we must have picked 
i - left elements from the rightside. The original length of nums is n which means the index of the rightmost element is 
right = n - 1 - (i - left) Therefore, we only need 2 state variables:
i and left,and we can calculate right inside the function.

Now that we have our state variables, what should our function return? 
The problem is asking for the maximum score from some number of operations, 
**so let's have our function dp(i, left) return the maximum possible score if we have already done i total operations and used **left** numbers from the left side. To answer the original problem, we should return dp(0, 0)**
dp(0, 0).


# 2. A recurrence relation to transition between states

At each state, we have to perform an operation. As stated in the problem description, we need to decide whether to take from the left end (
nums[left]
nums[left]) or the right end (
nums[right]
nums[right]) of the current 
nums
nums. Then we need to multiply the number we choose by 
multipliers[i]
multipliers[i], add this value to our score, and finally remove the number we chose from 
nums
nums. For implementation purposes, "removing" a number from 
nums
nums means incrementing our state variables 
i
i and 
left
left so that they point to the next two left and right numbers.

Let 
mult
=
multipliers[i]
mult=multipliers[i] and 
right = nums.length - 1 - (i - left)
right = nums.length - 1 - (i - left). The only decision we have to make is whether to take from the left or right of 
nums
nums.

If we choose left, we gain 
mult
⋅
nums[left]
mult⋅nums[left] points from this operation. Then, the next operation will occur at 
(i + 1, left + 1)
(i + 1, left + 1). 
i
i gets incremented at every operation because it represents how many operations we have done, and 
left
left gets incremented because it represents how many left operations we have done. Therefore, our total score is 
mult
⋅
nums[left] + dp(i + 1, left + 1)
mult⋅nums[left] + dp(i + 1, left + 1).
If we choose right, we gain 
mult
⋅
nums[right]
mult⋅nums[right] points from this operation. Then, the next operation will occur at 
(i + 1, left)
(i + 1, left). Therefore, our total score is 
mult
⋅
nums[right] + dp(i + 1, left)
mult⋅nums[right] + dp(i + 1, left).
Since we want to maximize our score, we should choose the side that gives more points. This gives us our recurrence relation:

dp(i, left)
=
max
⁡
(
mult
⋅
nums[left]
+
dp(i + 1, left + 1)
,
 mult
⋅
nums[right]
+
dp(i + 1, left)
)
dp(i, left)=max(mult⋅nums[left]+dp(i + 1, left + 1), mult⋅nums[right]+dp(i + 1, left))

Where 
mult
⋅
nums[left]
+
dp(i + 1, left + 1)
mult⋅nums[left]+dp(i + 1, left + 1) represents the points we gain by taking from the left end of 
nums
nums plus the maximum points we can get from the remaining 
nums
nums array and
mult
⋅
nums[right]
+
dp(i + 1, left)
mult⋅nums[right]+dp(i + 1, left) represents the points we gain by taking from the right end of 
nums
nums plus the maximum points we can get from the remaining 
nums
nums array.

# 3. Base cases

The problem statement says that we need to perform 
m
m operations. When 
i
i equals 
m
m, that means we have no operations left. Therefore, we should return 
0
0.



Top-down Implementation

Let's put the 3 parts of the framework together for a solution to the problem.

Protip: for Python, the functools module provides super handy tools that automatically memoize a function for us. We're going to use the @lru_cache decorator in the Python implementation.

If you find yourself needing to memoize a function in an interview and you're using Python, check with your interviewer if using modules like functools is OK.
This particular problem happens to have very tight time limits. For Java, instead of using a hashmap for the memoization, we will use a 2D array. For Python, we're going to limit our cache size to 
2000



    class Solution {
        private int[][] memo;
        private int[] nums, multipliers;
        private int n, m;
    
        private int dp(int i, int left) {
                if (i == m) {
                    return 0; // Base case
                }
        
                int mult = multipliers[i];
                int right = n - 1 - (i - left);
                    
                if (memo[i][left] == 0) {
                    // Recurrence relation
                    memo[i][left] = Math.max(mult * nums[left] + dp(i + 1, left + 1), 
                                             mult * nums[right] + dp(i + 1, left));
                }
        
                return memo[i][left];
            }
            
            public int maximumScore(int[] nums, int[] multipliers) {
                n = nums.length;
                m = multipliers.length;
                this.nums = nums;
                this.multipliers = multipliers;
                this.memo = new int[m][m];
                return dp(0, 0);
            }
        }    


Bottom-up Implementation
In the bottom-up implementation, the array works the same way as the function from top-down.
dp[i][left]
dp[i][left] represents the max score possible if
i
i operations have been performed and
left
left left operations have been performed.

Earlier in the explore card, we learned that while bottom-up is typically faster than top-down, it is often harder to implement. This is because the order in which we iterate needs to be precise. You'll see in the implementations below that we use the same math to calculate
right
right, and the same recurrence relation but we need to iterate backwards starting from
m
m (because the base case happens when
i
i equals
m
m). We also need to initialize
dp
dp with one extra row so that we don't go out of bounds in the first iteration of the outer loop.

    class Solution{
        private int dp(int i, int left){
        if(i==m)
            return 0;
        int mult=multipliers[i];
        int right= (n-1-(i-left));
        if(memo[i][left]==0)
            memo[i][left]=Math.max(mult*this.nums[left]+dp(i+1,left+1),
                    mult*nums[right]+dp(i+1,left));

        return memo[i][left];

    }
        public  int maximumScoreV2(int[] nums, int[] multipliers){
            int n = nums.length;
            int m = multipliers.length;
            this.n=n;
            this.m = m;
            this.nums=nums;
            this.multipliers=multipliers;
            this.memo = new int[m][m];
            return dp(0,0);
    
    
        }
    
        public static void main(String[] args) {
            int[] nums = new int[]{1,2,3,4};
            int[] multipliers = new int[]{3,2,1};
            System.out.println(maximumScore(nums,multipliers));
            MatrixMultiplications mm = new MatrixMultiplications();
            System.out.println(mm.maximumScoreV2(nums,multipliers));
        }
    }


In the bottom-up implementation, the array works the same way as the function from top-down. 
dp[i][left]
dp[i][left] represents the max score possible if 
i
i operations have been performed and 
left
left left operations have been performed.

Earlier in the explore card, we learned that while bottom-up is typically faster than top-down, it is often harder to implement. This is because the order in which we iterate needs to be precise. You'll see in the implementations below that we use the same math to calculate 
right
right, and the same recurrence relation but we need to iterate backwards starting from 
m
m (because the base case happens when 
i
i equals 
m
m). We also need to initialize 
dp
dp with one extra row so that we don't go out of bounds in the first iteration of the outer loop.


The time and space complexity of both implementations is 
O
(
m
2
)
O(m 
2
 ) where 
m
m is the length of
multipliers
multipliers. We will talk about more in depth about time and space complexity at the end of this chapter.



Up Next

Try the next two problems on your own. The first one is a very classical computer science problem and popular in interviews. If you get stuck, come back here for hints:

1143. Longest Common Subsequence

Click here to show hint regarding state variables and dp
Click here to show hint regarding the recurrence relation
Click here to show hint regarding base cases
221. Maximal Square

Click here to show hint regarding state variables and dp
Click here to show hint regarding the recurrence relation
Click here to show hint regarding base cases
