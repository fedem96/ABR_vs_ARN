import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.father = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        x = self.root
        p = None
        while x is not None:
            p = x
            if key <= x.key:
                x = x.left
            else:
                x = x.right

        if p is None:
            self.setRoot(key)
        elif key <= p.key:
            p.left = Node(key)
            p.left.father = p
        else:
            p.right = Node(key)
            p.right.father = p

    def insertNode(self, currentNode, key):
        if key <= currentNode.key:
            if currentNode.left:
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
                currentNode.left.father = currentNode
        elif key > currentNode.key:
            if currentNode.right:
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)
                currentNode.right.father = currentNode

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if currentNode is None:
            return currentNode
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inorder(self):
        def _inorder(v):
            if v.key is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print(v.key)
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)

    def trapianto(self, toBeReplacedNode, replacingNode):
        if toBeReplacedNode.father is None:
            self.root = replacingNode
        elif toBeReplacedNode == toBeReplacedNode.father.left:
            toBeReplacedNode.father.left = replacingNode
        else:
            toBeReplacedNode.father.right = replacingNode
        if replacingNode is not None:
            replacingNode.father = toBeReplacedNode.father

    def minimo(self, x):
        while x.left is not None:
            x = x.left
        return x

    def delete(self, key):
        z = self.find(key)
        if z is None:
            return
        if z.left is None:
            self.trapianto(z, z.right)
        elif z.right is None:
            self.trapianto(z, z.left)
        else:
            y = self.minimo(z.right)
            if y.father != z:
                self.trapianto(y, y.right)
                y.right = z.right
                y.right.father = y
            self.trapianto(z, y)
            y.left = z.left
            y.left.p = y

    def show(self):
        nodes = []
        nodes.append(self.root)
        h = self.nodeHeigth(self.root)
        numCifre = 2
        while nodes:
            newNodes = []
            sys.stdout.write(" " * int(numCifre*((2**(h+1) - 1)/2)))
            allNone = True
            for node in nodes:
                if node is not None:
                    allNone = False
                    print(node.key, end="")
                    newNodes.append(node.left)
                    newNodes.append(node.right)
                else:
                    print(" " * numCifre, end="")
                    newNodes.append(None)
                    newNodes.append(None)
                sys.stdout.write(" " * (numCifre*(2**(h+1) - 1)))
                sys.stdout.flush()
            print()
            if allNone:
                break
            nodes = newNodes
            h = h-1

    def height(self):
        if self.root is None:
            return 0
        return self.nodeHeigth(self.root)

    def nodeHeigth(self, node):
        if node is None:
            return -1
        hLeft = self.nodeHeigth(node.left)
        hRight = self.nodeHeigth(node.right)
        if hLeft >= hRight:
            return 1 + hLeft
        return 1 + hRight


def main():
    tree = ABR()
    sys.setrecursionlimit(10000)
    tree.insert(12)
    tree.insert(10)
    tree.insert(15)
    tree.insert(13)
    tree.insert(11)
    tree.insert(16)
    tree.insert(25)
    tree.show()

if __name__ == "__main__":
    main()
