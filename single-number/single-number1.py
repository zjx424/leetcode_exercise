class Solution:
    def singleNumber(self, nums):
    	dict={}
    	for i in nums:
    		dict[i]=dict.get(i,0)+1
    	for key,val in dict.items():
    		if val==1:
    			return key







if __name__ == '__main__':
	solution=Solution()
	nums=[2,3,3,1,4,4,2]
	solution.singleNumber(nums)