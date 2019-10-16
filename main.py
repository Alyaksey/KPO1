import random

import tree as tr
import numpy as np

tree = tr.Tree(2,100,True)
tree.create()
tree.draw_graph()
tree.create_hist()
print("Таблица вершин")
print(tree.nodes_table)
print("Таблица висячих вершин")
print(tree.leafs_table)
print("Мат. ожидание числа исходящих из узла ребер из этой гистограммы")
print(tree.average_nodes)
print("Среднее альфа")
print(tree.alpha)
alphas = []
node_counts = []
leafs_counts = []
height_counts = []
for i in range(400):
    tree = tr.Tree(2,100,True)
    tree.create()
    alphas.append(tree.alpha)
    node_counts.append(len(tree.nodes_table))
    leafs_counts.append(len(tree.leafs_table))
    height_counts.append(len(tree.levels))
