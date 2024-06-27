import sys
import os
import colorama 

sys.path.append('../')
from controller.tda.queque.quequeOperation import QuequeOperation
from controller.tda.stack.stackOperation import StackOperation
from controller.censoDao import CensoDao 
from controller.personaDaoControl import PersonaDaoControl


from controller.calculos import Calculos
from controller.tdaArray import TDAArray
from model.persona import Persona
from controller.tda.linked.linkedList import LinkedList
from controller.personaControl import PersonaControl

colorama.init()

def limpira_consola():
    os.system('cls||cls||clear')

#--------------------------------------------------------------------

# if __name__ == "__main__":
#     pc = PersonaControl()
#     pcd = PersonaDaoControl()
#     cd = CensoDao()
    
#     try:
    #     pc._persona._id = pc.generate_id()
    #     pc._persona._apellido = "Summer"
    #     pc._persona._nombres = "Brienne"
    #     pc._persona._telefono = "0983912311"
    #     pcd._persona._id = pc.generate_id()
    #     pcd._persona._apellido = "Summer"
    #     pcd._persona._nombres = "Brienne"
    #     pcd._persona._telefono = "0983912311"
    #     pc.save
    #     pcd.save
    #     pcd._persona = None
    #     pc._persona = None
    #     pc._persona._id = pc.generate_id()
    #     pc._persona._apellido = "Lilith"
    #     pc._persona._nombres = "Dubois"
    #     pc._persona._telefono = "0812931213"
    #     pcd._persona._id = pc.generate_id()
    #     pcd._persona._apellido = "Lilith"
    #     pcd._persona._nombres = "Dubois"
    #     pcd._persona._telefono = "0812931213"
    #     pc.save
    #     pcd.save
    #     pcd._persona = None
    #     pc._persona = None
    #     pc._persona._id = pc.generate_id()
    #     pc._persona._apellido = "Jean"
    #     pc._persona._nombres = "Roux"
    #     pc._persona._telefono = "08129371293"
    #     pcd._persona._id = pc.generate_id()
    #     pcd._persona._apellido = "Jean"
    #     pcd._persona._nombres = "Roux"
    #     pcd._persona._telefono = "08129371293"
    #     pc.save
    #     pcd.save
    #     pcd._persona = None
        # pc._persona = None
        # pc._persona._id = pc.generate_id()
        # pc._persona._apellido = "Emilie"
        # pc._persona._nombres = "Leroy"
        # pc._persona._telefono = "0721937112"
        # pcd._persona._id = pc.generate_id()
        # pcd._persona._apellido = "Emilie"
        # pcd._persona._nombres = "Leroy"
        # pcd._persona._telefono = "0721937112"
        # pc.save
    #     pcd.save
    #     pcd._persona = None
    #     pc._persona = None
    #     pc._persona._id = pc.generate_id()
    #     pc._persona._apellido = "Anne"
    #     pc._persona._nombres = "Lambert"
    #     pc._persona._telefono = "0987129312"
    #     pcd._persona._id = pc.generate_id()
    #     pcd._persona._apellido = "Anne"
    #     pcd._persona._nombres = "Lambert"
    #     pcd._persona._telefono = "0987129312"
    #     pc.save
    #     pcd.save
        
    #     cd.get_censo()._fecha = "2005-05-25"
    #     cd.get_censo()._censador = "Isabel Borns"
    #     # cd.get_censo()._peso = 50
    #     cd.get_censo()._weight = 50
    #     cd.get_censo()._estatura = 1.75
    #     cd.save
        
    # except Exception as error:
    #     print(error)

    # print(pcd._list())
    # print(cd._list())

#--------------------------------------------------------------------

# if __name__ == "__main__":
# #     limpira_consola()
# #     stack = StackOperation(5)
# #     queque = QuequeOperation(5)
    
#     try:
#         print(colorama.Fore.RED+ f"\n\nStack" + colorama.Fore.RESET)
#         stack.push(24)
#         stack.push(10)
#         stack.push(6)
#         stack.push(5)
#         print(colorama.Fore.BLUE+ f"\nImpresion de Stack" + colorama.Fore.RESET)
#         stack.print
#         stack.pop
#         stack.print
#         stack.pop
#         stack.print

# #         print(colorama.Fore.GREEN+ f"\nQueque" + colorama.Fore.RESET)
# #         queque.queque(24)
# #         queque.queque(10)
# #         queque.queque(6)
# #         queque.queque(5)
# #         print(colorama.Fore.BLUE+ f"\nImpresion de Stack" + colorama.Fore.RESET)
# #         queque.print
# #         queque.dequeque
# #         queque.print
# #         queque.dequeque
# #         queque.print

#     except Exception as e:
#         print(f"El error es: {e}")
        
        
# colorama.deinit()



pd = PersonaDaoControl()
print(pd.to_dict())