class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        visited_rooms.add(0)
        stack = [0]

        while stack :
            room = stack.pop()
            visited_rooms.add(room)
            for key in rooms[room]:
                if key not in visited_rooms:
                    stack.append(key)
        return len(visited_rooms) == len(rooms)