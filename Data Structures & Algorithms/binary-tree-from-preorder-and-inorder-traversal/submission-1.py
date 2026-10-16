class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # inorder tracks split point l-root-r
        split_point = {val:i for i, val in enumerate(inorder)}

        # preorder tracks all roots in sequence
        self.pre_i = 0

        def dfs(l, r):
            if l > r: return None

            root_val = preorder[self.pre_i]
            self.pre_i += 1

            root = TreeNode(root_val)

            split_i = split_point[root_val]

            root.left = dfs(l, split_i-1)
            root.right = dfs(split_i+1, r)

            return root
        

        return dfs(0, len(preorder)-1)