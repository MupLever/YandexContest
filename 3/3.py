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

    def pre_order(self, v):
        print(self.nodes[v].value)
        if self.nodes[v].left:
            self.pre_order(self.nodes[v].left)

        if self.nodes[v].right:
            self.pre_order(self.nodes[v].right)

    def swap(self, v):
        p = self.nodes[v].parent.value

        if self.nodes[p].parent is not None:
            pp = self.nodes[p].parent.value 
            if self.nodes[pp].left == p: # p — левый ребенок вершины pp, то 
                self.nodes[pp].left = v # v становится левым ребенком pp
                self.nodes[v].parent = pp
            else:
                self.nodes[pp].right = v # v становится правым ребенком pp
                self.nodes[v].parent = pp

        if self.nodes[p].left == v: #v — левый ребенок вершины p , то
            tmp = self.nodes[v].left
            self.nodes[v].left = p #p становится левым ребенком v ;
            self.nodes[p].parent = v
            # vr остаётся правым ребенком v;
            self.nodes[p].left = tmp # vl становится левым ребенком p ;
            # pr остаётся правым ребенком p
        else:
            tmp = self.nodes[v].right
            self.nodes[v].right = p# p становится правым ребенком v;
            self.nodes[p].parent = v
            # vl остаётся левым ребенком v;
            self.nodes[p].right = tmp # vr становится правым ребенком p;
            # pl остаётся левым ребенком p

n, _ = map(int, input().split(' '))
tree = Tree(n)

swaps = list(map(int, input().split(' ')))
for swp in swaps:
    tree.swap(swp)

tree.pre_order(1)
