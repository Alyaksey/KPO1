import os
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def create_hist(G):
    counts = []
    counts.append(len([x for x in G.nodes if G.degree(x) == 1]))
    counts.append(len([x for x in G.nodes if G.degree(x) == 2]))
    counts.append(len([x for x in G.nodes if G.degree(x) == 3]))
    x = range(len(counts))
    ax = plt.gca()
    ax.bar(x, counts, align='edge')
    ax.set_xticks(x)
    ax.set_xticklabels(('0', '1', '2'))
    plt.show()


class Node(object):

    def __init__(self, number: int, parent_number: int):
        self.number = number
        self.parent_number = parent_number
        self.childrens = []

    def add_childrens(self, node):
        self.childrens.append(node)

    def __str__(self):
        return "{}-{}".format(self.number, self.parent_number)

    def is_leaf(self):
        return len(self.childrens) == 0


class Level(object):

    def __init__(self, number: int):
        self.number = number
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def has_nodes(self):
        return len(self.nodes) > 0


class Tree(object):
    def __init__(self, childs_count, nodes_count, is_random=True):
        self.nodes_count = nodes_count
        self.childs_count = childs_count
        self.is_random = is_random
        self.levels = []
        self.graph = nx.Graph()
        self.nodes_table = []
        self.leafs_table = []
        self.alpha = 0
        self.average_nodes = 0

    def add_level(self, level: Level):
        self.levels.append(level)

    def generate_child_number(self, start: int):
        if self.is_random:
            return random.randint(start, self.childs_count)
        else:
            return self.childs_count

    def create(self):
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        current_nodes_count = 1
        current_parent_node = Node(1, 0)
        current_parent_node.add_childrens(Node(2, 1))
        self.levels.append(Level(0))
        self.levels[0].add_node(current_parent_node)
        self.graph.add_node(current_parent_node.__str__())
        current_level_count = 0
        is_created = False
        while current_nodes_count < self.nodes_count:
            for node in self.levels[current_level_count].nodes:
                if current_nodes_count == 1:
                    current_child_number = self.generate_child_number(1)
                else:
                    current_child_number = self.generate_child_number(0)
                if not is_created:
                    is_created = True
                    current_level_count += 1
                    self.levels.append(Level(1))
                for i in range(current_child_number):
                    current_nodes_count += 1
                    new_node = Node(current_nodes_count, node.number)
                    self.levels[current_level_count].add_node(new_node)
                    self.graph.add_node(new_node.__str__())
                    self.graph.add_edge(node.__str__(), new_node.__str__())
                    if current_nodes_count == self.nodes_count:
                        break
                if current_nodes_count == self.nodes_count:
                    break
            is_created = False
            if not self.levels[current_level_count].has_nodes():
                current_level_count -= 1
        self.nodes_table = [x for x in self.graph.nodes]
        self.leafs_table = [x for x in self.graph.nodes if self.graph.degree(x) == 1 and x != "1-0"]
        counts = []
        counts.append(len([x for x in self.graph.nodes if self.graph.degree(x) == 1]))
        counts.append(len([x for x in self.graph.nodes if self.graph.degree(x) == 2]))
        counts.append(len([x for x in self.graph.nodes if self.graph.degree(x) == 3]))
        self.average_nodes = np.mean(counts)
        self.alpha = len(self.nodes_table) / len(self.leafs_table)

    def draw_graph(self):
        p = nx.drawing.nx_pydot.to_pydot(self.graph)
        p.write_png("example.png")

    def create_hist(self):
        counts = []
        counts.append(len([x for x in self.graph.nodes if self.graph.degree(x) == 1 and x != "1-0"]))
        counts.append(len([x for x in self.graph.nodes if self.graph.degree(x) == 2]))
        counts.append(len([x for x in self.graph.nodes if self.graph.degree(x) == 3]))
        x = range(len(counts))
        ax = plt.gca()
        ax.bar(x, counts, align='edge')
        ax.set_xticks(x)
        ax.set_xticklabels(('0', '1', '2'))
        plt.show()
