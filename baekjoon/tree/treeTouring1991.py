"""트리 순회...해결안됨.. 다시보자"""
"""내가 다시 짜보자"""
import sys

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]
print(tree)

# root->left->right
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# left->root->right
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# left->right->root
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')