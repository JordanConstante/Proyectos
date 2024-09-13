from utilities import borrarPantalla,gotoxy, red_color,reset_color,green_color,yellow_color,blue_color,purple_color
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1, color="\033[97m", colornum="\033[97m"):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        self.color = color
        self.colornum = colornum
    
    def menu(self):
        gotoxy(self.col, self.fil)
        print(f"{self.color}{self.titulo}{reset_color}")
        
        self.col -= 5
        for i, opcion in enumerate(self.opciones, start=1):
            self.fil += 1
            gotoxy(self.col, self.fil)
            print(f"{self.colornum}{i}. {self.colornum}{opcion}{reset_color}")
        
        gotoxy(self.col + 5, self.fil + 2)
        opc = input(f"Elija opción [1...{len(self.opciones)}]: ")
        return opc

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def cedula():
        pass
    
class otra:
    pass    

if __name__ == '__main__':
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if(opciones_menu==1):
      numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
      print("Número validado:", numero_validado)
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)