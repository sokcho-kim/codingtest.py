class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums) - 2):  # 기준 숫자 선택
            if i > 0 and nums[i] == nums[i - 1]:  # 중복된 기준 숫자 건너뛰기
                continue
                
            left = i + 1  # 왼쪽 포인터
            right = len(nums) - 1  # 오른쪽 포인터

            while left < right:  # 포인터가 교차하지 않을 때까지 반복
                total = nums[i] + nums[left] + nums[right]  # 합 계산
                
                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # 중복된 왼쪽 숫자 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # 중복된 오른쪽 숫자 건너뛰기
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # 왼쪽 포인터 이동
                    right -= 1  # 오른쪽 포인터 이동
                elif total < 0:
                    left += 1  # 합이 0보다 작으면 왼쪽 포인터 이동
                else:
                    right -= 1  # 합이 0보다 크면 오른쪽 포인터 이동

        return answer