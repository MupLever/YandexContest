class Node:
    def __init__(self, _value):
        self.value = _value
        self.parent = None
        self.left = None
        self.right = None

    def str(self):
        return "parent: " + str(self.parent) + "\nleft: " + str(self.left) + "\nright: " + str(self.right)

class Tree:
    def __init__(self, _N):
        self.N = _N
        self.root = 1
        self.nodes = [None]
        for i in range(1, self.N + 1):
            node = Node(i)
            parent = i // 2
            if parent > 0:
                node.parent = self.nodes[parent].value
                if self.nodes[parent].left is None:
                    self.nodes[parent].left = i
                else:
                    self.nodes[parent].right = i
            self.nodes.append(node)

    def in_order(self, v):
        if self.nodes[v] is None:
            return

        if self.root == v:
            print(self.nodes[v].value, end=' ')

        if self.nodes[v].left:
            self.in_order(self.nodes[v].left)

        if self.root != v:
            print(self.nodes[v].value, end=' ')

        if self.nodes[v].right:
            self.in_order(self.nodes[v].right)

    def swap(self, v):
        if self.root == v:
            return
        
        p = self.nodes[v].parent

        if self.nodes[p].parent is not None:
            pp = self.nodes[p].parent
            if self.nodes[pp].left == p: # p — левый ребенок вершины pp, то 
                self.nodes[pp].left = v # v становится левым ребенком pp
            else:
                self.nodes[pp].right = v # v становится правым ребенком pp
            self.nodes[v].parent = pp
        else:
            self.root = v
            self.nodes[v].parent = None

        if self.nodes[p].left == v: #v — левый ребенок вершины p , то
            left_tree = self.nodes[v].left
            self.nodes[v].left = p #p становится левым ребенком v ;
            self.nodes[p].parent = v
            # vr остаётся правым ребенком v;
            self.nodes[p].left = left_tree # vl становится левым ребенком p ;
            if left_tree is not None:
                self.nodes[left_tree].parent = p
            # pr остаётся правым ребенком p
        else:
            right_tree = self.nodes[v].right
            self.nodes[v].right = p # p становится правым ребенком v;
            self.nodes[p].parent = v
            # vl остаётся левым ребенком v;
            self.nodes[p].right = right_tree # vr становится правым ребенком p;
            if right_tree is not None:
                self.nodes[right_tree].parent = p
            # pl остаётся левым ребенком p

n, _ = map(int, input().split(' '))
tree = Tree(n)

swaps = list(map(int, input().split(' ')))
for swp in swaps:
    tree.swap(swp)

tree.in_order(tree.root)
