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
        self.visited = False  # Прапорець, щоб відстежувати відвідування вузла

    def set_color(self, color):
        self.color = color

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

def depth_first_traversal(node, color_generator, total_nodes):
    if node is None:
        return

    if not node.visited:
        node.visited = True
        color = next(color_generator)
        node.set_color(color)
        depth_first_traversal(node.left, color_generator, total_nodes)
        depth_first_traversal(node.right, color_generator, total_nodes)
    # Позначаємо, що вузол був відвіданий, щоб забезпечити коректну роботу інших алгоритмів
    node.visited = False

def breadth_first_traversal(root, color_generator, total_nodes):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node.visited:
            node.visited = True
            color = next(color_generator)
            node.set_color(color)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    # Позначаємо, що вузол був відвіданий, щоб забезпечити коректну роботу інших алгоритмів
    node.visited = False

def generate_color(step, total_steps):
    base_color = [135, 206, 250]  # блакитний (light blue) у форматі RGB
    lighten_factor = (step + 4) / (total_steps + 4) # Наскільки світлішим має бути кожен наступний вузол
    new_color = [int(c * lighten_factor) for c in base_color]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'

def draw_heap(heap_root, title):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

# Приклад використання:
array = [9, 4, 7, 2, 5, 8, 3, 1, 6]
min_heap_root = build_min_heap(array)

total_nodes = len(array)
color_generator = (generate_color(step, total_nodes) for step in range(total_nodes))
depth_first_traversal(min_heap_root, color_generator, total_nodes)
draw_heap(min_heap_root, 'Depth-First Traversal')

# Скидання прапорців visited для наступного обходу
min_heap_root.visited = False

color_generator = (generate_color(step, total_nodes) for step in range(total_nodes))
breadth_first_traversal(min_heap_root, color_generator, total_nodes)
draw_heap(min_heap_root, 'Breadth-First Traversal')