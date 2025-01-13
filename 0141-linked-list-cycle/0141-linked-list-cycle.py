# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 연결 리스트의 헤드가 None -> 뭣도 없음 (사이클 x) : False 
        if not head:
            return False
        
        # 두 포인터 초기화: slow는 한 칸씩, fast는 두 칸씩 이동
        slow = head
        fast = head
        
        # fast 포인터가 None이 아니고 fast.next도 None이 아닌 동안 반복
        while fast and fast.next:
            slow = slow.next        # slow 포인터를 한 칸 이동
            fast = fast.next.next   # fast 포인터를 두 칸 이동
            
            # 두 포인터가 만나면(같으면) 사이클 있을유 
            if slow == fast:
                return True
        
        # fast가 None에 도달 (=갈 데 까지 간 상황) 사이클 없음 -> False
        return False