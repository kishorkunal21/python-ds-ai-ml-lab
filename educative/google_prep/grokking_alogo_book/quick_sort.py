def quick_sort(nums : list[int]):
    if len(nums) <=1:
        return nums## base case
    
    pivot  = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


    

    


print(quick_sort([77,44,55,66,88,99,11,22,43,44]))
    
    