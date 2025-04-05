# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeTwoLists(list1, list2):
    '''Merge the two lists into one sorted list.
    The list should be made by splicing together the nodes of the first two lists.
    >>> Solution().mergeTwoLists([1,2,4], [1,3,4])
    [1, 1, 2, 3, 4, 4]
    >>> Solution().mergeTwoLists([], [])
    []
    '''
    res = []
    for _ in list1, list2:
        res.append(list1)
        res.append(list2)
    return res


class Solution:
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
