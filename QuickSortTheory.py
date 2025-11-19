# Quick Sort

list = [42,11,3,21,7,15]

# To sort in ascending order, we need two pointers.

pointer1 = 42 #always at the beginning of the list
pointer2 = 15 #always at the end of the list

# We compare the two pointers
# If p1 > p2 then we swap the two

# This would change the list to: 15, 11, 3, 21, 7, 42

# We then swap the pointers
# If it isn't or we've just done a swap, pointer 1 always moves towards pointer 2

# So now
pointer1 = 7

# We now continue the process with comparisons and moving the pointers.

# We will eventually reach a list like this: 3, 7, 11, 15, 21, 42

# We now use recursion once we have the pivot value.

# We have a left list of 3,7,11
# Right list is 21,42

# We now do the same for these two lists

# We then split lists again, if we have an empty list we use recursion to send it back to where it originally came from.
