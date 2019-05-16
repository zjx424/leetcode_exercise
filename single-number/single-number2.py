class Solution:
    def singleNumber(self, nums):
    	set_nums_sum=sum(set(nums))
    	result=set_nums_sum*2-sum(nums)
    	return result












if __name__ == '__main__':
	solution=Solution()
	nums=[2,3,3,1,4,4,2]
	solution.singleNumber(nums)