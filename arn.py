import sys

from termcolor import colored


class ColoredNode:
    def __init__(self, key, black=True):
        self.key = key
        self.left = None
        self.right = None
        self.father = None
        self.isBlack = black


class ARN:
    def __init__(self):
        self.NIL = ColoredNode(None)
        self.root = self.NIL

    def setRoot(self, key):
        self.root = ColoredNode(key)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.father = x
        y.father = x.father
        if x.father is self.NIL:
            self.root = y
        elif x == x.father.left:
            x.father.left = y
        else:
            x.father.right = y
        y.left = x
        x.father = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.father = x
        y.father = x.father
        if x.father is self.NIL:
            self.root = y
        elif x == x.father.right:
            x.father.right = y
        else:
            x.father.left = y
        y.right = x
        x.father = y

    def fixup(self, z):
        while z.father.isBlack is False:
            if z.father == z.father.father.left:
                y = z.father.father.right
                if y.isBlack is False:
                    z.father.isBlack = True
                    y.isBlack = True
                    z.father.father.isBlack = False
                    z = z.father.father
                else:
                    if z == z.father.right:
                        z = z.father
                        self.leftRotate(z)
                    z.father.isBlack = True
                    z.father.father.isBlack = False
                    self.rightRotate(z.father.father)
            else:
                if z.father == z.father.father.right:
                    y = z.father.father.left
                    if y.isBlack is False:
                        z.father.isBlack = True
                        y.isBlack = True
                        z.father.father.isBlack = False
                        z = z.father.father
                    else:
                        if z == z.father.left:
                            z = z.father
                            self.rightRotate(z)
                        z.father.isBlack = True
                        z.father.father.isBlack = False
                        self.leftRotate(z.father.father)
        self.root.isBlack = True

    def insertNode(self, key):
        z = ColoredNode(key)
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.father = y
        if y is self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.isBlack = False
        self.fixup(z)

    def insert(self, key):
        self.insertNode(key)

    def findRoot(self):
        return self.root.key

    def inorder(self):
        def _inorder(v):
            if v is self.NIL:
                return
            if v.left is not self.NIL:
                _inorder(v.left)
            if v.isBlack:
                print(v.key)
            else:
                print(colored(v.key, 'red'))
            if v.right is not self.NIL:
                _inorder(v.right)
        _inorder(self.root)

    def height(self):
        if self.root.key is None:
            return 0
        return self.nodeHeigth(self.root)

    def nodeHeigth(self, node):
        if node is None or node.key is None:
            return -1
        hLeft = self.nodeHeigth(node.left)
        hRight = self.nodeHeigth(node.right)
        if hLeft >= hRight:
            return 1 + hLeft
        return 1 + hRight

    def blackHeight(self):
        cont = 0
        n = self.root
        while n is not self.NIL:
            if n.isBlack is 'black':
                cont += 1
            n = n.right
        return cont

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
                if node is not None and node.key is not None:
                    allNone = False
                    if node.isBlack:
                        print(node.key, end="")
                    else:
                        print(colored(node.key, 'red'), end="")
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


def main():
    albero = ARN()
    for i in range(10, 20):
        albero.insert(i)

    albero.show()

if __name__ == "__main__":
    main()