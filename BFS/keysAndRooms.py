# https://leetcode.com/problems/keys-and-rooms/description/

def canVisitAllRooms(rooms):
    roomsLen = len(rooms)
    visited = [False]*roomsLen

    def dfs(roomNum):
        if False not in visited:
            return True

        for key in rooms[roomNum]:
            if not visited[key]:
                visited[key] = True
                if dfs(key):
                    return True
        return False
    visited[0] = True
    return dfs(0)



print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
