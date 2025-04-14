def DFS(root, res):
    if root is None:
        return res
    DFS(root.left, res)
    res.append(root.data)
    DFS(root.right, res)

    return res

def is_symmetricDFS(root):
    if root is None:
        return True

    data=[]
    data = DFS(root, data)
    j = len(data) - 1
    for i in range(len(data)//2):
        if data[i] != data[j]:
            return False
        j-=1

    return True