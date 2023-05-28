# leetcode, rt 80%, mu 63%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key and not (root.left or root.right):
                return None
        else:
            return None

        def searchNode(node, key):
            if node:
                if node.val > key:
                    return searchNode(node.left, key)
                elif node.val < key:
                    return searchNode(node.right, key)
                else:
                    return node

        def findNodeToSwitch(node, key):
            if node.left:
                node = node.left
                while node.right:
                    node = node.right
                return node
            elif node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node
        
        def searchParent(parent, node, key):
            """Find parent of node to be deleted, return none if not found."""
            if node.val < key:
                parent, node = node, node.right
            elif node.val > key:
                parent, node = node, node.left
            else:
                return parent
            return searchParent(parent, node, key)
        
        def deleteNode(root, key):
            parent = searchParent(None, root, key)
            if parent.left and parent.left.val == key:
                if parent.left.left:
                    parent.left = parent.left.left
                elif parent.left.right:
                    parent.left = parent.left.right
                else:
                    parent.left = None
            elif parent.right and parent.right.val == key:
                if parent.right.left:
                    parent.right = parent.right.left
                elif parent.right.right:
                    parent.right = parent.right.right
                else:
                    parent.right = None

        node = searchNode(root, key)
        if node:
            if node.left or node.right:
                node_switch = findNodeToSwitch(node, key)
                val = node_switch.val
                deleteNode(root, val)
                node.val = val
            else:
                deleteNode(root, key)
        return root
