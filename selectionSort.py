#selection sort
import random
array=[random.randint(0,1000000) for i in range(0,200)] #generate unsorted array

print(array) #display array

def selection_sort(array):
    for i in range(0,len(array)): #iterate through the length of the array
        min = i #set min to current pointer
        for j in range(i+1,len(array)): #the entire array starting from pointer
            if array[j] < array[min]: #if a value less than pointer 
                min = j #set lesser value to min - ultimately finds least value
                
        if min != i: #if there was a value smaller than the original pointer
            temp = array[i] #store current pointer value
            array[i]=array[min] #set current pointer to new value
            array[min] = temp #set the old low value with the higher value

    return array #return the sorted array
print('==========================================') #visible divider
print(selection_sort(array))  # print sorted array
