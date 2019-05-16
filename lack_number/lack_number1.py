class Solution:
    def lack_numbers(self, nums):
    	result=1
    	for i in nums:
    		result=result^i
    	print(result)












if __name__ == '__main__':
	solution=Solution()
	nums=[1,8,9,7,4,3,2,5]
	solution.lack_numbers(nums)