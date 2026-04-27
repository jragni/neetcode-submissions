"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        
        i = 0
        while i < len(sorted_intervals) - 1:
            meeting1 = sorted_intervals[i]
            meeting2 = sorted_intervals[i+1]

            print(meeting1.start, meeting2.start, meeting1.end, i )
            if meeting1.start <= meeting2.start and meeting2.start < meeting1.end:
                return False
            
            i += 1
        return True
            

