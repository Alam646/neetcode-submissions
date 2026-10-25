class Solution:

    def encode(self, strs: List[str]) -> str:
        mainlist = ""
        for x in range(len(strs)):
            length = len(strs[x])
            mainlist += str(length)
            mainlist += "."
            mainlist += strs[x]
        
        print(mainlist)
        return mainlist


    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0
        while i < len(s):
            j = i
            
            while s[j] != ".":
                j += 1
            
            length_str = s[i:j]
            len_int = int(length_str)

            word = s[j+1:len_int + j + 1]
            decoded.append(word)


            i = len_int + j + 1

        return decoded


            