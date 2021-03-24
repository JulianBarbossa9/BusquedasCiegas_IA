import numpy as np
import time

class Node():
    def __init__(self, state, parent,action, depth, step_cost):
        self.state = state
        self.parent = parent
        self.action = action 
        self.depth = depth
        self.step_cost = step_cost
        

        #Nodos Hijos
        self.mov_up = None
        self.mov_down = None
        self.mov_left = None
        self.mov_right = None

    # Miro si se puede mover hacia abajo
    def mover_abajo(self):
        # Busco donde esta la baldosa vacia
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[0] == 0:
            return False
        else:
            #Valor de la baldosa de arriba
            up_valor = self.state[zero_index[0] - 1, zero_index[1]]
            new_state = self.state.copy()
            #La baldosa vacia le doy el nuevo valor de la baldosa de arriba
            new_state [zero_index[0], zero_index[1]] = up_valor
            #La baldosa de arriba le doy el valor de la baldosa vacia
            new_state [zero_index[0] - 1, zero_index[1]] = 0
            return new_state, up_valor

    #Miro si se puede mover hacia la derecha
    def  mover_derecha(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index [1] == 0:
            return False
        else :
            #Valor de la baldosa de la derecha 
            left_valor = self.state[zero_index[0],zero_index[1] - 1]
            #Guardo la posicion de las baldosas
            new_state = self.state.copy()
            new_state[zero_index[0], zero_index[1]] = left_valor
            new_state[zero_index[0], zero_index[1] - 1] = 0 
            return new_state, left_valor

    #Miro si se puede mover hacia arriba
    def mover_arriba(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[0] == 2:
            return False
        else:
            #Valor de de la baldosa de abajo
            abajo_valor = self.state[zero_index[0] + 1, zero_index[1]]
            new_state = self.state.copy()
            new_state[zero_index[0],zero_index[1]] = abajo_valor
            new_state[zero_index[0] + 1,zero_index[1]] = 0
            return new_state, abajo_valor

    #Miro si se puede mover a la izquierda
    def mover_izquier(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[1] == 2:
            return False
        else:
            #Valor de la baldosa de la derecha
            right_valor = self.state[zero_index[0],zero_index[1] + 1]
            new_state = self.state.copy()
            new_state[zero_index[0],zero_index[1]] = right_valor
            new_state[zero_index[0],zero_index[1] + 1] = 0
            return new_state,right_valor

    #Muestra los resutados
    def mostrarResul(self):
        rastro_state = [self.state]
        rastro_action = [self.action]
        rastro_prof = [self.depth]
        rastro_step_cost = [self.step_cost]
       

        #Añado informacion a los nodos
        while self.parent:
            self = self.parent

            rastro_state.append(self.state)
            rastro_action.append(self.action)
            rastro_prof.append(self.depth)
            rastro_step_cost.append(self.step_cost)
            

        #Contador de pasos
        contador = 0
        while rastro_state:
            print ('Paso:',str(contador))
            print (rastro_state.pop())
            # print 'Accion: ', rastro_action.pop(),'profundidad: ', str(rastro_prof.pop()), 'step cost: ', str(rastro_step_cost.pop()), 'Total:  ',str(rastro_path_cost.pop())
            print ('Acción = ',rastro_action.pop(),', Profundidad =',str(rastro_prof.pop()),\
            ', Valor de la baldosa = ',str(rastro_step_cost.pop()),'\n')

            contador += 1
    
    ###########Busquedas
    def busqueda_primero_Anchura(self, goal_state):
        start = time.time()
        #Cola de nodos encontrados, peron no visitados
        agenda = [self]
        #Numero de nodos que salieron de la cola, para medir el tiempo y rendimiento de la busqueda
        agenda_num_nodos_sali = 0
        #Numero máximo de nodos en cola, para medir rendimiento del espacio usado
        agenda_max_length = 1
        #Profundidad de la agenda
        prof_agenda = [0] 
        #Cola para coste de trayecto ////////////
        agenda_path_cost = [0]
        #Recordar nodos visitados (expandidos)
        visitado = set([])

        while agenda:
            if len(agenda) > agenda_max_length:
                agenda_max_length = len(agenda)#Actualizo la longitud maxima de la cola
        
            #Remuevo y selecciono el primer elemento de la cola (.pop)
            nodo_actual = agenda.pop(0)
            agenda_num_nodos_sali += 1
            #Actualizo la profundidad del nodo actual
            prof_actual = prof_agenda.pop(0)
            #Actualizar el camino para llegar al nodo actual
            path_cost_actual = agenda_path_cost.pop(0)
            #Guardo en "visitado" los nodos ya visitados, asi evitar estados repetidos, que se representa como una tupla - Guarde los estados visitados en una matriz de 1x9
            visitado.add(tuple(nodo_actual.state.reshape(1,9)[0]))

            #Cuando se encuentre el estado Meta/Final buscar el nodo raiz y mostrar ruta
            if np.array_equal(nodo_actual.state, goal_state):#Miro si el nodo actual es igual al estados meta si es asi entra
                nodo_actual.mostrarResul()

                #Muestre resultados
                #print("Rendimeinto de numero de nodos visitados: " + str(agenda_num_nodos_sali))
                print ('Nodos salidos de la Cola: ',str(agenda_num_nodos_sali))
                #print("Numero maximo de nodos visitado: " + str(agenda_max_length))
                print ('Maximo de nodos en la Cola: ', str(agenda_max_length))
                #print("Tiempo: %0.2fs " % (time.time()-start))
                print ('Tiempo: %0.2fs' % (time.time()-start))

                return True

            else:
                #Miro si se puede mover la baldosa vacia hacia abajo
                if nodo_actual.mover_abajo():
                    new_state, up_valor = nodo_actual.mover_abajo()
                    #Miro si el nodo actual ya ha sido visitado
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:
                        
                        #Creo un nodo hijo
                        nodo_actual.mov_down = Node (state = new_state, parent = nodo_actual, action = 'arriba', depth = prof_actual + 1, step_cost = up_valor)

                        agenda.append(nodo_actual.mov_down)
                        prof_agenda.append(prof_actual + 1)
                        agenda_path_cost.append(path_cost_actual + up_valor)
                
                # Miro se se puede mover la baldosa de iz a derecha
                if nodo_actual.mover_derecha():
                    new_state, left_valor = nodo_actual.mover_derecha()
                    #Miro si el nodo ya ha sido visitado
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:

                        #Creo un nodo hijo
                        nodo_actual.mov_right = Node (state = new_state, parent = nodo_actual, action = 'izquierda', depth = prof_actual + 1, step_cost = left_valor)

                        agenda.append(nodo_actual.mov_right)
                        prof_agenda.append(prof_actual + 1)
                        agenda_path_cost.append(path_cost_actual + left_valor)

                #Miro si se puede mover la baldosa de abajo hacia arriba
                if nodo_actual.mover_arriba():
                    new_state, abajo_valor = nodo_actual.mover_arriba()
                    #Miro si el nodo ya ha sido visitado 
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:

                        #Creo un nodo hijo
                        nodo_actual.mov_up = Node(state = new_state, parent = nodo_actual, action = 'abajo', depth = prof_actual + 1, step_cost = abajo_valor)

                        agenda.append(nodo_actual.mov_up)
                        prof_agenda.append(prof_actual + 1)
                        agenda_path_cost.append(path_cost_actual + abajo_valor)
                
                #Miro si puedo mover la baldosa de der a izquier
                if nodo_actual.mover_izquier():
                    new_state, right_valor = nodo_actual.mover_izquier()
                    #Miro se el nodo ya ha sido visitado
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:

                        #Creo nodo hijo
                        nodo_actual.mov_left = Node(state = new_state, parent = nodo_actual, action = 'derecha', depth = prof_actual + 1, step_cost = right_valor)

                        agenda.append(nodo_actual.mov_left)
                        prof_agenda.append(prof_actual + 1)
                        agenda_path_cost.append(right_valor + path_cost_actual)

    def busqueda_primero_Profundidad(self, goal_state):

        start = time.time()
        #Pila de nodos encontrados pero no visitados
        agenda = [self]
        # Numero de nodos sacados de la pila
        agenda_num_nodos_sali = 0
        #Numero máximo de nodos en la pila, para medir rendimiento del espacio usado
        agenda_max_length = 1
        #Profundidad de la pila
        prof_agenda = [0]
        #Pila para el coste del trayecto
        agenda_path_cost = [0]
        #Recordar nodos visitados (expandidos)
        visitado = set([])

        while agenda:
            if len(agenda) > agenda_max_length:
                agenda_max_length = len(agenda)
            
            nodo_actual = agenda.pop(0)#Selecciono y elimino el primer nodo de la pila
            agenda_num_nodos_sali += 1
            #Actualizo la profundidad del nodo actual
            prof_actual = prof_agenda.pop(0)
            #Actualizar el camino para llegar al nodo actual
            path_cost_actual = agenda_path_cost.pop(0)
            #Guardo en "visitado" los nodos ya visitados, asi evitar estados repetidos, que se representa como una tupla - Guarde los estados visitados en una matriz de 1x9
            visitado.add(tuple(nodo_actual.state.reshape(1,9)[0]))

             #Cuando se encuentre el estado Meta/Final buscar el nodo raiz y mostrar ruta
            if np.array_equal(nodo_actual.state, goal_state):#Miro si el nodo actual es igual al estados meta si es asi entra
                nodo_actual.mostrarResul()

                #Muestre resultados
                #print("Rendimeinto de numero de nodos visitados: " + str(agenda_num_nodos_sali))
                print ('Nodos salidos de la Pila: ',str(agenda_num_nodos_sali))
                #print("Numero maximo de nodos visitado: " + str(agenda_max_length))
                print ('Maximo de nodos en la Pila: ', str(agenda_max_length))
                #print("Tiempo: %0.2fs " % (time.time()-start))
                print ('Tiempo: %0.2fs' % (time.time()-start))

                return True

            else: 

                #Miro si se puede mover la baldosa vacia hacia abajo
                if nodo_actual.mover_abajo():
                    new_state, up_valor = nodo_actual.mover_abajo()
                    #Miro si el nodo actual ya ha sido visitado
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:
                        
                        #Creo un nodo hijo
                        nodo_actual.mov_down = Node (state = new_state, parent = nodo_actual, action = 'arriba', depth = prof_actual + 1, step_cost = up_valor)

                        agenda.insert(0, nodo_actual.mov_down)
                        prof_agenda.insert(0, prof_actual + 1)
                        agenda_path_cost.insert(0, path_cost_actual + up_valor)
                
                # Miro se se puede mover la baldosa de iz a derecha
                if nodo_actual.mover_derecha():
                    new_state, left_valor = nodo_actual.mover_derecha()
                    #Miro si el nodo ya ha sido visitado
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:

                        #Creo un nodo hijo
                        nodo_actual.mov_right = Node (state = new_state, parent = nodo_actual, action = 'izquierda', depth = prof_actual + 1, step_cost = left_valor)

                        agenda.insert(0, nodo_actual.mov_right)
                        prof_agenda.insert(0, prof_actual + 1)
                        agenda_path_cost.insert(0, path_cost_actual + left_valor)

                #Miro si se puede mover la baldosa de abajo hacia arriba
                if nodo_actual.mover_arriba():
                    new_state, abajo_valor = nodo_actual.mover_arriba()
                    #Miro si el nodo ya ha sido visitado 
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:

                        #Creo un nodo hijo
                        nodo_actual.mov_up = Node(state = new_state, parent = nodo_actual, action = 'abajo', depth = prof_actual + 1, step_cost = abajo_valor)

                        agenda.insert(0, nodo_actual.mov_up)
                        prof_agenda.insert(0, prof_actual + 1)
                        agenda_path_cost.insert(0, path_cost_actual + abajo_valor)
                
                #Miro si puedo mover la baldosa de der a izquier
                if nodo_actual.mover_izquier():
                    new_state, right_valor = nodo_actual.mover_izquier()
                    #Miro se el nodo ya ha sido visitado
                    if tuple(new_state.reshape(1,9)[0]) not in visitado:

                        #Creo nodo hijo
                        nodo_actual.mov_left = Node(state = new_state, parent = nodo_actual, action = 'derecha', depth = prof_actual + 1, step_cost = right_valor)

                        agenda.insert(0, nodo_actual.mov_left)
                        prof_agenda.insert(0, prof_actual + 1)
                        agenda_path_cost.insert(0, right_valor + path_cost_actual)







    
    








test = np.array([1,2,3,8,6,4,7,5,0]).reshape(3,3)
easy = np.array([1,3,4,8,6,2,7,0,5]).reshape(3,3)
medium = np.array([2,8,1,0,4,3,7,6,5]).reshape(3,3)
hard = np.array([5,6,7,4,0,8,3,2,1]).reshape(3,3)
ff = np.array([4,5,1,8,3,7,0,6,2]).reshape(3,3)

initial_state = ff
goal_state = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)
print (initial_state,'\n')
print (goal_state)

root_node = Node(state=initial_state,parent=None,action=None,depth=0,step_cost=0)
# search level by level with queue
root_node.busqueda_primero_Anchura(goal_state)
#root_node.busqueda_primero_Profundidad(goal_state)






        