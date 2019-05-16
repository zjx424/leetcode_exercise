#Time Limit Exceeded




class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
    	len_nums=len(nums)
    	for i in range(len_nums):
    		for j in range(1,k+1):
    			try:
    				if nums[i]==nums[i+j]:
    					return True
    			except:
    				pass

if __name__ == '__main__':
	for x in xrange(1,10):
		print(x)