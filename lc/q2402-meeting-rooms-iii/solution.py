# You are given an integer n. There are n rooms numbered from 0 to n - 1.
# You are also given a list of meetings where meetings[i] = [starti, endi]
# represents the start and end times of the ith meeting.
# The start time of the ith meeting is meetings[i][0] and the end time of the ith meeting is meetings[i][1].
# All the values of start_i are unique.
# Meetings are allocated to rooms in the following way:

# Each meeting wil ltake place in the unique room with lowest number.
# If there are no available rooms, the meeting will be delayed until a room is available.
# When a room becomes unused, meetings that have an earlier start time will be scheduled in the room.


from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, num_rooms, meetings):
        available_rooms = [room for room in range(num_rooms)]
        heapify(available_rooms)

        # ele: [end_time, room_number]
        occupied_rooms = []

        booking_counts = [0] * num_rooms

        # sort by start time
        sorted_meetings = sorted(meetings, key=lambda x: x[0])

        for start_time, end_time in sorted_meetings:

            # prepare all available rooms for the current meeting
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                _, room = heappop(occupied_rooms)
                heappush(available_rooms, room)

            # assign a room to the current meeting
            # bacause heappop(availble_rooms) will always popup the smallest room number
            if available_rooms:
                room = heappop(available_rooms)
                heappush(occupied_rooms, [end_time, room])

            # if there is no available room, we need to delay the meeting
            else:
                # we will always assign the room with the smallest end time
                current_end, room = heappop(occupied_rooms)
                new_end = (
                    current_end + end_time - start_time
                )  # Update the room's end time
                heappush(occupied_rooms, [new_end, room])

            # Q: is room defined in inner scope? should be room cleared by gc?
            booking_counts[room] += 1

        _max = -1
        max_index = -1

        for i in range(len(booking_counts)):
            if booking_counts[i] > _max:
                _max = booking_counts[i]
                max_index = i

        return max_index
