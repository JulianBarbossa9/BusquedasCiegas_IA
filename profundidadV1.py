import numpy as np

# EstadoInicio ='''4-5-1
# 8-3-7
# e-6-2'''

# EstadoFinal= '''1-2-3
# 4-5-6
# 7-8-x'''

#filas = 3
#columnas = 3
#ff = [[1,2,3], [4,5,6], [7,8,0]]

# def list_to_string(list_):
#     return '\n'.join(['-'.join(row) for row in list_])

# def string_to_list(string_):
#     return [row.split('-') for row in string_.split('\n')]


# #print(string_to_list(EstadoInicio))
# #print(list_to_string(EstadoInicio))
# #matriz = np.array(ff).reshape(filas,columnas)
# #print(matriz)

# def localion (rows, elemeto_encotrar):
#     for fila, row in enumerate(rows):
#         for colum, elemento in enumerate(row):
#             if elemento == elemeto_encotrar:
#                 return fila , colum


# pos_final = {}
# fila_final = string_to_list(EstadoFinal)
# for numero in '12345678x':
#     pos_final[numero] = localion(fila_final, numero)

# #print(pos_final)


# estadoInicial = np.array([[1, 2, 3], [4, 5, 6], [7,8,0]])
# print(estadoInicial)
# newArr= []
# #for x in np.nditer(estadoInicial):
#     #newArr.append(x)


# #newArrPa = np.array([newArr])
# #print(newArrPa)

# for x in estadoInicial:
#     for y in x:
#             newArr.append(y)

# # print(newArr)
# newArrPa = np.array([newArr])
# # print(newArrPa)


#pp=range(0,100)
# for ss in range(3):
    # print(ss)

num_list = []
# 1 2 3
# 4 5 6
# 7 8 0 <--0;empty
# 3 * y + x + 1  
# (x= 1, y = 2) ==> 3 * 2 + 1 + 1 = 8
# (x = 2, y = 1) ==> 3 * 1 + 2 + 1 = 6
#Creo el arreglo de 3x3 con 0 que es el espacio que esta vacio
for x in range(3):
    l = []
    for y in range(3):
        l.append(3 * x + y + 1)
    num_list.append(l)
num_list[2][2] = 0

#print(num_list)

INICIAL=([[6, 2, 8],
        [4, 7, 1],
        [0, 3, 5]]) 


class Pila:

    def __init__(self, node_Incial, node_Final):
        self.items = []
        self.node_Incial = node_Incial
        self.node_Final = node_Final

    def estaVacia(self):
        return self.items == []
    
    def incluir(self, item):
        self.items.insert(0, item)
    
    def extraer(self):
        return self.items.pop(0)
    
    def tamano(self):
        return len(self.items)

    

# s = Pila(INICIAL, num_list)
# #s.incluir(num_list)
# s.incluir(INICIAL)
# s.incluir(num_list)
# s.extraer()
# print(s.tamano())
# print(s.estaVacia())

class hash_table:
    def __init__(self):
        self.table = [None] * 127

    #Función de la tabla de disperción
    def Hash_func(self, valor):
        key = 0
        for i in range(0, len(valor)):
            key += ord(valor[i])
        return key % 127

    #Funcion que ingresa elementos
    def InsertE(self, valor):
        hash = self.Hash_func(valor)
        if self.table[hash] is None:
            self.table[hash] = valor
    
    #Buscar elementos
    def busqueda(self, valor):
        hash = self.Hash_func(valor)
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
    
    def remover(self, valor):
        hash = self.Hash_func(valor)
        if self.table[hash] is None:
            print("No hay elementos con ese valor", valor)
        else:
            print("Elemento con valor", valor, "eliminado")
            self.table[hash] is None


# H = hash_table()
# H.InsertE(num_list)
# H.InsertE("B")
# H.InsertE("C")
# print(H.busqueda(num_list))
goal_state = np.array([1,2,3,5,8,4,0,6,7]).reshape(3,3)
pruebaspa = np.array([4,9,6,3]).reshape(2,2)
#print(goal_state)
zero_index = [i[0] for i in np.where(goal_state  == 0)]
        # if zero_index[0] == 0:
        #     return False
        # else:
        #     up_value = goal_state[zero_index[0]-1,zero_index[1]]
print(zero_index)
print(np.where(goal_state == 0))
visited = set([]) # record visited states
# pp = goal_state[zero_index[0]+1,zero_index[1]]
# print(pp)
# opa = goal_state.copy()
# # print(opa)
# opa[zero_index[0],zero_index[1]] = pp
# opa[zero_index[0] - 1,zero_index[1]] = 0
# print(opa)
#evitar el estado repetido, que se representa como una tupla
visited.add(tuple(pruebaspa.reshape(1,4)[0]))
print(visited)
print(goal_state)