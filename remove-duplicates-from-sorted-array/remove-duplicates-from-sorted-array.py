
class Solution:
    def removeDuplicates(self, nums):
    	if not nums:
    		return 0
    	count=1
    	i=0
    	for j in range(1,len(nums)):
    		if nums[j]!=nums[i]:
    		#nums[1]!=num[0] i=1 nums[1]=num[1] 
    		#nums[4]!=num[1] i=2 nums[2]=nums[4]
    			i+=1
    			nums[i]=nums[j]
    			count+=1
    		else:#可有可无
    			continue#可有可无

    	print(count)
    	return count





if __name__ == '__main__':
	solution=Solution()
	nums=[0,1,1,1,2,2,3,3]
	solution.removeDuplicates(nums)