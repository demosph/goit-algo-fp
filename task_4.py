import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.parent = None
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_min_heap(array):
    if not array:
        return None
    array.sort()  # Сортування масиву для визначення мінімального значення
    root = Node(array[0])
    queue = [root]
    for i in range(1, len(array)):
        parent = queue[0]
        new_node = Node(array[i])
        new_node.parent = parent
        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node
            queue.pop(0)
        queue.append(new_node)
        while parent.parent and new_node.val < parent.val:
            new_node.val, parent.val = parent.val, new_node.val
            new_node = parent
            parent = parent.parent
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання:
array = [9, 4, 7, 2, 5, 8, 3, 1, 6]
min_heap_root = build_min_heap(array)
draw_heap(min_heap_root)
