# leetcode, rt 42%, mu 97%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def go(node):
            if node:
                yield str(node.val)
                if node.left:
                    yield from go(node.left)
                else:
                    yield ","
                if node.right:
                    yield from go(node.right)
                else:
                    yield ","
        return " ".join(go(root))
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def translate(val):
            if val and val != ",":
                return TreeNode(val)

        def stream(data):
            for i in data.split(" "):
                yield translate(i)
        
        def deserialize(stream):
            node = next(stream)
            if node:
                node.left = deserialize(stream)
                node.right = deserialize(stream)
            return node
        
        return deserialize(stream(data))
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))