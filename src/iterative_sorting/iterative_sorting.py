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
def count_sort(arr, maximum=-1):
    negative = False

    # Checks to see if there's a maximum passed and sets it if one isn't passed
    if maximum == -1 and len(arr) > 0:
        maximum = max(arr)

    # Check to see if any negative values are inside the passed list
    for i in arr:
        if i < 0:
            negative = True

    if negative == False:
        # Creates an array to hold the count (based on the maximum number)
        count = [0 for x in range(0, maximum + 1)]

        # print("Count before counting: ", count)

        # Goes through and talleys the number from the passed list
        for i in arr:
            count[i] += 1

        # print("Count after counting: ", count)

        # Add the sum of the previous state to the current one
        for i in range(0, maximum + 1):
            if i > 0:
                count[i] = count[i] + count[i-1]

        # print("Count after adding: ", count)

        # Create a new list to hold the sorted numbers
        newList = [x for x in range(len(arr))]

        # Go through the array and place the values in the right index
        for i in arr:
            newList[count[i] - 1] = i
            count[i] -= 1

        # print("New List: ", newList)

        arr = newList
    else:
        arr = "Error, negative numbers not allowed in Count Sort"

    return arr
