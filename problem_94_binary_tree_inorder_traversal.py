from typing import List, Optional
from structure_builders.binary_tree import TreeNode, list_to_tree, print_levels


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def recurssive_traversal(head: Optional[TreeNode]):
            if head is None:
                return

            recurssive_traversal(head.left)

            answer.append(head.val)

            recurssive_traversal(head.right)

        recurssive_traversal(root)
        return answer


"""
Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 
"""
if __name__ == "__main__":
    solution = Solution()
    tree = list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

    # result = solution.inorderTraversal(tree)

    print("Inorder Traversal Result:")
    print_levels(tree)
