class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        temp_ind = []

        for x in range(len(temperatures)):
            while temp_ind and temperatures[x] > temp_ind[-1][0]:
                rem_list = temp_ind.pop()
                ind = rem_list[-1]
                res_ind = x - ind
                res[ind] = res_ind
            
            temp_ind.append([temperatures[x],x])
        
        return res