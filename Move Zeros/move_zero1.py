class Solution(object):
    def moveZeroes(self, nums):
    	zeros=0
    	for i in range(len(nums)):
    		if nums[i]!=0:
    			#如果遇到0则不交换 
    			#如果遇到非0,0的位置加1,交换


    			nums[i],nums[zeros]=nums[zeros],nums[i]#python的交换
    			
    			zeros+=1






if __name__ == '__main__':
	solution=Solution()
	nums=[1,2,0,5,0,9]
	solution.moveZeroes(nums)
	print(nums)