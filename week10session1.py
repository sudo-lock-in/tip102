class GraphNode:

  def __init__(self, value, edges = None):
      self.val = value
      if not edges:
          self.edges = []
      else:
          self.edges = edges

  def add_connection(self, new_node):
      self.edges.append(new_node)

# example
# adjacency_dictionary = {
#     "Mexico City": ["São Paulo", "Los Angeles"],
#     "Los Angeles": ["Mexico City", "Atlanta"],
#     "Atlanta": ["Los Angeles"],
#     "São Paulo": []
# }

flights = {
    'JFK': ['LAX', 'DFW'],
    'LAX': ['JFK'],
    'DFW': ['JFK', 'ATL'],
    'ATL': ['DFW']
}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])




def bidirectional_flights(flights):
    # n being the length of flights (flights has n nodes)
    #  each node represents the ID of a different destination 
    # and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]
    # so the index is the start and the value of the index is the destinations
    #  returns True if for every flight from a destination i to a destination j there also exists a flight from destination j to destination i
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:  # check if destination j has a flight back to i
                return False 
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))
    
def get_direct_flights(flights, source):
    direct = []
    for j in range(len(flights[source])):
        if flights[source][j] == 1:
            direct.append(j)
    return direct


flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))


def get_adj_dict(flights):
    d = {}
    for a, b in flights:
        if a not in d:
            d[a] = []
        d[a].append(b)
        if b not in d:
            d[b] = []
        d[b].append(a)
    return d
    
    
flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
# print(get_adj_dict(flights))


def find_center(terminals):
    d = {}
    for a, b in terminals:
        d[a] = d.get(a, 0) + 1
        d[b] = d.get(b, 0) + 1
        if d[b] > 1:
            return b
        if d[a] > 1:
            return a
        

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

# print(find_center(terminals1))
# print(find_center(terminals2))

from collections import deque


# BFS
def get_all_destinations(flights, start):
    queue = deque([start])
    visited = set([start])

    can_reach = []

    while queue:
        curr = queue.popleft()
        can_reach.append(curr)

        for neighbor in flights.get(curr, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return can_reach

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))



# DFS
def get_all_destinations(flights, start):
    visited = set()
    can_reach = []

    def dfs(location):
       can_reach.append(location)
       visited.add(location)
       for neighbor in flights.get(location, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
                
    return can_reach
  

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))


# One possible approach to this problem is to use a dictionary.

#     Create a dictionary that maps each deaprture airport to its corresponding arrival airport for efficient lookup.
#     Identify the starting airport. It is the only airport that is only a departure airport and never an arrival airport.
#     Trace the itinerary by following the mapping from departure to arrival until there are no more flights.

def find_itinerary(boarding_passes):
    flight_map = {}
    arrivals = set()
    itinerary = []

    for departure, arrival in boarding_passes:
        flight_map[departure] = arrival
        arrivals.add(arrival)

    start = None

    for departure, arrival in boarding_passes:
        if departure not in arrivals:
            start = departure
            break
    
    while start:
        itinerary.append(start)
        start = flight_map.get(start)
    return itinerary
    

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

# print(find_itinerary(boarding_passes_1))
# print(find_itinerary(boarding_passes_2))



