class Solution:
    def singleNumber(self, nums):
    	ret=0
    	for i in nums:
    		ret=ret^i
    		print(ret)
    	return ret






if __name__ == '__main__':
	solution=Solution()
	nums=[2,3,3,1,4,4,2]
	solution.singleNumber(nums)
	print('*'*100)
	print(10101^10101) #result == 0
	print(10101^00000) #result == 10101
	print(2^3)         #result == 1




