#average = O(n^2)
def bubble_sort(my_list):
    swaps = 0
    #start at length of list -1 and go down until you reach 0
    for i in range(len(my_list) -1 , 0, -1):
        #iterate forwards up to i
        for j in range(i):
            #if current element greater than next element swap them
            if my_list[j] > my_list[j+1]:
                swaps += 1
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list, swaps

array = [4,5,6,8,1,3,4,5,7,9,0]
print('bubble sort\n',bubble_sort(array),'\n')

#average = O(n^2)
def selection_sort(my_list):
    swaps = 0
    #loop through each element keeping track of the index of the minimum element
    for i in range(len(my_list)-1):
        min_index = i
        #loop through elements after i
        for j in range(i+1, len(my_list)):
            #compare elements and update min_index if needed
            if my_list[j] < my_list[min_index]:
                min_index = j
        #swap current index with min_index if needed
        if i != min_index:
            swaps += 1
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list, swaps

array = [4,5,6,8,1,3,4,5,7,9,0]
print('selection sort\n',selection_sort(array),'\n')

#average = O(n^2), on almost sorted data = O(n)
def insertion_sort(my_list):
    swaps = 0
    #start at second element and compare it to the element before it
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        #keep comparing current element to the one before it
        while temp < my_list[j] and j > -1:
            swaps += 1
            #if current is less than one before swap them and move down
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list, swaps

array = [4,5,6,8,1,3,4,5,7,9,0]
print('insertion sort\n',insertion_sort(array),'\n')

#helper function for merge sort, takes two sorted lists
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    #compare each element of each list and add the larger one to 
    # combined list then go down the list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    #if either list still has elements dump them into combined list
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined
#merge sort does not sort in place, it creates a new sorted list
def merge_sort(my_list):
    #if the list has 1 element just return that one element
    if len(my_list) == 1:
        return my_list
    #get middle index of list
    mid_index = int(len(my_list)/2)
    #split the list into the left and right halves and call merge sort on then
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

array = [4,5,6,8,1,3,4,5,7,9,0]
print('merge sort\n',merge_sort(array),'\n')

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list


#helper for pivot
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

#helper function for quick sort
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

array = [4,5,6,8,1,3,4,5,7,9,0]
print('quick sort\n',quick_sort(array),'\n')