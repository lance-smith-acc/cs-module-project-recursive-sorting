# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    # Loop while the merged array is smaller than the combined length of the arrays
    for i in range(elements): 
       
        # If A is empty
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # If B is empty
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1 
         # If the value of the current element of A is less than the value of the current element of B, append the value of A to the merged array and count up on A
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # Else, append the value of the current element of B and count up on B
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # While the array is longer than one item, split it
    # Once the array is one element, it is sorted
    # Recombine the array into it's sorted version
    if len(arr) > 1:
        left_arr = arr[0:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)
        arr = merge(left, right)

    return arr

testArr = [5,2,3,1,9,7,8,6]
print(merge_sort(testArr))

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
	# checkStart is the first element in the right
	# half of the list
    checkStart = mid + 1
    # If the two halves we're merging are already
	# sorted, no need to do anything
    if arr[mid] <= arr[checkStart]:
        return
    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and checkStart <= end:
        # If element 1 is in right place
        if arr[start] <= arr[checkStart]:
            start += 1
        else:
            value = arr[checkStart]
            index = checkStart
            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            checkStart += 1
	# we don't return anything in in-place functions
	# since we're directly mutating the input array


def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
