class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist yet, create an empty list for it
        if key not in self.timemap:
            self.timemap[key] = []
            
        self.timemap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap: 
            return ""

        left = 0
        right = len(self.timemap[key]) - 1
        res = ""

        while left <= right:
            mid = (right + left) // 2
            if self.timemap[key][mid][0] == timestamp:
                return self.timemap[key][mid][1]
            elif self.timemap[key][mid][0] < timestamp:
                res = self.timemap[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res