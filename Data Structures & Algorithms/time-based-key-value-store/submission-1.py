# Problem: Design a time-based key-value store. For a given key, retrieve the value at a specific time, 
# or the closest value that occurred BEFORE that time.
# Core Pattern: Dictionary of Arrays + Binary Search ("Best so far" tracking).
# Key Intuition: Because the problem guarantees timestamps are strictly increasing, simply appending 
# new values to a list naturally creates a perfectly sorted array in O(1) time. This perfectly sorted 
# array unlocks O(log n) Binary Search. If we find a time from the past (mid < target), we save it 
# as our "best so far" (res) and keep searching the right half to see if we can get even closer.

class TimeMap:

    def __init__(self):
        # Dictionary to store key -> list of [timestamp, value] pairs
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist yet, initialize an empty list for it
        if key not in self.timemap:
            self.timemap[key] = []
            
        # O(1) append. Since timestamps are given in strictly increasing order,
        # this naturally keeps the array perfectly sorted for Binary Search.
        self.timemap[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        # If we have no history of this key, return an empty string
        if key not in self.timemap: 
            return ""

        left = 0
        right = len(self.timemap[key]) - 1
        res = "" # Tracks our "closest past value so far"

        while left <= right:
            mid = (right + left) // 2
            mid_time = self.timemap[key][mid][0]
            mid_val = self.timemap[key][mid][1]

            # Instant win: exact time match
            if mid_time == timestamp:
                return mid_val
            
            # The mid time is in the past. This is a valid answer!
            # Save it, but search the right half to see if we can get closer.
            elif mid_time < timestamp:
                res = mid_val
                left = mid + 1
                
            # The mid time is in the future. We haven't reached this state yet.
            # It's invalid. Throw away the right half and search the past.
            else:
                right = mid - 1
        
        # Returns either the closest past value, or "" if all times were in the future
        return res