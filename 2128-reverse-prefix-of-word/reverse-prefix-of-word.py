class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result=""
        for i in range(len(word)):
            if word[i]==ch:
                text=word[:i+1]
                result=text[::-1]+""+word[i+1:]
                break
            else:
                result=word
        return result          
        