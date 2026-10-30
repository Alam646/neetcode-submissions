# Problem: Find the distance in days to the next warmer temperature.
# Core Pattern: Monotonic Decreasing Stack (The "Waiting Room")
# Key Intuition: Instead of scanning forward to find a warmer day (O(N^2)), use a stack to store past days that are still waiting for a warmer temperature. As we iterate, if today is hotter than the day at the top of the stack, today is the answer that past day was waiting for. We use a while loop because a single hot day might resolve multiple past cold days at once.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Initialize results with 0s. If a day never finds a warmer future day, 
        # it correctly defaults to 0 (no extra work needed at the end).
        res = [0] * len(temperatures)

        # The waiting room stack. Will store pairs: [temperature, index]
        # It naturally stays sorted from hottest (bottom) to coldest (top).
        temp_ind = []

        for x in range(len(temperatures)):
            
            # Chain Reaction: While the stack has waiting days, and TODAY'S temp 
            # is hotter than the waiting day at the top of the stack...
            while temp_ind and temperatures[x] > temp_ind[-1][0]:
                
                # ...resolve that past day! Pop it from the waiting room.
                rem_list = temp_ind.pop()
                ind = rem_list[-1] # Extract the past day's original index
                
                # The distance in days is simply Today's index (x) - Past day's index (ind)
                res_ind = x - ind
                
                # Save the answer at the PAST day's position in the results array
                res[ind] = res_ind
            
            # After resolving any past days we could, today must now enter the 
            # waiting room to wait for its own warmer future day.
            temp_ind.append([temperatures[x], x])
        
        return res