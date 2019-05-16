#输入类型:
#1 s="{}[]{}"
#2 s="[{()}]"
#3 s="[(]"
#4 s="]"



class Solution:
    def isValid(self, s):
    	stack=[] # 设置堆栈
    	mapping = {")": "(", "}": "{", "]": "["} # 设置字典用于匹配 注意是反括号对应正括号
    	if len(s)%2==1: # 如果长度为单数直接排除True 返回False
    		print("False")
    		return False
    	else:
	    	for i in s:
	    		if i not in mapping:
	    			stack.append(i)
	    		elif i in mapping and stack!=[]:# 如果是反括号进的话且为第一个
	    			top=stack[-1]
	    			if top==mapping[i]:
	    				stack.pop()
	    			else:
	    				print("F")
	    				return False
	    	if stack==[]:
	    		print("T")
	    		return True
	    	else:
	    		print("F")
	    		return False


    	
    	
    		


if __name__ == '__main__':
	solution=Solution()
	string="(])"
	solution.isValid(string)
	
	

	