
from controller.tda.linked.linkedList import LinkedList
from controller.tda.tree.node import Node

class TreeNumber():
    def __init__(self) -> None:
        self.__root = None 
        self.__heigth = 0 
        self.__nro_nodes = 0 
        self.__levels =  LinkedList()
        self.__orders =  LinkedList()
        
    @property
    def getNodes(self):
        return self.__nro_nodes

    @property
    def getHeight(self):
        return self.__heigth

    def __calcHeight(self, tree):
        if tree ==  None:
            return 9
        else:
            left = self.__calcHeight(tree._left)
            right = self.__calcHeight(tree._right)
            if left > right:
                left += 1
                return left 
            else:
                right += 1
                return right
            
    def __calcLevels(self, tree, level):
        if tree != None:
            self.__levels.get(level).add(tree)
            level += 1
            self.__calcLevels(tree._left, level)
            self.__calcLevels(tree._right, level)
        else:
            self.__levels.get(level).add(None)
            level += 1
            self.__calcLevels(None, level)
            self.__calcLevels(None, level)

    def levels(self):
        self.__levels = LinkedList()
        #TODO
        #calc height
        self.__heigth = self.__calcHeight(self.__root)
        for i in range(0, self.__heigth):
            self.__levels.add(LinkedList())
            
    
    def insert(self, data):
        if self.__root == None:
            self.__root = Node(data)
            self.__nro_nodes += 1
            self.levels()
            return True
        else:
            new = Node(data)
            recent = self.__root
            father = None 
            while True:
                father = recent
                if data == recent._data:
                    return False
                elif data < recent._data:
                    recent = recent._left
                    if recent == None:
                        new._father = father
                        father._left = new 
                        self.__nro_nodes += 1
                        self.levels()
                        return True
                else:
                    recent = recent._right
                    if recent == None:
                        new._father = father
                        father._right = new 
                        self.__nro_nodes += 1
                        self.levels()
                        return True
                    
    def __pre_order(self, tree):
        if tree != None:
            self.__orders.add(tree, self.__orders._length)
            self.__pre_order(tree._left)
            self.__pre_order(tree._right)

    def pre_orders(self):
        self.__orders = LinkedList()
        self.__pre_order(self.__root)
        return self.__orders
                    
    def __pos_order(self, tree):
        if tree != None:
            self.__pos_order(tree._left)
            self.__pos_order(tree._right)
            self.__orders.add(tree, self.__orders._length)

    def pos_orders(self):
        self.__orders = LinkedList()
        self.__pos_order(self.__root)
        return self.__orders

    def __in_order(self, tree):
        if tree != None:
            self.__in_order(tree._left)
            self.__orders.add(tree, self.__orders._length)
            self.__in_order(tree._right)

    def in_orders(self):
        self.__orders = LinkedList()
        self.__in_order(self.__root)
        return self.__orders