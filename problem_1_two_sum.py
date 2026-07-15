from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {0: nums[0]}

    for i in range(1, len(nums) - 1):
        print(f"index: {i}")
        print(seen)
        current_value = nums[i]
        complement = target - current_value

        if complement in seen.values():
            print(f"entered on index {i}")
            keys = [key for key, val in seen.items() if val == complement]
            return [keys[0], i]

        seen[i] = nums[i]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    result = twoSum(nums=nums, target=target)
    print(result)
