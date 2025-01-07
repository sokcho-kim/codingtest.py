class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # 배열을 오름차순으로 정렬
        n = len(nums)  # 배열 길이 저장
        closest_sum = float('inf')  # 가장 가까운 합을 저장할 변수

        # 첫 번째 수를 고정
        for i in range(n - 2):
            left, right = i + 1, n - 1  # 포인터는 각 양 방향에서 부터 온다
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  # 현재 세 수의 합 계산

                # 현재 합이 타겟과 더 가까우면 업데이트
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # 현재 합이 타겟보다 작으면 left 포인터를 오른쪽으로 
                if current_sum < target:
                    left += 1
                # 현재 합이 타겟보다 크면 right 포인터를 왼쪽으로 
                elif current_sum > target:
                    right -= 1
                else:
                    # 현재 합이 정확히 타겟과 같으면 바로 반환
                    return current_sum

        return closest_sum  # 가장 가까운 합을 반환
    