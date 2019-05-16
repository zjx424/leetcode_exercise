class Solution:
	def hammingWeight(self, n):
		return bin(n).count('1')
		



if __name__ == '__main__':
	solution=Solution()
	solution.hammingWeight(00000000000000000000000000001011)
	