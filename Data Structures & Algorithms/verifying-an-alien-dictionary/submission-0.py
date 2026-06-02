class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        j = 1
        while j < len(words):
            word1 = words[j-1]
            word2 = words[j]
            is_checked = False

            for i in range(len(word1)):
                if is_checked:
                    break

                if i == len(word2):
                    return False

                if word1[i] != word2[i]:
                    char1_index = order.index(word1[i])
                    char2_index = order.index(word2[i])

                    if char1_index > char2_index:
                        return False
                    
                    is_checked = True
                    break
            
            j += 1
        
        return True