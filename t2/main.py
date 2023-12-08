import networkx as nx
import matplotlib.pyplot as plt
import random

def erdos_renyi_graph(n, p):
    """
    Generates an Erdős-Rényi random graph with n nodes and edge probability p.
    """
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
        for j in range(i+1, n):
            if random.random() < p:
                G.add_edge(i, j)
    return G

# Parameters
num_nodes = 40
edge_prob = 0.8

# Generate the random graph
random_graph = erdos_renyi_graph(num_nodes, edge_prob)

# Visualization
plt.figure(figsize=(16, 12))
nx.draw(random_graph, with_labels=True, node_color='skyblue', font_weight='bold', node_size=500)
plt.title('Erdős-Rényi Random Graph')
plt.show()

# Basic graph statistics
print("Number of nodes:", random_graph.number_of_nodes())
print("Number of edges:", random_graph.number_of_edges())
print("Average clustering coefficient:", nx.average_clustering(random_graph))
print("Average shortest path length:", nx.average_shortest_path_length(random_graph))
