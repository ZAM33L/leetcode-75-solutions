# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #get the middle of the linked list to get left and right half
        slow = head
        fast = head

        while fast:
            fast = fast.next.next
            slow = slow.next

        #reverse right half of the linked list
        prev = None

        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        #get the maximum twin sum by getting pairwise sums

        maxTwinSum = 0

        while prev and head:

            maxTwinSum = max(maxTwinSum , prev.val+head.val)
            head = head.next
            prev = prev.next

        #return the maximum twin sum
        return maxTwinSum