from controller.tda.tree.jug.node import Node
from controller.tda.linked.linkedList import LinkedList
from controller.tda.tree.jug.rules import Rules

class JugTree():
    def __init__(self, first, last) -> None:
        self.__state_first = first
        self.__state_final = last
        self.__nodes = LinkedList()
        self.__list_nodes = LinkedList()

    def isNodeSearch(self, na, ns):
        return (na._jD._current_capacity == ns._jD._current_capacity) and (na._jL._current_capacity == ns._jL._current_capacity)
        
    def search(self):
        try: 
            if self.isNodeSearch(self.__state_first, self.__state_final):
                self.__nodes.add(self.__state_final, self.__nodes._length)
            else:
                self.__nodes = LinkedList()
                self.__list_nodes = LinkedList()
                self.__list_nodes.add(self.__state_first, self.__nodes._length)
                while self.__list_nodes._length > 0:
                    current = self.__list_nodes.deleteFirst()
                    if self.isNodeSearch(current, self.__state_final):
                        return current
                    else:
                        ar = Rules()
                        rules = ar.rules(current._jD, current._jL)
                        rules = self.deleteRules(rules)
                        current.addSucessors(rules)
                        for i in range(0, rules._length):
                            auxR = rules.get(i)
                            self.__list_nodes.add(auxR, self.__list_nodes._length)
                            self.__nodes.add(auxR, self.__nodes._length)
                            if self.isNodeSearch(auxR, self.__state_final):
                                return auxR
        except Exception as error:
            print("errores")
            print(error)
        return None

    def deleteRules(self, rules):
        list = LinkedList()
        if not (rules.isEmpty and self.__nodes.isEmpty):
            rulesA = rules.toArray 
            nodesA = self.__nodes.toArray
            for i in range(0, len(rulesA)):
                nad = True  
                for j in range(0, len(nodesA)):
                    if self.isNodeSearch(rulesA[i], nodesA[j]):
                        nad = False
                        break
                if nad:
                    list.add(rulesA[i])
        return list
            

    def route(self, node):
        routes = LinkedList() 
        while node != None:
            routes.add(node)
            node = node._father
        return routes
    