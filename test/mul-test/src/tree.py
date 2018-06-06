from treelib import Tree

class Tree1(Tree):

    def createTree(self,path):
        infile = open(path, 'r')
        lines = infile.readlines()  # 读取多行

        tree1 = Tree()

        line1 = lines[0]
        root = line1.split(';')[0]
        children = line1.split(';')[1][:-1]
        childs = children.split(',')

        tree1.create_node(root, root)
        for child in childs:
            tree1.create_node(child, child, parent=root)

        for line in lines[1:]:
            parent = line.split(';')[0]
            children = line.split(';')[1][:-1]
            childs1 = children.split(',')
            for child1 in childs1:
                tree1.create_node(child1, child1, parent=parent)
        return tree1

