class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, 0
        min_count = math.inf
        curr = 0

        while right < len(blocks):
            # build window
            while right - left + 1 <= k:
                if blocks[right] == "W":
                    curr += 1
                right += 1

            # check for min
            min_count = min(curr, min_count)
            # slide left and update curr
            if blocks[left] == "W":
                curr -= 1
            left += 1
        
        
        return min_count
                    