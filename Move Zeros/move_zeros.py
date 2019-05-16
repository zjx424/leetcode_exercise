class Solution(object):
    def moveZeroes(self, nums):
    	for i,v in enumerate(nums):
    		if v==0:
    			nums.remove(0)
    			nums.append(0)
    	return nums






if __name__ == '__main__':
	solution=Solution()
	nums=[0,0,1]
	solution.moveZeroes(nums)