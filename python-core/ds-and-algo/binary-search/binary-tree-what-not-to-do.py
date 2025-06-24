import time
import numpy as np

def binary_tree( x:int,  arr:list[int]):
    print(arr)

    mid, left_index, right_index,counter = int(len(arr)/2),0,len(arr)-1,0
    #[1,2,3,4,5][1]
    while(mid<=right_index):
        if x == arr[mid]:
            print('found {} in {} counter'.format(x,counter))
            return
        
        if mid == right_index:
            print('{} NOT FOUND '.format(x))
            return -1
        
        print('\nmid[{}]:{}, right[{}]:{}, x:{} arr{}'
              .format(mid,arr[mid],right_index,arr[right_index],x,arr))
        if x < arr[mid]:
            arr = arr[0:mid]
            mid = int(len(arr)/2) #new mid
            right_index=len(arr)-1 #new right
            print('NEW < : ',arr, mid, right_index)
            print('x < mid ::: mid[{}]:{} , right[{}]:{}, x:{}, arr {} '
                  .format(mid,arr[mid],right_index,arr[right_index],x,arr))
        elif x > arr[mid] <=arr[right_index]:
            arr = arr[mid+1:]#start from next of mid index
            mid = int(len(arr)/2) #new mid
            right_index=len(arr)-1 #new right
            print('NEW : ',arr, mid, right_index)
            print('x < mid ::: mid[{}]:{} , right[{}]:{}, x:{}, arr {} '
                  .format(mid,arr[mid],right_index,arr[right_index],x,arr))
        else:
            print('{x} NOT FOUND '.format(x))
            return -1
        counter+=1
            
    return -1    

def optimised_binary_tree(x:int,arr:list[int]):
    print("Array:", arr)
    left_index, right_index = 0, len(arr) - 1
    counter = 0

    while left_index <= right_index:
        counter += 1
        mid = (left_index + right_index) // 2  # Calculate the middle index

        if arr[mid] == x:
            print(f"Found {x} at index {mid} in {counter} steps")
            return mid  # Return the index where the value is found
        elif x < arr[mid]:
            right_index = mid - 1  # Narrow the search to the left half
        else:
            left_index = mid + 1  # Narrow the search to the right half

    print(f"{x} NOT FOUND in {counter} steps")
    return -1  # Return -1 if the value is not found



sorted_array =np.sort(np.random.randint(1,100,size=10))

binary_tree(-466,[28, 29, 33, 44, 45 ,46, 61, 69 ,84 ,92])


def using_linear_search( x:int,  arr:list[int]):

    start = time.time()
    print('using brute force')
    counter = 0
    for i in arr:
        if i==x:
            print('found :{} in {} steps'.format( x,counter))
            break
        counter+=1
    print('time taken :{} ms'.format(((time.time()-start))*1000))    
    print('----------------------------------------')
