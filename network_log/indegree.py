import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def read_graph_from_csv(csv_file_path):
    # Load CSV into DataFrame
    df = pd.read_csv(csv_file_path)

    # Create directed graph from DataFrame
    G = nx.from_pandas_edgelist(df, 'sources', 'destinations', create_using=nx.DiGraph())

    return G


def draw_graph(G):
    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for visualizing the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)
    plt.title("Directed Graph")
    plt.show()


def print_adjacency_matrix(G):
    # Print the adjacency matrix
    A = nx.adjacency_matrix(G)
    print("Adjacency Matrix:\n", A.todense())


def recursively_investigate_in_degree_chain(G, vertex, visited=None):
    if visited is None:
        visited = set()

    # Avoid revisiting nodes
    if vertex in visited:
        return
    visited.add(vertex)

    # Get the in-degree vertices (predecessors)
    in_degree_vertices = list(G.predecessors(vertex))

    if not in_degree_vertices:
        print(f"Vertex {vertex} has no incoming edges.")
    else:
        print(f"Vertices leading to {vertex}: {in_degree_vertices}")

    # Recursive call for each predecessor
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
    # Replace 'path_to_your_csv.csv' with your actual CSV file path
    csv_file_path = 'srcdes.csv'

    # Read and build graph
    G = read_graph_from_csv(csv_file_path)

    # Draw the graph
    #draw_graph(G)

    # Print the adjacency matrix
    #print_adjacency_matrix(G)

    # User input for investigating a vertex
    # vertex = input("Enter the vertex to start the in-degree investigation: ")
    vertex = "192.168.10.45"

    #print(f"Starting in-degree investigation from vertex {vertex}:")
    #recursively_investigate_in_degree_chain(G, vertex)

    print(f"Starting out-degree investigation from vertex {vertex}:")
    recursively_investigate_out_degree_chain(G, vertex)


if __name__ == "__main__":
    main()
