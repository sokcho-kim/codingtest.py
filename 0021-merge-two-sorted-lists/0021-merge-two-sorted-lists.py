# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy  # 병합된 리스트의 마지막 노드(포인터)

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 한 리스트가 끝난 후 남은 노드를 병합 리스트에 추가
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

        # 연결 리스트 생성 헬퍼 함수
        def create_linked_list(arr: List[int]) -> Optional[ListNode]:
            dummy = ListNode(0)
            current = dummy
            for val in arr:
                current.next = ListNode(val)
                current = current.next
            return dummy.next
