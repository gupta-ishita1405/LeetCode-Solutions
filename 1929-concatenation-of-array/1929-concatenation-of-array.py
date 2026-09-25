class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        ans=[]

        for i in range(n):
            ans.append(nums[i])
        
        return nums+nums
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna