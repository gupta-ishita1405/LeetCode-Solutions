class Solution(object):
    def runningSum(self, nums):
        n=len(nums)
        ans=[]
        for i in range(1,n+1):
            s=0
            for j in range(i):
                s += nums[j]
            ans.append(s)
        return ans
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna