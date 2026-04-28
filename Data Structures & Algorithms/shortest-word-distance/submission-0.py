class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_poses = []
        word2_poses = []
        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                word1_poses.append(i)
            if word2 == wordsDict[i]:
                word2_poses.append(i)
            
        delta = float('inf')
        for p1 in word1_poses:
            for p2 in word2_poses:
               delta = min(delta, abs(p1 - p2))
        
        return int(delta)
