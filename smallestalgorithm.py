"""
Question 4:
"""

input = [4, 7, 2, 5]


def findsmallest(lst, k):
    # Remove duplicates
    nodups = set(lst)

    # Create list and sort
    sortedlist = list(nodups)
    sortedlist.sort()

    return sortedlist[k - 1]


if findsmallest(input, 2) == 4:
    print("Found the 2nd smallest element: 4!")

"""
Question 5:

In order to find the kth smallest number, you have to maintain a sorted list of
'found' smallest numbers to compare to. Our best-case sort algorithms are O(nlog(n)),
so it is unlikely (impossible?) to find a linear BigO algorithm to manage our inner
function of smallest k.

The worst case for a k value would be half the list, since values over half the list
could be found using (list - k)th greatest value instead.

If you drop the (1/2) coefficient of our inner function, it still has a BigO of
O(nlog(n)).

As a result, you might as well just sort the whole outer list and index to the kth
smallest to get your result, as seen in question 4.
"""
