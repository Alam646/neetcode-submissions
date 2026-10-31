class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []

        # or this works too: pairs = list(zip(position, speed))
        for x in range(len(position)):
            pairs.append([position[x],speed[x]])


        pairs.sort(reverse=True)


        timestack = []
        for x in range(len(pairs)):
            time = (target - pairs[x][0]) / pairs[x][1]
            timestack.append(time)
            if len(timestack) >= 2:
                if timestack[-1] <= timestack[-2]:
                    timestack.pop()
        
        return len(timestack)