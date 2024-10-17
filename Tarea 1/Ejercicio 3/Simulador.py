# CI-3641 Lenguajes de Programación
# Alumno: Jesus Gutierrez
# Carnet: 20-10332
# Pregunta 3

class Programa:
    """
    Clase Programa 
    
    Esta clase representa un programa de escrito en un lenguaje 'x'.

    Atributos:
    -----------
        nombre : str 
            El nombre del programa.
        lenguaje : str 
            El lenguaje de programación en el que está escrito el programa.

    Métodos:
    --------
        __init__(self, nombre, lenguaje): Inicializa una instancia de la clase Programa con el nombre y el lenguaje especificados.
    """
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

class Interprete:
    """
    Clase Interprete

    Esta clase representa un intérprete que traduce de un lenguaje base a un lenguaje objetivo.

    Atributos:
    -----------
    lenguaje_base : str
        El lenguaje de programación base desde el cual se traducirá.
    lenguaje_target : str
        El lenguaje de programación objetivo al cual se traducirá.

    Métodos:
    --------
    __init__(self, lenguaje_base, lenguaje_target)
        Inicializa una instancia del intérprete con los lenguajes especificados.
    """
    def __init__(self, lenguaje_base, lenguaje_target):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_target = lenguaje_target

        
class Traductor:
    """
    Clase Traductor

    Esta clase representa un traductor, escrito en un lenguaje base, que puede convertir texto 
    de un lenguaje origen a un lenguaje destino

    Atributos:
    -----------
    lenguaje_base : str
        El lenguaje en el que esta escrito el traductor.
    lenguaje_origen : str
        El lenguaje del cual se va a traducir.
    lenguaje_destino : str
        El lenguaje al cual se va a traducir.

    Métodos:
    --------
    __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        Inicializa una instancia de la clase Traductor con los attributos especificados.
    """
    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino

class Maquina:
    """
    Clase Maquina
    
    Esta clase simula una máquina que puede definir y ejecutar programas en diferentes lenguajes de programación. 
    Permite definir programas, intérpretes y traductores, y verificar si un programa es ejecutable en el entorno actual.
    
    Atributos:
    ----------
    LOCAL : str 
        Constante que representa el lenguaje local de la máquina.
    programas : dict 
        Diccionario que almacena los programas definidos, con el nombre del programa como clave.
    interpretes : list 
        Lista que almacena los intérpretes definidos.
    traductores : list 
        Lista que almacena los traductores definidos.
    """
    LOCAL = "LOCAL"

    def __init__(self):
        self.programas = {}
        self.interpretes = []
        self.traductores = []

    def definirPrograma(self, nombre, lenguaje):
        """
        Define un nuevo programa y lo agrega a la lista de programas.

        Args:
            nombre (str): El nombre del programa a definir.
            lenguaje (str): El lenguaje en el que el programa es ejecutable.

        Returns:
            None

        Prints:
            Mensaje de error si el programa ya está definido.
            Mensaje de confirmación si el programa se define correctamente.
        """
        if nombre in self.programas:
            print(f" Error: El programa '{nombre}' ya está definido")
            return
        self.programas[nombre] = Programa(nombre, lenguaje)
        print(f" Se definió el programa '{nombre}', ejecutable en '{lenguaje}'")

    def definirInterprete(self, lenguaje_base, lenguaje_target):
        """
        Define un intérprete para un lenguaje de programación objetivo.

        Args:
            lenguaje_base (str): El lenguaje de programación en el que está escrito el intérprete.
            lenguaje_target (str): El lenguaje de programación que el intérprete puede ejecutar.

        Returns:
            None
        
        Prints:
            Mensaje de confirmación si el programa se define correctamente.
        """
        self.interpretes.append(Interprete(lenguaje_base, lenguaje_target))
        print(f" Se definió un intérprete para '{lenguaje_target}', escrito en '{lenguaje_base}'")

    def definirTraductor(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        """
        Define un nuevo traductor y lo agrega a la lista de traductores.

        Args:
            lenguaje_base (str): El lenguaje en el que está escrito el traductor.
            lenguaje_origen (str): El lenguaje de origen que el traductor puede traducir.
            lenguaje_destino (str): El lenguaje de destino al que el traductor puede traducir.

        Returns:
            None
            
        Prints:
            Mensaje de confirmación si el programa se define correctamente.
        """
        self.traductores.append(Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino))
        print(f" Se definió un traductor de '{lenguaje_origen}' hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")


    def existeInterprete(self, lenguaje_origen, visitados=None):
        """
        Verifica si existe un intérprete que pueda traducir desde el lenguaje de origen al lenguaje local.
        Args:
            lenguaje_origen (str): El lenguaje desde el cual se desea traducir.
            visitados (set, opcional): Un conjunto de lenguajes ya visitados para evitar ciclos. Por defecto es None.
        Returns:
            bool: True si existe un intérprete que pueda traducir desde el lenguaje de origen al lenguaje local, False en caso contrario.
        """
        
        lenguaje_destino = self.LOCAL
        
        if visitados is None:
            visitados = set()
        
        if lenguaje_origen == lenguaje_destino:
            return True

        # Evitar ciclos
        if lenguaje_origen in visitados:
             return False

        visitados.add(lenguaje_origen)

        # Buscamos si hay un interprete directo
        if any(i.lenguaje_base == lenguaje_destino and i.lenguaje_target == lenguaje_origen for i in self.interpretes):
            return True

        # Buscamos interpretes que tengan lenguaje_origen como lenguaje_base
        for interprete in self.interpretes:
            if interprete.lenguaje_target == lenguaje_origen:
                if self.existeInterprete(interprete.lenguaje_base, visitados):
                    return True

        return False
        
    def esEjecutable(self, nombre_programa):
        """
        Verifica si un programa es ejecutable en el entorno actual.
        
        Args:
            nombre_programa (str): El nombre del programa que se desea verificar.
        
        Returns:
            bool: True si el programa es ejecutable, False en caso contrario.
        
        Comportamiento:
            - Si el programa no está definido en el entorno, imprime un mensaje de error y retorna False.
            - Si el programa está escrito en el lenguaje local o existe un intérprete para su lenguaje, retorna True.
            - Si no hay intérprete disponible, busca traductores que puedan traducir el programa a un lenguaje para el cual exista un intérprete.
            - Si encuentra un traductor adecuado, verifica si existe un intérprete para el lenguaje destino o para el lenguaje base del traductor.
            - Si se cumplen las condiciones anteriores, retorna True. En caso contrario, retorna False.
        """
        if nombre_programa not in self.programas:
            print(f" Error: El programa '{nombre_programa}' no está definido")
            return

        # Chequeamos interpretes
        programa = self.programas[nombre_programa]
        if programa.lenguaje == self.LOCAL or self.existeInterprete(programa.lenguaje):
            return True
        
        # Chequeamos traductores
        traductores_disponibles = [t for t in self.traductores if t.lenguaje_origen == programa.lenguaje]
        for traductor in traductores_disponibles:
            if self.existeInterprete(traductor.lenguaje_destino):
                if self.existeInterprete(traductor.lenguaje_base):
                    return True
                elif self.buscar_traductor(traductor.lenguaje_base):
                    return True
        
        return False
        
    def buscar_traductor(self, lenguaje_base_traductor):
        """
        Busca un traductor disponible que pueda traducir desde el lenguaje base especificado.

        Args:
            lenguaje_base_traductor (str): El lenguaje base desde el cual se desea traducir.

        Returns:
            bool: True si se encuentra un traductor que pueda traducir desde el lenguaje base especificado
                  y cuyo lenguaje destino sea ejecutable, de lo contrario False.
        """
        traductores_disponibles = [t for t in self.traductores if t.lenguaje_origen == lenguaje_base_traductor]
        for traductor in traductores_disponibles:
            if self.existeInterprete(traductor.lenguaje_destino):
                if self.existeInterprete(traductor.lenguaje_base):
                    return True
            else:
                if self.buscar_traductor(traductor.lenguaje_destino):
                    return True
        return False

        
  
def Simulador():
    """
    Simula una máquina que puede definir programas, intérpretes y traductores, 
    y verificar si un programa es ejecutable. 
    
    Comandos disponibles:
    - DEFINIR PROGRAMA <nombre> <lenguaje>: Define un programa con el nombre y la ruta especificados.
    - DEFINIR INTERPRETE <lenguaje_base> <lenguaje>: Define un intérprete con el nombre y la ruta especificados.
    - DEFINIR TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>: Define un traductor con el nombre, 
     el lenguaje de origen y el lenguaje de destino especificados.
    - EJECUTABLE <nombre>: Verifica si el programa con el nombre especificado es ejecutable.
    - SALIR: Termina la simulación.
    Si se introduce un comando no válido, se muestra un mensaje de error.
    
    """
    maquina = Maquina()
    while True:
        entrada = input("$> ")
        orden = entrada.split()
        comando = orden[0]
        
        if comando == "DEFINIR":
            
            if orden[1] == "PROGRAMA":
                maquina.definirPrograma(orden[2], orden[3])
            elif orden[1] == "INTERPRETE":
                maquina.definirInterprete(orden[2], orden[3])
            elif orden[1] == "TRADUCTOR":
                maquina.definirTraductor(orden[2], orden[3], orden[4])
            else:
                print(" Error. Entrada no válida")
                
        elif comando == "EJECUTABLE":
            if not maquina.esEjecutable(orden[1]): 
                print(f" No es posible ejecutar el programa '{orden[1]}'")
            else:    
                print(f" Sí, es posible ejecutar el programa '{orden[1]}'")
            
        elif comando == "SALIR":
            break
        
        else:
            print(" Error. Entrada no válida")
            

if __name__ == "__main__":
    Simulador()