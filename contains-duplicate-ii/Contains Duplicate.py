class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
    	dict={}
    	for i, v in enumerate(nums):
    		if v in dict and i-dict[v]<=k:
    			print("T")
    			return True
    		dict[v]=i
    	return False






if __name__ == '__main__':
	solution=Solution()
	nums=[1,2,3,1,2,3]

	k=3

	solution.containsNearbyDuplicate(nums,k)