import numpy as np
def binary_search(x:int, arr:list[int]):
    print('input : {} searching : {}'.format(arr,x))

    left, right =0,len(arr)-1#floor division operator
    mid=(right-left)//2 
    print(left, right, mid, arr)


    counter =1
    while(left<=right):
        print('counter : {} left : {} mid : {} right : {}'
              .format(counter, arr[left], arr[mid], arr[right] ))
        if x ==arr[mid]:
            print('FOUND {} in {} steps'.format(x,counter))
            return

        if x<arr[mid] :
            right = mid-1
            mid = (left+right)//2
            print('x < mid : ',left, right, mid)
        else:
            left = mid +1
            mid = (left+right)//2
            print('x < mid : ',left, right, mid)
        counter+=1    

    print(x,' NOT FOUND')        


#binary_search(10, np.random.randint(10,100,10))
binary_search(70000000, np.arange(10,1100000000,10))
