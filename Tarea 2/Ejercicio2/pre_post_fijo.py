# CI-3641 Lenguajes de Programación
# Alumno: Jesus Gutierrez
# Carnet: 20-10332
# Pregunta 2

class Solver:
    
    # CALCULAR EL RESULTADO DADA LA EXPRESION EN PREFIJO
    def calcular_prefijo(self, expresion):
        self.pila = []
        for i in expresion[::-1]:
            if i.isdigit():
                self.pila.append(int(i))
            else:
                izquierda = self.pila.pop()
                derecha = self.pila.pop()
                resultado = eval(f"{izquierda}{i}{derecha}")
                self.pila.append(resultado)
        print(self.pila.pop())

    # CALCULAR EL RESULTADO DADA LA EXPRESION EN POSTFIJO
    def calcular_postfijo(self, expresion):
        self.pila = []
        for i in expresion:
            if i.isdigit():
                self.pila.append(int(i))
            else:
                derecha = self.pila.pop()
                izquierda = self.pila.pop()
                resultado = eval(f"{izquierda}{i}{derecha}")
                self.pila.append(resultado)
        print(self.pila.pop())
        
    # MOSTRAR EL INFIJO DADA LA EXPRESION EN PREFIJO
    def mostrar_prefijo(self, expresion):
        self.lista = []
        for index, i in enumerate(expresion[::-1]):
            if i.isdigit():
                self.lista.append(i)
            else:
                if i == "-" or i == "+":
                    if (index == len(expresion) - 1) or ((expresion[index + 1].isdigit() and expresion[index - 1].isdigit()) or 
                    ((expresion[index - 1].isdigit() or expresion[index - 1].isdigit() == False))):
                        izquierda = self.lista.pop()
                        derecha = self.lista.pop()
                        if i == "-" and len(derecha) > 2 and ("*" not in derecha and "/" not in derecha):
                            self.lista.append(f"{izquierda} {i} ({derecha})")
                        else:
                            self.lista.append(f"{izquierda} {i} {derecha}")
                    # else:     
                    #     print("HOLA")
                    #     izquierda = self.lista.pop()
                    #     derecha = self.lista.pop()
                    #     self.lista.append(f"({izquierda} {i} {derecha})")
                        
                elif i == "*" or i == "/": 
                    izquierda = self.lista.pop()
                    izquierda2 = izquierda.replace(" ", "")
                    
                    derecha = self.lista.pop()
                    derecha2 = derecha.replace(" ", "")
                    
                    if ("+" in derecha2 or "-" in derecha2) or ("*" not in derecha2 and "/" not in derecha2):
                        if (len(derecha2) == 1 and index != len(expresion) - 1) or (len(derecha2) == 1):
                            derecha = f"{derecha}"
                        else:
                            derecha = f"({derecha})"
                        
                    if ("+" in izquierda2 or "-" in izquierda2):
                        if ("*" in izquierda2 or "/" in izquierda2) and (index != len(expresion) - 1): 
                            izquierda = f"{izquierda}"
                        else:    
                            izquierda = f"({izquierda})"
                    
                    self.lista.append(f"{izquierda} {i} {derecha}")
                    
                else:
                    print("Operador ingresado no valido")
        print(self.lista[0])
        
    # MOSTRAR EL INFIJO DADA LA EXPRESION EN POSTFIJO 
    def mostrar_postfijo(self, expresion):
        self.lista = []
        for index, i in enumerate(expresion):
            if i.isdigit():
                self.lista.append(i)
            else:
                if i == "-" or i == "+":
                    if (index == len(expresion) - 1) or ((expresion[index + 1].isdigit() and expresion[index - 1].isdigit()) or 
                    ((expresion[index - 1].isdigit() or expresion[index - 1].isdigit() == False))):
                        derecha = self.lista.pop()
                        izquierda = self.lista.pop()
                        if i == "-" and len(derecha) > 2:
                            self.lista.append(f"{izquierda} {i} ({derecha})")
                        else:
                            self.lista.append(f"{izquierda} {i} {derecha}")
                    # else:
                    #     print("HOLA")
                    #     derecha = self.lista.pop()
                    #     izquierda = self.lista.pop()
                    #     self.lista.append(f"({izquierda} {i} {derecha})")
                        
                elif i == "*" or i == "/":
                    derecha = self.lista.pop()
                    derecha2 = derecha.replace(" ", "")
                    if ("+" in derecha2 or "-" in derecha2) and ("*" not in derecha2 or "/" not in derecha2):
                        derecha = f"({derecha})"
                       
                    izquierda = self.lista.pop()
                    izquierda2 = izquierda.replace(" ", "")
                    if ("+" in izquierda2 or "-" in izquierda2):
                        izquierda = f"({izquierda})"
                            
                    self.lista.append(f"{izquierda} {i} {derecha}")
                    
                else:
                    print("Operador ingresado no valido")
        print(self.lista[0])
    
        

def Simulador():
    
    solver = Solver()
    
    while True:
        entrada = input("$> ")
        orden = entrada.split()
        if orden == []:
            print("Secuencia de comandos no valida")
            
        else: 
            match orden[0]:
                case "EVAL":
                    match orden[1]:
                        case "PRE":
                            expresion = "".join(orden[2:]).replace(" ", "")
                            print(expresion)
                            solver.calcular_prefijo(expresion)
                        case "POST":
                            expresion = "".join(orden[2:]).replace(" ", "")
                            solver.calcular_postfijo(expresion)
                        case _:
                            print("Secuencia de comandos no valida")

                case "MOSTRAR":
                    match orden[1]:
                        case "PRE":
                            expresion = "".join(orden[2:]).replace(" ", "")
                            solver.mostrar_prefijo(expresion)
                        case "POST":
                            expresion = "".join(orden[2:]).replace(" ", "")
                            solver.mostrar_postfijo(expresion)
                        case _:
                            print("Secuencia de comandos no valida")
                            
                case "SALIR":
                    break
                case _:
                    print("Secuencia de comandos no valida")

if __name__ == "__main__":
    Simulador()