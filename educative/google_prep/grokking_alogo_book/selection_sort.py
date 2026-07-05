#from typing import List
def find_minimum(nums:list[int]):
    small = nums[0]
    index = 0
    smallest_index = 0
    for i in nums:
        if i<small:
            small = i
            smallest_index = index
        index +=1    
    return small, smallest_index

def selection_sort(nums : list[int]):
    sorted_nums = []
    copied_nums = nums.copy()
    for _ in nums:
        smallest,index =  find_minimum(copied_nums)        
        sorted_nums.append(smallest)
        copied_nums.pop(index)
        
    print(sorted_nums)


selection_sort([9,8,7,6,5,4,4,3,2,21])        


