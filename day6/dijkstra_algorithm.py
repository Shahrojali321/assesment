"""Defination: Program to implement Dijkstra’s Shortest Path algorithm on a graph"""

def dijkstra_algorithm(graph,current_distance,nodes):
    unvisited = {node: None for node in nodes} 
    visited = {}
    current = 'B'
    current_distance = 0
    unvisited[current] = current_distance
    """algorithm to find the shortest path"""
    while True:
        for neighbour, distance in graph[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key = lambda x: x[1])[0]

    return visited
    
""" creating graph and calling function"""
if __name__=='__main__':
    current_distance = 0
    graph = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    print(f"The shortest path is : {dijkstra_algorithm(graph,current_distance,nodes)}")