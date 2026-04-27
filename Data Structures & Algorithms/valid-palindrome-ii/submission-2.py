class Solution:
    def validPalindrome(self, s: str) -> bool:
        can_delete = True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if can_delete:
                    can_delete = False
                    # try move right over
                    right -= 1
                    if s[left] == s[right]:
                        continue
                    # try left
                    right += 1
                    left += 1
                    if s[left] == s[right]:
                        continue
                    else:
                        return False
                else:
                    return False
            left += 1
            right -= 1
        return True
                    