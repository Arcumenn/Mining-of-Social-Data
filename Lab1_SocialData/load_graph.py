import igraph as ig

# Load the graph
G = ig.Graph.Read_GraphML("reply_network.graphml")
# currently 'process_tweets' saves a directed graph; thus it is converted here
G_undirected = G.as_undirected(combine_edges=None)

# Print first 5 vertices with attributes
for v in G_undirected.vs[:5]:
    print(v.index, v.attributes())

# Print first 5 edges with attributes
for e in G_undirected.es[:5]:
    print(e.source, e.target, e.attributes())
