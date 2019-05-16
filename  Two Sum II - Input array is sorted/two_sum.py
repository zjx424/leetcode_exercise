class Solution:
    def twoSum(self, numbers, target):
        len_numbers=len(numbers)
        index_array=[]
        new_list=[]
        for index in range(len_numbers):
            if target-numbers[index] not in new_list:
                new_list.append(numbers[index])
            else:
                index_first=numbers.index(target-numbers[index])
                index_array.append(index_first+1)
                index_array.append(index+1)
        print(index_array)
        return index_array





if __name__ == '__main__':
    solution=Solution()
    numbers=[2,3,18,23,68,90,12,45,67,89,4]
    target=30
    solution.twoSum(numbers,target)