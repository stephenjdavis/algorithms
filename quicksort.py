def quicksort(arr):
    # Check for an array containing one or no numbers and return it.
    if len(arr) <= 1:
        return arr

    # Create three arrays
    less = []
    equal = []
    greater = []
    # Create a pivot (We could use and the randint function but we'll just use the middle value.)
    pivot = arr[len(arr) // 2]

    # Iterate through every number in the passed array and add each to the appropriate new array
    # based on the pivot value.
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    # Recursively call this function by passing the less array and the greater array
    # until the sort is complete
    sorted = quicksort(less) + equal + quicksort(greater)
    return sorted


print (quicksort([3,5,7,88,6,4,67,4,3,223,4,56,78,64,]))