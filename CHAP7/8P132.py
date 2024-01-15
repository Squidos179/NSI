def internNode(tree:tuple)->int:
    if tree == None: 
        return 0 
    else: 
        return 1 + size(tree[1]) + size(tree[2])

def heigh(tree:tuple)->int:
    if tree == None:
        return -1
    elif tree[1] == None and tree[2] == None:
        return 0
    else:
        return 1 + max(heigh(tree[1]), heigh(tree[2]))

def size(tree:tuple)-> int:
    if tree == None:
        return 0
    elif tree[1] == None and tree[2] == None:
        return 1
    else:
        return 1 + size(tree[1]) + size(tree[2])
    
def leaves(tree:tuple)->int: return size(tree) - internNode(tree)

tree1 = None
assert internNode(tree1) == 0

tree2 = (1, None, None)
assert internNode(tree2) == 1

tree3 = (1, (2, None, None), (3, None, None))
assert internNode(tree3) == 3

tree4 = None
assert heigh(tree4) == -1

tree5 = (1, None, None)
assert heigh(tree5) == 0

tree6 = (1, (2, None, None), (3, None, None))
assert heigh(tree6) == 1

tree7 = None
assert size(tree7) == 0

tree8 = (1, None, None)
assert size(tree8) == 1

tree9 = (1, (2, None, None), (3, None, None))
assert size(tree9) == 3