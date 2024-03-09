from collections import namedtuple # nametupled 사용

QueueElement = namedtuple("QueueElement", ["node", "height"])

class Node:
    def __init__(self, name):
        self.name       = name
        self.parent     = None
        self.children   = []


def compute_height(n, parents):
    max_height      = 1
    node_list       = []
    node_queue      = []
    root_node       = None
  
    for i in range(n):
        node_list.append(Node(i))

    for i, parent_index in enumerate(parents):
        if parent_index != -1:
            node_list[i].parent = node_list[parent_index]
            node_list[parent_index].children.append(node_list[i])
        else:
            root_node = node_list[i]

    node_queue = [QueueElement(root_node, 1)]


    for node in node_list:
        children_str = []
        for child in node.children:
            children_str.append(str(child.name))
        # print(node.name, "children", ",".join(children_str))

    while len(node_queue) > 0:
        node_tuple = node_queue.pop()
        
        for child_node in node_tuple.node.children:
            node_queue.append(QueueElement(child_node, node_tuple.height+1))
            max_height = max(max_height, node_tuple.height+1)

    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == "__main__":
    main()
