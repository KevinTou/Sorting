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
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # The sort will keep running until no more swaps are made
    while True:
        # The initialization of the ending condition
        swap = 0

        # Goes through the array and swaps if the value on the RHS is smaller than the current value
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # Increases swap count
                swap += 1

        # Breaks when the for loop can make a clean pass
        if swap == 0:
            break
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
