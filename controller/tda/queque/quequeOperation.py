
from controller.tda.linked.linkedList import LinkedList
from controller.exception.LinkedEmpty import LinkedEmpty
import colorama 


colorama.init() 
class QuequeOperation(LinkedList):
    def __init__(self, top):
        super().__init__() 
        self.__top = top

    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verify_top(self):
        print(colorama.Fore.CYAN + f"Dentro de verify_top: {self._length}" + colorama.Fore.RESET)
        return self._length < self._top
    
    def queque(self, data):
        if self.verify_top:
            self.add(data, self._length)
        else:
            raise LinkedEmpty('Queque full')
    
    @property 
    def dequeque(self):
        if self.isEmpty:
            raise LinkedEmpty('Queque empty')
        else:
            return self.delete(0)
        
        
colorama.deinit() 
    
if __name__ == "__main__":
    pass