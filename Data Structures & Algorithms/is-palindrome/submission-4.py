class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'

        while left < right:
            l_string = s[left].lower()
            r_string = s[right].lower()

            if not l_string in alphanumeric:
                left += 1
            elif not r_string in alphanumeric:
                right -= 1
            else:
                if l_string != r_string:
                    return False
                else:
                    left += 1
                    right -= 1
        return True