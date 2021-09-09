class Imagen:
    
    def __init__(self,titulo, ancho, alto, filas, columnas, celdas, filtros):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas
        self.filtros = filtros
        
    def get_titulo(self):
        return self.titulo

    def get_ancho(self):
        return int(self.ancho)

    def get_alto(self):
        return int(self.alto)
    
    def get_filas(self,):
        return self.filas
    
    def get_columnas(self):
        return self.columnas

    def get_celdas(self):
        return self.celdas 
    
    def get_filtros(self):
        return self.filtros 
    
    
    def set_titulo(self,titulo):
        self.titulo = titulo

    def set_ancho(self,ancho):
        self.ancho = ancho

    def set_alto(self,alto):
        self.alto = alto
    
    def set_filas(self,filas):
        self.filas = filas
    
    def set_columnas(self,columnas):
        self.columnas = columnas
        
    def set_celdas(self,celdas):
        self.celdas = celdas
    
    def set_filtros(self,filtros):
        self.filtros = filtros
        
    
    