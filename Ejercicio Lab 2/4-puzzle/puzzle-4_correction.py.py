# Puzle Lineal con búsqueda en profundidad
from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = {0,1}
    auxiliar = 0
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:        
        nodo = nodos_frontera.pop()        
        # extraer nodo y añadirlo a visitados

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()            
            # operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            auxiliar = hijo[0]*1000+hijo[1]*100+hijo[2]*10+hijo[3]
            hijo_izquierdo = Nodo(hijo)
            if not auxiliar in nodos_visitados:                
                nodos_frontera.append(hijo_izquierdo)
                nodos_visitados.add(auxiliar)
            # operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            auxiliar = hijo[0]*1000+hijo[1]*100+hijo[2]*10+hijo[3]
            hijo_central = Nodo(hijo)
            if not auxiliar in nodos_visitados:
                nodos_visitados.add(auxiliar)                
                nodos_frontera.append(hijo_central)
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            auxiliar = hijo[0]*1000+hijo[1]*100+hijo[2]*10+hijo[3]
            hijo_derecho = Nodo(hijo)
            if not auxiliar in nodos_visitados:
                nodos_visitados.add(auxiliar)               
                nodos_frontera.append(hijo_derecho)

            
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])           



if __name__ == "__main__":
    estado_inicial=[4,2,3,1]
    solucion=[1,2,3,4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)