class Graph():
    def __init__(self):

        @property
        def num_vertex(self):
            raise NotImplementedError("Por favor implemente este método")

        @property
        def num_edges(self):
            raise NotImplementedError("Por favor implemente este método")
            
        def exist_edges(self, v1, v2):
            raise NotImplementedError("Por favor implemente este método")
        
        def weight_edges(self, v1, v2):
            raise NotImplementedError("Por favor implemente este método")
        
        def insert_edges(self, v1, v2):
            raise NotImplementedError("Por favor implemente este método")
        
        def insert_edges_weight(self, v1, v2, weight):
            raise NotImplementedError("Por favor implemente este método")
        
        def adjacent(self, v1):
            raise NotImplementedError("Por favor implemente este método")

    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i + 1) + "\n"
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range (0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady " + "V" + str(adj._destination + 1) + "weight " + str(adj._weight) + "\n"
        return out 
        