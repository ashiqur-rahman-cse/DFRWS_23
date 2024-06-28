import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def uppercase(x):
    return x.upper()
def read_graph_from_csv(csv_file_path):
    #df = pd.read_csv(csv_file_path)
    df = pd.read_csv(csv_file_path, converters={'sources': uppercase, 'destinations': uppercase})
    G = nx.from_pandas_edgelist(df, 'sources', 'destinations', create_using=nx.DiGraph())
    return G

def draw_graph(G):
    pos = nx.spring_layout(G)  # Layout for visualizing the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)
    plt.title("Directed Graph")
    plt.show()

def print_adjacency_matrix(G):
    A = nx.adjacency_matrix(G)
    print("Adjacency Matrix:\n", A.todense())

def recursively_investigate_in_degree_chain(G, vertex, visited=None):
    if visited is None:
        visited = set()

    if vertex in visited:
        return

    visited.add(vertex)

    in_degree_vertices = list(G.predecessors(vertex))

    if not in_degree_vertices:
        print(f"Vertex {vertex} has no incoming edges.")
    else:
        print(f"Vertices leading to {vertex}: {in_degree_vertices}")

    for pred in in_degree_vertices:
        recursively_investigate_in_degree_chain(G, pred, visited)
def recursively_investigate_out_degree_chain(G, vertex, visited=None):
    if visited is None:
        visited = set()

    if vertex in visited:
        return

    visited.add(vertex)

    out_degree_vertices = list(G.successors(vertex))

    if not out_degree_vertices:
        print(f"Vertex {vertex} has no outgoing edges.")
    else:
        print(f"Vertices that {vertex} leads to: {out_degree_vertices}")

    for succ in out_degree_vertices:
        recursively_investigate_out_degree_chain(G, succ, visited)
def main():

    csv_file_path = 'srcdes.csv'
    G = read_graph_from_csv(csv_file_path)
    #draw_graph(G)
    #print_adjacency_matrix(G)

    #vertex = "192.168.10.241"
    vertex = "FE80:1B92:88FA:FD29:AFF6"

    print(f"Starting in-degree investigation from vertex {vertex}:")
    #recursively_investigate_in_degree_chain(G, vertex)

    #print(f"Starting out-degree investigation from vertex {vertex}:")
    recursively_investigate_out_degree_chain(G, vertex)

if __name__ == "__main__":
    main()