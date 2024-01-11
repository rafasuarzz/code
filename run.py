# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
grafo = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Craiova': [('Pitesti', 138), ('Rimnicu Vilcea', 146), ('Drobeta', 120)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Sibiu', 80), ('Craiova', 146)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Pitesti': [('Bucharest', 101), ('Rimnicu Vilcea', 97), ('Craiova', 138)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211)]
}
print(search.depth_first_graph_search(ab).path())
print(search.breadth_first_graph_search(ab).path())
print(search.ramificacion_acotacion(ab).path())
print(search.Heuristica(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
