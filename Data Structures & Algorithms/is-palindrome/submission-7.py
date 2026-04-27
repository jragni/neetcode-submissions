class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            # check if alpha
            r_lower = s[right].lower()
            l_lower = s[left].lower()
            if not l_lower.isalnum():
                left += 1
                continue

            if not r_lower.isalnum():
                right -= 1
                continue
            
            
            if r_lower != l_lower:
                return False
            
            left += 1
            right -= 1

        return True