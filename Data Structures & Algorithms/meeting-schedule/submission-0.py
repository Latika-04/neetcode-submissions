"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by their start time
        intervals.sort(key=lambda i: i.start)
        
        # Check for overlaps between adjacent intervals
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            
            # If the current meeting starts before the previous one ends, there's a conflict
            if i2.start < i1.end:
                return False
                
        return True