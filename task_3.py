import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node].append((to_node, weight))

def visualize_graph(graph):
    G = nx.Graph()

    for node, edges in graph.edges.items():
        for edge in edges:
            G.add_edge(node, edge[0], weight=edge[1])

    pos = nx.spring_layout(G)
    labels = {node: node for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=1500, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

def dijkstra(graph, start):
    # Ініціалізуємо словник для зберігання найкоротших відстаней
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    # Ініціалізуємо бінарну купу (піраміду) для зберігання вершин та їх відстаней
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Якщо поточна відстань до вершини більша за раніше обчислену, пропускаємо
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            # Якщо нова відстань до сусідньої вершини менша за раніше обчислену, оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('D', 'E', 7)

    visualize_graph(graph)

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Найкоротші відстані від вершини", start_node)
    for node, distance in shortest_distances.items():
        print("Вершина:", node, "- Відстань:", distance)