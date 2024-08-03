from controller.tda.linked.linkedList import LinkedList
from controller.tda.tree.jug.node import Node

class Rules():
    def rules(self,jb, jl):
        x = jb._current_capacity
        y = jl._current_capacity
        rules = LinkedList() 

        #* regla 1
        if x < jb._capacity: 
            node = Node()
            node.set_current_capacity(jb._capacity, y)
            rules.add(node)

        #* regla 2
        if x < jl._capacity: 
            node = Node()
            node.set_current_capacity(x, jl._capacity)
            rules.add(node)

        #* Vaciar jarra grande
        if x > 0:
            node = Node()
            node.set_current_capacity(0, y)
            rules.add(node)

        #* Vaciar jarra pequenia
        if y > 0:
            node = Node()
            node.set_current_capacity(x, 0)
            rules.add(node)
            
        #* Llenar la jarra grande con la pequenia 
        if (x+y) >= jb._capacity and (x < jb._capacity and y > 0):
            node = Node()
            node.set_current_capacity(jb._capacity, y - (jb._capacity - x))
            rules.add(node)
            
        #* Llenar la jarra pequenia con la grande
        if (x+y) >= jl._capacity and (y < jl._capacity and x > 0):
            node = Node()
            node.set_current_capacity(x - (jl._capacity - y), jl._capacity)
            rules.add(node)
            
        #* Vaciar la jarra grande em la pequenia 
        if (x+y) <= jl._capacity and x > 0:
            node = Node()
            node.set_current_capacity(0, (x+y))
            rules.add(node)
            
        #* Vaciar la jarra pequenia em la grande 
        if (x+y) <= jb._capacity and y > 0:
            node = Node()
            node.set_current_capacity((x+y), 0)
            rules.add(node)

        return rules