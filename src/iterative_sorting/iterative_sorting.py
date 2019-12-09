# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr) - 1):
            # Update the smallest_index if the current value is smaller
            if arr[j + 1] < arr[smallest_index]:
                smallest_index = j + 1
            # TO-DO: swap
        # Temporarily hold the value of the array[cur_index] before overwriting it
        temp = arr[cur_index]
        # Sets the cur_index's value to the smallest_index's value
        arr[cur_index] = arr[smallest_index]
        # Complete the final swap by assigning the smallest_index's value to the cur_index's value
        arr[smallest_index] = temp
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
