# Problem: Find the area of the largest rectangle that can be formed within a histogram.
# Core Pattern: Monotonic Increasing Stack + Index Stealing
# Key Intuition: A bar can stretch left and right as long as adjacent bars are the same height or taller. Use a stack as a waiting room to track bars [height, start_index] that haven't found their right-side wall yet. 
# When a shorter bar arrives, it acts as a right-side wall. The taller bars in the stack are trapped, so you pop them and calculate their maximum area using today's index as the right wall limit. 
# Crucially, the shorter bar "steals" the starting index of the taller bars it just popped. It can do this because a short rectangle can safely stretch backwards through the exact space the taller bars were occupying.
# After processing all bars, any survivors left in the stack never hit a wall, so their right wall is the very end of the array (len(heights)).

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Track the absolute maximum area found so far
        max_area = 0

        # The "waiting room". Stores pairs of [height, starting_index].
        # Bars sit here while they are actively stretching to the right.
        stack = []

        for x in range(len(heights)):   
            # 1. Default assumption: This bar starts exactly at its own index.
            start = x
            
            # 2. The Graveyard (The while loop):
            # If the current bar is shorter than the bar at the top of the stack, 
            # it acts as a solid brick wall. The taller bar cannot stretch any further.
            while stack and heights[x] <= stack[-1][0]:
                
                # Pull the trapped taller bar out of the stack
                start_height, start_ind = stack.pop()
                
                # Calculate its final area. 
                # Width = (Today's index 'x' acting as the right wall) - (The bar's original starting index)
                area = start_height * (x - start_ind)
                
                # Update our all-time max area if this rectangle is bigger
                max_area = max(max_area, area)
                
                # 3. Index Stealing: 
                # Because the current bar is shorter, it can physically slide backwards 
                # through the empty space left by the tall bar we just destroyed. 
                # We steal its starting index so our short bar remembers how far back it stretches.
                start = start_ind
            
            # 4. The Push:
            # Add today's bar to the waiting room. If it stole an index in the while loop, 
            # 'start' will be that stolen index. Otherwise, it's just 'x'.
            stack.append([heights[x], start])

        # 5. The Cleanup Loop (The Survivors):
        # The array is completely finished. Any bars still sitting in the stack 
        # successfully stretched all the way to the absolute end of the array without hitting a wall.
        for x in range(len(stack)):
            start_height, start_ind = stack.pop()
            
            # Their right wall is the very edge of the screen, which is len(heights).
            area = start_height * (len(heights) - start_ind)
            max_area = max(max_area, area)
            
        return max_area