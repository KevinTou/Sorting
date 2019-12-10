# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Get the total number of elements
    elements = len(arrA) + len(arrB)

    # Create a list based on the size of elements
    merged_arr = [0] * elements
    # TO-DO

    # Initialize reference points to keep track of increments
    a_count = 0
    b_count = 0

    # Go through the list and replace the 0's with the smallest element between arrA and arrB
    for index in range(elements):
        # Checks to see if the list is done sorting on side A and assigns the current index to the value of arrB[b_count]
        if a_count >= len(arrA):
            merged_arr[index] = arrB[b_count]
            b_count += 1
        # Checks to see if the list is done sorting on side B and assigns the current index to the value of arrA[a_count]
        elif b_count >= len(arrB):
            merged_arr[index] = arrA[a_count]
            a_count += 1
        # If the value of a is smaller, assign a to the merged_arr[index] and move on to its next reference point
        elif arrA[a_count] < arrB[b_count]:
            merged_arr[index] = arrA[a_count]
            a_count += 1
        # Otherwise, assign b to the merged_arr[index] and move on to its next reference point
        else:
            merged_arr[index] = arrB[b_count]
            b_count += 1

    # Returns the merged array
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    if len(arr) > 1:
        # Get the middle (floor division)
        middle = len(arr) // 2
        # Get everything from the LHS and break it down until you get a list of length 1
        left = merge_sort(arr[:middle])
        # Get everything from the LHS and break it down until you get a list of length 1
        right = merge_sort(arr[middle:])
        # Re-assign arr
        arr = merge(left, right)
    return arr

    # # STRETCH: implement an in-place merge sort algorithm
    # def merge_in_place(arr, start, mid, end):
    #     # TO-DO

    #     return arr

    # def merge_sort_in_place(arr, l, r):
    #     # TO-DO

    #     return arr

    # # STRETCH: implement the Timsort function below
    # # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
    # def timsort( arr ):

    #     return arr
