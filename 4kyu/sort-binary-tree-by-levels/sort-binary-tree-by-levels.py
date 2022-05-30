def tree_by_levels(node):
    result = []
    if not node:
        return result
    q = []
    q.append(node)
    while q != []:
        node = q.pop(0)
        result.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)    
    return result
