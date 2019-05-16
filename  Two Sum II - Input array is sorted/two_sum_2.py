#使用头尾指针,实现遍历,因为其是排序好的数据,所以直接设置头指针为0,尾指针为len(numbers)-1
#参考教程https://github.com/azl397985856/leetcode/blob/master/problems/167.two-sum-ii-input-array-is-sorted.md

class Solution:
    def twoSum(self, numbers, target):
    	pointer_arry=[]
    	head_pointer=0
    	tail_pointer=len(numbers)-1
    	while head_pointer<tail_pointer:
    		if numbers[head_pointer]+numbers[tail_pointer]<target:
    			head_pointer+=1
    		elif numbers[head_pointer]+numbers[tail_pointer]>target:
    			tail_pointer-=1
    		else:
    			pointer_arry.append(head_pointer+1)
    			pointer_arry.append(tail_pointer+1)
    			break
    	return pointer_arry







if __name__ == '__main__':
	solution=Solution()
	numbers=[4,7,2,8]
	target=15
	solution.twoSum(numbers,target)



