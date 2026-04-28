class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        delta = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            elif wordsDict[i] == word2:
                p2 = i
            
            if p1 != -1 and p2 != -1:
                delta = min(abs(p1 - p2), delta)
            
            print(f'p1: {p1}, p2: {p2}, delta: {delta}')

        return delta
