from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        print('开始 l ; r', l, r)
        while l <= r:
            mid = (l + r) // 2
            print(mid, nums[mid])
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                print('左右相等')
                print('l ; r = ', l, r)
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                print('左边界小等于中位数', mid)
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                print('左边界不小等中位数', mid)
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
            print('遍历 l ; r', l, r)

        return False

obj = Solution()
print(obj.search([2,5,6,0,0,1,2], 2))
