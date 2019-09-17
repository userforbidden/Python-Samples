import heapq

def meetingRoom(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key = lambda x:x[0])

    free_rooms = []

    heapq.heappush(free_rooms,intervals[0][1])

    for i in intervals[1:]:
        if i[0] >= free_rooms[0]:
            heapq.heappop(free_rooms)
        
        heapq.heappush(free_rooms,i[1])

    print(len(free_rooms))


intervals = [[0, 30],[5, 10],[15, 20],[2,7],[5,15],[10,45]]
meetingRoom(intervals)
