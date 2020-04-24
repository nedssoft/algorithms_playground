def lca(root, v1, v2):
    if root == None:
        None
    if v1 > v2:        
        temp = v2
        v2 = v1
        v1 = temp
    while root.info < v1 or root.info > v2:
        if root.info < v1:
            root = root.right
        elif root.info > v2:
            root = root.left       
    return root 