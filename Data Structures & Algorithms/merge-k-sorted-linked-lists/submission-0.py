# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final=ListNode()

        heap=[]
        for x in lists:
            curr=x
            while curr:
                heapq.heappush(heap,curr.val)
                curr=curr.next

        root=final=ListNode()
        while heap:
            x=heapq.heappop(heap)
            
            temp=ListNode()
            temp.val=x
            final.next=temp
            final=final.next
        
        return root.next