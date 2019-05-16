#需要从除第一个数开始循环

class Solution:
	def majorityElement(self, nums):
		majority=nums[0]
		count=1
		for i in nums[1:]:
			if count==0:
				majority=i
			if majority==i:
				count+=1
			else:
				count-=1
		return majority










if __name__ == '__main__':
	solution=Solution()
	nums=[6,5,5]
	solution.majorityElement(nums)



