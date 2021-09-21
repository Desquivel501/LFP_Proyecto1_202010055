from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexico:
    
    
    
    def __init__(self):
        self.reservadas = ["TITULO", "ANCHO", "ALTO", "FILAS", "COLUMNAS", "CELDAS", "FILTROS", "MIRRORX", "MIRRORY", "DOUBLEMIRROR"]
        self.simbolos = ["@", ";", ",", "=", "{", "}", "[", "]"]
        self.listaTokens = [] 
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0
        self.contHex = 0
        self.contArroba = 0
    
    def agregarToken(self, caracter, token, linea, columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''
    
    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))
        self.buffer = ''
        
    def estado0(self,caracter):
        if caracter.isalpha():
            self.buffer += caracter 
            self.columna += 1
            self.estado = 2
        
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
            self.estado = 1

        elif caracter == "\"":
            self.buffer += caracter
            self.columna += 1
            self.estado = 3
        
        elif caracter == "#":
            self.buffer += caracter
            self.columna += 1
            self.estado = 6
        
        elif caracter == "@":
            self.buffer += caracter 
            self.columna += 1
            self.estado = 7

        elif caracter in self.simbolos:
            if caracter == ";":
                self.agregarToken(str(caracter), "Punto y Coma", self.linea, self.columna)
            elif caracter == ",":
                self.agregarToken(str(caracter), "Coma", self.linea, self.columna)
            elif caracter == "=":
                self.agregarToken(str(caracter), "Igual", self.linea, self.columna)
            elif caracter == "{":
                self.agregarToken(str(caracter), "Llave Izquierda", self.linea, self.columna)
            elif caracter == "}":
                self.agregarToken(str(caracter), "Llave Derecha", self.linea, self.columna)
            elif caracter == "[":
                self.agregarToken(str(caracter), "Corchete Izquierdo", self.linea, self.columna)
            elif caracter == "]":
                self.agregarToken(str(caracter), "Corchete Derecho", self.linea, self.columna)
                
            self.buffer = ''
            self.columna+=1
        
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
            
        elif caracter in ['\t',' ']:
            self.columna += 1      
            
        elif caracter == '\r':
            pass
        
        elif caracter == '&':
            print('Se aceptó la cadena!')
            pass      
        
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.columna += 1 

    #Numero    
    def estado1(self,caracter):
        if caracter.isdigit():
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregarToken(self.buffer,'Entero',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1
    
    #Palabra
    def estado2(self,caracter):
        if caracter.isalpha():
            self.buffer +=caracter
            self.columna += 1  
        else:
            if self.palabraReservada():
                self.agregarToken(self.buffer.strip(), self.buffer.strip(), self.linea, self.columna)
                self.estado = 0
                self.columna+=1
                self.i -= 1
                
            elif self.buffer.upper() in ["TRUE", "FALSE"]:
                self.agregarToken(self.buffer, "Boolean", self.linea, self.columna)
                self.estado = 0
                self.columna+=1
                self.i -= 1
            
            else:
                
                self.agregar_error(self.buffer, self.linea, self.columna)
                self.estado = 0
                self.columna+=1
                self.i -= 1   
        
    #Cadena entre comillas
    def estado3(self,caracter):
        if caracter != "\"":           
            self.buffer +=caracter
            self.columna += 1 
        else:
            self.buffer +=caracter
            self.agregarToken(self.buffer, "Cadena", self.linea, self.columna)
            self.estado = 0
            self.columna+=1    
    
    #Simbolos
    def estado5(self, caracter):
        if caracter == ";":
            self.agregarToken(str(caracter), "Punto y Coma", self.linea, self.columna)
        elif caracter == ",":
            self.agregarToken(str(caracter), "Coma", self.linea, self.columna)
        elif caracter == "=":
            self.agregarToken(str(caracter), "Igual", self.linea, self.columna)
        elif caracter == "{":
            self.agregarToken(str(caracter), "Llave Izquierda", self.linea, self.columna)
        elif caracter == "}":
            self.agregarToken(str(caracter), "Llave Derecha", self.linea, self.columna)
        elif caracter == "[":
            self.agregarToken(str(caracter), "Corchete Izquierdo", self.linea, self.columna)
        elif caracter == "]":
            self.agregarToken(str(caracter), "Corchete Derecho", self.linea, self.columna)
        
        self.buffer =""
        self.columna += 1 
        self.estado = 0
    
    #Color Hex
    def estado6(self,caracter):
        if (caracter.isalpha() or caracter.isdigit()) and self.contHex < 6:
            self.contHex += 1    
            self.buffer +=caracter
            self.columna += 1 
        else:
            self.contHex = 0
            self.agregarToken(self.buffer, "Color Hex", self.linea, self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1  
    
    #Arrobas
    def estado7(self,caracter, final):
        if caracter == "@":
            self.contArroba += 1
            self.buffer +=caracter
            self.columna += 1
        else:
            if self.contArroba != 3:
                self.contArroba = 0
                self.estado = 0
                self.columna += 1 
                if final:
                    pass
                else:
                    self.agregar_error(self.buffer,self.linea,self.columna)
            
            else:
                self.contArroba = 0
                self.agregarToken(self.buffer, "Arrobas", self.linea, self.columna)
                print("here")
                self.estado = 0
                self.columna+=1  
        
          
    def palabraReservada(self):
        if self.buffer.upper() in self.reservadas:
            return True
        else:
            return False
        
    def analizar(self,cadena):
        self.listaTokens = [] 
        self.listaErrores = []
        
        self.i = 0
        
        while self.i < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.i])
            elif self.estado == 1:
                self.estado1(cadena[self.i])
            elif self.estado == 2:
                self.estado2(cadena[self.i])
            elif self.estado == 3:
                self.estado3(cadena[self.i])
            # elif self.estado == 4:
            #     self.estado4(cadena[self.i])
            elif self.estado == 5:
                self.estado5(cadena[self.i])
            elif self.estado == 6:
                self.estado6(cadena[self.i])
            elif self.estado == 7:
                self.estado7(cadena[self.i], False)
            self.i += 1

        
        last = len(self.listaTokens)-1
        if self.listaTokens[last] != "@@@@":
            self.listaTokens.append(Token("@@@@","Arrobas", self.listaTokens[last].linea+1, 1))
        
        return (self.listaTokens,self.listaErrores)
        
    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviar())
        print(x)

    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviar())
            print(x)
