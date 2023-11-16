import networkx as nx
import pandas as pd

df = pd.read_csv('sni.csv')

G = nx.from_pandas_edgelist(df, source='Source', target='Target', create_using=nx.DiGraph())

num_nodes = len(G.nodes())
num_edges = len(G.edges())

avg_degree = 2 * num_edges / num_nodes

top_node = max(G.degree, key=lambda x: x[1])

strongly_connected_components = list(nx.strongly_connected_components(G))
num_strongly_connected = len(strongly_connected_components)

weakly_connected_components = list(nx.weakly_connected_components(G))
num_weakly_connected = len(weakly_connected_components)

clustering_coefficient = nx.average_clustering(G)

num_components = len(list(nx.connected_components(G.to_undirected())))

density = nx.density(G)

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Average degree: {avg_degree}")
print(f"Top node: {top_node[0]} (Degree: {top_node[1]})")
print(f"Number of strongly connected components: {num_strongly_connected}")
print(f"Number of weakly connected components: {num_weakly_connected}")
print(f"Clustering coefficient: {clustering_coefficient}")
print(f"Number of components: {num_components}")
print(f"Network density: {density}")
