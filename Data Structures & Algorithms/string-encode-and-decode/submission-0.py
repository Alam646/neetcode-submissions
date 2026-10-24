class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            len_str = len(i)
            res += str(len_str) + "#" + i
        return res 


    def decode(self, s: str) -> List[str]:
        lst = []

        i = 0
        while i < len(s):
            j = s.find('#', i)
            len_str = s[i:j]
            int_len_str = int(len_str)
            i = j + 1 #where the string starts
            the_word = s[i:i+int_len_str]
            lst.append(the_word)
            i = i + int_len_str
        return lst
