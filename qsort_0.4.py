
'''

QuickSort Algorithm (Python)
last change: 10.01.2021
by: Konrad Lange

'''

#   --- imports ---
from random import randint
import timeit
#   --- code ---

count = 0

def qsort(array):   #define function qsort() and give access to list array

    less = []       #define the sublists less, equal, greater
    equal = []
    greater = []

    if len(array) > 1:      #if list has more than one element

        pivot = array[0]    #use first element as pivot

        for x in array:     #for every element x in the given list 
            
            if x < pivot:           #if x is smaller than pivot
                less.append(x)      #append x to less
                
            elif x == pivot:        #if x is equal to pivot
                equal.append(x)     #append x to equal
                
            elif x > pivot:         #if x is greater than pivot
                greater.append(x)   #append x to greater
                
        return qsort(less) + equal + qsort(greater)         #return the less after running it through qsort, return equal, return the less after running it through qsort <-- recursive 

    else:
        return array                #if given list has only one element in it return the list

def main():     #define function main()

    array = []  #create an empty list

    for j in range(0, 1):

        for i in range(0, 1000000):          #do the following 10 times
            num = randint(0, 999)        #generate a random integer between 0 and 99
            array.append(num)           #and add it to the empty list

    start = timeit.default_timer()      #start timer
    sorted_array = qsort(array)         #saving result of qsort(array) in sorted_array
    end = timeit.default_timer()        #end timer
    runtime = (end - start)             #calculating runtime
    print('runtime:', runtime, 's')     #printing runtime
    print('sorted: ', sorted_array)     #print sorted_array
    
main()                                  #calling main()