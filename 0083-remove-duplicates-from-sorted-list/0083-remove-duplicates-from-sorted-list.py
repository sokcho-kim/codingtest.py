# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        python


from typing import Optional

# 단일 연결 리스트의 노드 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # 노드의 값
        self.next = next      # 다음 노드를 가리키는 포인터

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 헤드가 비어있다면 None을 반환
        if not head:
            return None

        # 현재 노드를 헤드로 초기화
        current = head

        # 연결 리스트의 끝까지 반복
        while current and current.next:
            # 현재 노드의 값과 다음 노드의 값이 같다면
            if current.val == current.next.val:
                # 중복 노드를 건너뛰기 위해 next 포인터를 변경
                current.next = current.next.next
            else:
                # 중복이 아니라면 다음 노드로 이동
                current = current.next

        # 중복이 제거된 리스트의 헤드를 반환
        return head
