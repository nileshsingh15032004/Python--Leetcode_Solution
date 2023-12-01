from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []  # Initialize an empty list to store the result
        carry = 1  # Initialize carry to 1 as we are adding one to the number

        for i in reversed(digits):
            # Add the current digit, carry, and update the carry
            total = i + carry
            ans.append(total % 10)
            carry = total // 10

        # If there is still a carry after the loop, add it as a new digit
        if carry:
            ans.append(carry)

        # Reverse the result list to get the correct order
        return ans[::-1]
