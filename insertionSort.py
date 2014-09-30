#Insertion Sort
import random

#creates an array of 200 random integers between 0 and 1M (non-distinct ie possible duplicates)
array=[random.randint(0,1000000) for i in range(0,200)]

#5,2,3,6,7,8

print(array)

def insertion_sort(array):
    for i in range(0,len(array)): #scan the entire array
        pointer = array[i] #set pointer object to variable called pointer  =>2
        while (i>0 and array[i-1] >pointer):
            array[i] = array[i-1]
            i = i -1
        array[i] = pointer
        
    return array
    
print ("=================================")
print (insertion_sort(array))
