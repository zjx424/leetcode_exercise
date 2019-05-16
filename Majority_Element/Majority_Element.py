class Solution:
    def majorityElement(self, nums):
    	count_dict={}
    	val_list=[]
    	for i in nums:
    		count_dict[i]=count_dict.get(i,0)+1
    	for key,val in count_dict.items():
    		val_list.append(val)
    	max_val=max(val_list)
    	for key in count_dict:
    		if count_dict[key]==max_val:
    			return key













if __name__ == '__main__':
	solution=Solution()
	nums=[1,1,2,2,2,2]
	solution.majorityElement(nums)