import imgkit
from PIL import ImageTk, Image 


class ImagenHtml:
    
    def __init__(self, lista, ancho, alto, titulo, filtros):
        self.lista = lista
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.filtros = filtros
        
        self.string = ""
        
    def generarHTML(self):
        self.string=""
        
        self.string += '''
        
        <table style="border-collapse: collapse; " border="1">
        <tbody>
        '''
        
        for columna in self.lista:
            self.string +='''
            <tr>
            ''' 
            for j in columna:
                if str(j) == str("0"):
                    j = "#FFFFFF"
                self.string +='''
                    <td style="height:50px;width:50px;background-color: ''' +  str(j) +''';">&nbsp;</td>
                '''
            self.string +='''
            <tr>
            '''
  
        self.string +='''
        </tbody>
        </table>
        '''
        nombre = str("HTML\\" + self.titulo.replace('"', '') + ".html")
        nombre_imagen = str("Imagenes\\" + self.titulo.replace('"', '') + ".png")
        archivo = open(nombre,"w+")
        archivo.write(self.string)
        archivo.close()
        
        path_wkthmltoimage = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'
        config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
        options = {
            'crop-w': f'{int(len(self.lista[0]))*54}',
            'crop-x': '0',
            'crop-y': '0',
        }
        
        imgkit.from_url(nombre, nombre_imagen, config=config, options=options)
        image = Image.open(nombre_imagen)
        resized = image.resize((self.ancho,self.alto),Image.ANTIALIAS)
        resized.save(nombre_imagen)
        
        
        for filtro in self.filtros:
            if filtro == "MIRRORX":             
                new_list = self.lista
                
                self.string=""
                self.string += '''
                
                <table style="border-collapse: collapse; " border="1">
                <tbody>
                '''
                
                for columna in new_list:
                    self.string +='''
                    <tr>
                    '''
                    
                    for j in reversed(columna):
                        if str(j) == str("0"):
                            j = "#FFFFFF"
                        self.string +='''
                            <td style="height:50px;width:50px;background-color: ''' +  str(j) +''';">&nbsp;</td>
                        '''
                    
                    self.string +='''
                    <tr>
                    '''
        
                self.string +='''
                </tbody>
                </table>
                '''
                nombre = str("HTML\\" + self.titulo.replace('"', '') + "_MIRRORX.html")
                nombre_imagen = str("Imagenes\\" + self.titulo.replace('"', '') + "_MIRRORX.png")
                archivo = open(nombre,"w+")
                archivo.write(self.string)

                path_wkthmltoimage = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'
                config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
                
                
                options = {
                    'crop-w': f'{int(len(self.lista[0]))*54}',
                    'crop-x': '0',
                    'crop-y': '0',
                }
                
                imgkit.from_url(nombre, nombre_imagen, config=config, options=options)
                image = Image.open(nombre_imagen)
                resized = image.resize((self.ancho,self.alto),Image.ANTIALIAS)
                resized.save(nombre_imagen)
        
            elif filtro == "MIRRORY":  
                new_list = self.lista
                
                self.string=""
                self.string += '''
                
                <table style="border-collapse: collapse; " border="1">
                <tbody>
                '''
                
                for columna in reversed(new_list):
                    self.string +='''
                    <tr>
                    '''
                    
                    for j in columna:
                        if str(j) == str("0"):
                            j = "#FFFFFF"
                        self.string +='''
                            <td style="height:50px;width:50px;background-color: ''' +  str(j) +''';">&nbsp;</td>
                        '''
                    
                    self.string +='''
                    <tr>
                    '''
        
                self.string +='''
                </tbody>
                </table>
                '''
                nombre = str("HTML\\" + self.titulo.replace('"', '') + "_MIRRORY.html")
                nombre_imagen = str("Imagenes\\" + self.titulo.replace('"', '') + "_MIRRORY.png")
                archivo = open(nombre,"w+")
                archivo.write(self.string)
                
                path_wkthmltoimage = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'
                config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
                
                
                options = {
                    'crop-w': f'{int(len(self.lista[0]))*54}',
                    'crop-x': '0',
                    'crop-y': '0',
                }
                
                imgkit.from_url(nombre, nombre_imagen, config=config, options=options)
                image = Image.open(nombre_imagen)
                resized = image.resize((self.ancho,self.alto),Image.ANTIALIAS)
                resized.save(nombre_imagen)
        
            elif filtro == "DOUBLEMIRROR":         
                new_list = self.lista
                
                self.string=""
                self.string += '''
                
                <table style="border-collapse: collapse; " border="1">
                <tbody>
                '''
                
                for columna in reversed(new_list):
                    self.string +='''
                    <tr>
                    '''
                    
                    for j in reversed(columna):
                        if str(j) == str("0"):
                            j = "#FFFFFF"
                        self.string +='''
                            <td style="height:50px;width:50px;background-color: ''' +  str(j) +''';">&nbsp;</td>
                        '''
                    
                    self.string +='''
                    <tr>
                    '''
        
                self.string +='''
                </tbody>
                </table>
                '''
                nombre = str("HTML\\" + self.titulo.replace('"', '') + "_DOUBLEMIRROR.html")
                nombre_imagen = str("Imagenes\\" + self.titulo.replace('"', '') + "_DOUBLEMIRROR.png")
                archivo = open(nombre,"w+")
                archivo.write(self.string)
                
                path_wkthmltoimage = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'
                config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
                
                
                options = {
                    'crop-w': f'{int(len(self.lista[0]))*54}',
                    'crop-x': '0',
                    'crop-y': '0',
                }
                
                imgkit.from_url(nombre, nombre_imagen, config=config, options=options)
                image = Image.open(nombre_imagen)
                resized = image.resize((self.ancho,self.alto),Image.ANTIALIAS)
                resized.save(nombre_imagen)