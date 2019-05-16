class Solution:
    def reverseBits(self, n):
    	return int(bin(n)[2:].zfill(32)[::-1],2)






#>>取整
#zfill从左边开始填充到zfill里面的数(n),n位
#bin函数可以把数字n转化为2进制,且转化为的形式是字符串形式,可以进行切片操作
#转化为的字符串前面带有0b,0o,0x的前缀,需要去掉
if __name__ == '__main__':
	n=10101
	solution=Solution()
	result=solution.reverseBits(n)
	print(result)

	