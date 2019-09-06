import heapq
#Definition for Interval
class Interval(object):
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self,intervals):
        if not intervals:
            return 0
        
          
        used_rooms = 0

        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])
        s_ptr, e_ptr = 0,0 
        
        L = len(intervals)

        while s_ptr < L:
            if start_times[s_ptr] >= end_times[e_ptr]:
                e_ptr += 1
                used_rooms -= 1
            used_rooms += 1
            s_ptr += 1

        return used_rooms 
        
        

""" The Heap Approach 
        #the heap intialization
        free_rooms = []
        # Sort the meetings in increasing order of their start time.
        intervals.sort(key =lambda x:x.start)
        # print(intervals)
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms,intervals[0].end)
        # For all the remaining meeting rooms
        for i in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms,i.end)
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms) """


intervals= [Interval(1, 10), Interval(11, 30), Interval(3, 19), Interval(2, 7), Interval(8, 12), Interval(10, 20)]

print(Solution().minMeetingRooms(intervals))