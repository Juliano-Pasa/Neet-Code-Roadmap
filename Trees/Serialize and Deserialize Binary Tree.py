from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""

        nodes = [root]
        while len(nodes):
            current = nodes.pop()

            if not current:
                result += "N#"
                continue
            
            result += str(current.val) + "#"
            nodes.append(current.right)
            nodes.append(current.left)

        return result

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split('#')
        if data[0] == 'N':
            return None

        root = TreeNode(data[0])
        nodes = [root]
        idx = 1
        
        while idx < len(data) - 1:
            if data[idx] == 'N':
                if data[idx-1] == 'N':
                    nodes.pop()
                idx += 1
                continue

            current = TreeNode(data[idx])
            parent = nodes[-1]

            if data[idx-1] == 'N':
                nodes.pop()
                parent.right = current
            else:
                parent.left = current
            nodes.append(current)
            idx += 1          
        
        return root