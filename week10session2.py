from collections import deque

def can_rebook(flights, source, dest): # BFS
    if source == dest:
        return True
    
    queue = deque([source])
    visited = [False] * len(flights)
    # print(len(flights))
    visited[source] = True


    while queue:
        curr = queue.popleft()

        for neighbor in range(len(flights[curr])):
            # print(len(flights[curr]))
            if flights[curr][neighbor] == 1 and not visited[neighbor]:
                if neighbor == dest:
                    return True
                queue.append(neighbor)
                visited[neighbor] = True
    return False



    

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# print(can_rebook(flights1, 0, 2))
# print(can_rebook(flights2, 0, 2)) 


def can_rebook(flights, source, dest): # DFS
    visited = [False] * len(flights)
    def dfs(curr):
        if curr == dest:
            return True
        
        visited[curr] = True

        for neighbor in range(len(flights[curr])):
            if flights[curr][neighbor] == 1 and not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False
    return dfs(source)

# print(can_rebook(flights1, 0, 2))
# print(can_rebook(flights2, 0, 2)) 


def counting_flights(flights, i, j):
    pass
