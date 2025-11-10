import igraph as ig

# Load the graph
G = ig.Graph.Read_GraphML("retweet_network.graphml")
G_undirected = G.as_undirected(combine_edges=None)

print("Original directed edges:", G.ecount())
print("Undirected edges (with duplicates kept):", G_undirected.ecount())

print("Number of nodes:", G_undirected.vcount())
print("Number of edges:", G_undirected.ecount())
print("Is directed?", G_undirected.is_directed())

# Print first 5 vertices with attributes
for v in G_undirected.vs[:5]:
    print(v.index, v.attributes())

# Print first 5 edges with attributes
for e in G_undirected.es[:5]:
    print(e.source, e.target, e.attributes())