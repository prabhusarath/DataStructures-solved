
# coding: utf-8

# In[1]:

def Tree_traversal(tree):
    preorder(tree)
    inorder(tree)
    postorder(tree)


# In[ ]:

def preorder(trees):
    if trees:
        print(trees.getVal()) #data
        preorder(trees.getLeft()); #LeftChild
        preorder(trees.getRight()); #RightChild


# In[ ]:

def inorder(trees):
    if trees:
        inorder(trees.getLeft()); #LeftChild
        print(trees.getVal());  #data
        inorder(trees.getRight());#RightChild


# In[ ]:

def postorder(trees):
    if trees:
        postorder(trees.getLeft()); #LeftChild
        postorder(trees.getRight()); #RightChild
        print(trees.getVal())  #data

