# Manejador de tablas de metodos virtuales

class_definitions = {}

# Funcion para definir la clase
def define_class(class_name, methods, base_class=None):
    if class_name in class_definitions:
        print(f"Error: Clase '{class_name}' ya existe")
        return

    if base_class and base_class not in class_definitions:
        print(f"Error: Clase base '{base_class}' no existe")
        return

    if len(methods) != len(set(methods)):
        print("Error: Definiciones repetidas en la lista de nombres de métodos")
        return

    if base_class and check_cycle(class_name, base_class):
        print("Error: Se genera un ciclo")
        return

    class_definitions[class_name] = {
        "methods": methods,
        "base_class": base_class
    }
    print(f"Clase '{class_name}' definida con metodos {methods} y base '{base_class}'")

# Funcion para chequear si existe un ciclo
def check_cycle(class_name, base_class):
    visited = set()
    while base_class:
        if base_class in visited:
            return True
        visited.add(base_class)
        base_class = class_definitions[base_class]["base_class"]
    return False

# Funcion para calcular la tabla de metodos
def get_method_table(class_name):
    method_table = {}
    while class_name:
        class_info = class_definitions[class_name]
        for method in class_info["methods"]:
            if method not in method_table:
                method_table[method] = class_name
        class_name = class_info["base_class"]
    return method_table

# Funcion para mostrar la tabla de metodos
def describe_class(class_name):
    if class_name not in class_definitions:
        print(f"Error: Clase '{class_name}' no existente")
        return
    method_table = get_method_table(class_name)
    for method, origin in method_table.items():
        print(f"{method} -> {origin} :: {method}")

# Funcion para manejar la entrada del comando CLASS
def handle_class_command(args):
    if len(args) < 2:
        print("Error: Entrada invalida")
        return

    class_name = args[0]
    methods = args[1:]
    base_class = None

    if ":" in args[1]:
        base_class = args[2]
        methods = args[3:]
    define_class(class_name, methods, base_class)

# Funcion para manejar los argumentos del comando DESCRIBIR
def handle_describe_command(args):
    if len(args) != 1:
        print("Error: Entrada invalida")
        return
    class_name = args[0]
    describe_class(class_name)
    

def Simulador():
    while True:
        action = input("$> Ingrese una accion: ").strip().split()
        if not action:
            continue
        command = action[0].upper()
        args = action[1:]
        if command == "CLASS":
            handle_class_command(args)
        elif command == "DESCRIBIR":
            handle_describe_command(args)
        elif command == "SALIR":
            break
        else:
            print("Error: Entrada Invalida")

if __name__ == "__main__":
    Simulador()