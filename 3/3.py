class Node:
    def __init__(self, _value):
        self.value = _value
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self, _N):
        self.N = _N
        self.nodes = [0]
        for i in range(1, self.N + 1):
            node = Node(i)
            parent = i // 2
            if parent > 0:
                node.parent = self.nodes[parent]
                if self.nodes[parent].left is None:
                    self.nodes[parent].left = i
                else:
                    self.nodes[parent].right = i
            self.nodes.append(node)

    def in_order(self, v):
        if self.nodes[v].left:
            self.in_order(self.nodes[v].left)
        print(self.nodes[v].value)
        if self.nodes[v].right:
            self.in_order(self.nodes[v].right)

    def swap(self, v):
        pass
        # p = nodes[v].parent
        # pp = nodes[p].parent
        # if nodes[pp].left == p: # p — левый ребенок вершины pp, то 
        #     v становится левым ребенком pp
        # else:
        #     v становится правым ребенком pp
        # if nodes[p].left == v: #v — левый ребенок вершины p , то
        #     nodes[v].left = p #p становится левым ребенком v ;
        #     # vr остаётся правым ребенком v;
        #     nodes[p].left = nodes[v].left # vl становится левым ребенком p ;
        #     nodes[v].left = None # vl становится левым ребенком p ;
        #     # pr остаётся правым ребенком p
        # else:
        #     nodes[v].right = p# p становится правым ребенком v;
        #     # vl остаётся левым ребенком v;
        #     nodes[p].right = nodes[v].right# vr становится правым ребенком p;
        #     nodes[v].right = None
        #     # pl остаётся левым ребенком p

N, _ = map(int, input().split(' '))
tree = Tree(N)
tree.in_order(1)
# swaps = list(map(int, input().split(' ')))
# for swp in swap:
#     tree.swap(swp)
