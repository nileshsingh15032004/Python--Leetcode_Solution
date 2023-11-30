from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement] + 1, i + 1]  # Indices are 1-based

            num_dict[num] = i

        return []
