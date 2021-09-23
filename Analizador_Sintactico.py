from imagen import Imagen
from colorama import Fore, Back, Style
from imagenHTML import ImagenHtml
from Error import Error


class AnalizadorSintactico:
    
    def __init__(self):
        pass

    def analizar(self, lista):
        listaImagenes = []
        Errores = []
        
        i = 0
        
        while i < len(lista):

            nueva_imagen = Imagen(None,None,None,None,None,None,None)
            filas = 0
            columnas = 0
            dim = 0
            lista_celdas = []
            leyendo_celdas = False
            lista_filtros = []
            foundFila = False
            foundColumna = False
    
            
            
            while i < len(lista):
                
                if lista[i].lexema.upper() == "TITULO":
                    nueva_imagen.titulo = lista[i+2].lexema.upper()
                    
                elif lista[i].lexema.upper() == "ANCHO":
                    nueva_imagen.ancho = lista[i+2].lexema.upper()
                    
                elif lista[i].lexema.upper() == "ALTO":
                    nueva_imagen.alto = lista[i+2].lexema.upper()
                    
                elif lista[i].lexema.upper() == "FILAS":
                    nueva_imagen.filas = lista[i+2].lexema.upper()
                    dim +=1
                    filas = int(lista[i+2].lexema.upper())
                    foundFila = True
                    
                elif lista[i].lexema.upper() == "COLUMNAS":
                    nueva_imagen.columnas = lista[i+2].lexema.upper()
                    dim +=1
                    columnas = int(lista[i+2].lexema.upper())
                    foundColumna = True
                
                elif lista[i].lexema.upper() == "CELDAS":
                    
                    leyendo_celdas = True
                    for j1 in range(filas):
                        column = []
                        for i1 in range(columnas):
                            column.append(0)
                        lista_celdas.append(column)
                
                elif lista[i].lexema.upper() == "[" and leyendo_celdas and dim == 2:
                    fila = int(lista[i+3].lexema)
                    columna = int(lista[i+1].lexema)
                
                    try:
                                                            
                        if lista[i+5].lexema.upper() == "TRUE":
                            lista_celdas[fila][columna] = lista[i+7].lexema
                        elif lista[i+5].lexema.upper() == "FALSE":
                            lista_celdas[fila][columna] = "#FFFFFF"
                            
                    except IndexError:
                        Errores.append(Error("Celda (" + str(columna) + ","+ str(fila) +") fuera de rango", None, None))
                        pass
                                    
                elif lista[i].lexema.upper() == "MIRRORX":
                    lista_filtros.append("MIRRORX")
                
                elif lista[i].lexema.upper() == "MIRRORY":
                    lista_filtros.append("MIRRORY")
                
                elif lista[i].lexema.upper() == "DOUBLEMIRROR":
                    lista_filtros.append("DOUBLEMIRROR")

                elif lista[i].lexema.upper() == "@@@@":
                    nueva_imagen.celdas = lista_celdas
                    nueva_imagen.filtros = lista_filtros
                    
                    if nueva_imagen.titulo is None or nueva_imagen.ancho is None or nueva_imagen.alto is None or nueva_imagen.filas is None or nueva_imagen.columnas is None or nueva_imagen.celdas is None:
                        print("Imagen no Valida")
                        i+=1
                        break
                    else:
                        listaImagenes.append(nueva_imagen)
                        i+=1
                        break

                i += 1
            
            if foundColumna is False:
                Errores.append(Error('Token "COLUMNA" no encontrado', None, None))
                
            if foundFila is False:
                Errores.append(Error('Token "FILA" no encontrado', None, None))
        

        
        for imagen in listaImagenes:
            
            test = ImagenHtml(imagen.get_celdas(),imagen.get_ancho(), imagen.get_alto(),imagen.get_titulo(), imagen.get_filtros())
            test.generarHTML()
            
        return (listaImagenes,Errores)
            
            
            # print("Filtros:", imagen.filtros)

            
            
                    
        
        
    