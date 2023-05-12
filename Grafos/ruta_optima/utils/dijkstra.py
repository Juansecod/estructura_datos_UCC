from queue import PriorityQueue
from math import inf
import networkx as nx

def dijkstra(start, end, graph):
    def backtrace(prev, start, end):
        node = end
        path = []
        while node != start:
            path.append(node)
            node = prev[node]
        path.append(node)
        path.reverse()
        return path

    def cost(u, v):
        return graph.get_edge_data(u,v).get('weight')
    
    prev = {} 
    dist = {v: inf for v in list(nx.nodes(graph))} 
    visited = set() 
    pq = PriorityQueue()  
    dist[start] = 0 
    pq.put((dist[start], start))
    
    while 0 != pq.qsize():
        curr_cost, curr = pq.get()
        visited.add(curr)
        for neighbor in dict(graph.adjacency()).get(curr):
            path = dist[curr] + cost(curr, neighbor)
            if path < dist[neighbor]:
                dist[neighbor] = path
                prev[neighbor] = curr
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    pq.put((dist[neighbor],neighbor))
                else:
                    _ = pq.get((dist[neighbor],neighbor))
                    pq.put((dist[neighbor],neighbor))

    return backtrace(prev, start, end), dist[end]