import networkx as nx
import matplotlib.pyplot as plt

#
# #1
#

transport_network = nx.Graph()
transport_network.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
transport_network.add_edges_from([
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "F"), ("E", "F"),
    ("C", "G"), ("D", "G"), ("E", "H"), ("F", "I"), ("I", "K"), ("B", "J"), ("G", "K")
])

# Visualize
nx.draw(transport_network, with_labels=True, node_color='lightpink', node_size=1000, pos=nx.spring_layout(G))
plt.title("Public Transport Network")
plt.show()

# Analyze the updated graph
print("Number of nodes:", transport_network.number_of_nodes())
print("Number of edges:", transport_network.number_of_edges())
print("Degree of each node:", dict(transport_network.degree()))

#
# #2
#

def dfs(graph, start, path=None):
    if path is None:
        path = []
    path.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            dfs(graph, neighbor, path)
    return path

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(n for n in graph.neighbors(node) if n not in visited)
    return visited

# Execute DFS and BFS
dfs_path = dfs(transport_network, 'A')
bfs_path = bfs(transport_network, 'A')

print("DFS:", dfs_path)
print("BFS:", bfs_path)

print("DFS досліджує якомога глибше кожний вузол, перш ніж повернутися назад."
+ "\nЦе означає, що, обираючи нову вершину, алгоритм переходить до неї і продовжує досліджувати далі, доки це можливо.")
print("BFS досліджує всі вузли на поточному рівні перед переходом на наступний. Це створює ефект рівновіддаленості, де кожен "
+ "\nвузол на даній відстані опрацьовується перед переходом до дальшої відстані.")

#
# #3
#

transport_network.add_weighted_edges_from([
    ("A", "B", 2), ("A", "C", 1), ("B", "D", 5), ("C", "D", 2), ("C", "E", 3), ("D", "F", 1), 
    ("C", "G", 2), ("D", "G", 3), ("E", "H", 2), ("F", "I", 4), ("I", "K", 1), ("B", "J", 3), ("G", "K", 2),
    ("E", "F", 1)
])

def dijkstra(graph, start):
    return nx.single_source_dijkstra_path(graph, start)

# Shortest paths from 'A'
shortest_paths = dijkstra(transport_network, 'A')
print("Shortest paths from 'A':", shortest_paths)

# Visualize
edge_labels = nx.get_edge_attributes(transport_network, 'weight')
pos = nx.spring_layout(transport_network)

nx.draw(transport_network, pos, with_labels=True, node_color='lightgreen', node_size=1000)
nx.draw_networkx_edge_labels(transport_network, pos, edge_labels=edge_labels)

plt.title("Weighted Public Transport Network")
plt.show()