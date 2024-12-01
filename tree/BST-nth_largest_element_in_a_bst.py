# educative

def find_nth_highest_in_bst(node, n):
    if node is None:
        return None
      
    k = 0
    stack = []
    
    def go_right(node):
        while node:
            stack.append(node)
            node = node.right
            
            
    go_right(node)

    while stack:
        node = stack.pop()
        k += 1
        if k == n:
            return node
        go_right(node.left)
    
    return None