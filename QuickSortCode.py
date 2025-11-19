values = [45,3,22,4,54,34,2] # 7 Values so highest index is 6
def quicksort(array): # Defining function
    if len(array) <= 1: # This is a breaking condition, if length is either 1 or nothing, send it straight back as it is.
        return array
    pointer1 = 0
    pointer2 = len(array) - 1 # Setting up pointer 1 and pointer 2 to the first and last values of the list. Have to -1 as len doesn't count from 0
    while pointer1 != pointer2: # When they are equal to one another, we have found our pivot value
        if ((array[pointer1] > array[pointer2] and pointer1 < pointer 2) or
            (array[pointer1] < array[pointer2] and pointer 1 > pointer2)): """Either or of these can be true, and we start doing comparisons and swaps, we are seeing
if the value of pointer 2 is smaller than pointer1, as we have swapped them we must check them either way round. Either p1 > p2, or we compare the index of the pointers compared to one another,
if either are true we then perform a swap."""
            array[pointer1], array[pointer2] = array[pointer2], array[pointer1] # This swaps the values over, given that the above is true. Whatever values are at p1 gets swapped with p2 and vice versa. We may see a temporary variable where we store the pointers for an exam however.
            pointer1, pointer2 = pointer2, pointer1 # This swaps the pointers over, NOT the values.
            """ Temp variable could be: temp = p1
                                        p1 = p2,
                                        p2=temp
                                                """
        if pointer1 < pointer2: # P1 always moves towards P2, either p1 has to go up one, or down one. These if statements account for this whether it should move towards or away
            pointer1 = pointer1 + 1
        else:
            pointer1 = pointer1 - 1
        left = quicksort(array[0:pointer1])
        right = quicksort(array[pointer1 + 1:len(array)]) # Using list splicing, using recursion we quick sort the left and right lists, the function calls itself recursively, running itself from the inside
        """This is the returning the left, pivot, and right of the list/array"""return left + [array[pointer1]] + right # On line above: No -1 above as we go upto but not including. 
print(quicksort(values))