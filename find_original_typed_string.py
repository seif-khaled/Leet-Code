class Solution:
    def possibleStringCount(self, word: str) -> int:
        initial_counter=1
        last_letter=False
        for i in range(len(word)):
            if last_letter == False or last_letter != word[i]:
                last_letter=word[i]
            elif last_letter == word[i]:
                initial_counter+=1
        return initial_counter
        