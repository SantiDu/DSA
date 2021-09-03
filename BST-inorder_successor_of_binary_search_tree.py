def find_successor(root, d):
  def find_min(node):
    while node.left:
      node = node.left
    return node

  # def find_inorder_successor(node):
  #   if node.right:
  #     node = find_min(node.right)
  #     return node
  #   else:
  #     while node.parent:
  #       if node.parent.left is node:
  #         return node
  #       node = node.parent
  #     return None

  successor = None

  while root:
    if root.data > d:
      successor = root
      root = root.left
    elif root.data < d:
      root = root.right
    else:
      if root.right:
        return find_min(root.right)
      return successor

  return root