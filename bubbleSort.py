#Buble Sort
import random
array = [random.randint(0,100000) for i in range(0,100)]

print (array)

def bubble_sort(array):
    for i in range(0,len(array)): #start at left node index [0] #pointer
        for j in range(i+1,len(array)): #check the next node [i+1]
            if array[i]>array[j]: #if pointer is bigger than next node swap
                temp = array[i]  # store pointer 
                array[i] = array[j] #make pointer the lesser value
                array[j] = temp #give next node the bigger value
                #continue checking each element against the pointer value
    return array


print (bubble_sort(array))
