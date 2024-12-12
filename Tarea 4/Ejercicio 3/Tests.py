import pytest
import coverage 
from io import StringIO 
# Importar el código a probar
from Manejador import define_class, describe_class, handle_class_command, handle_describe_command, class_definitions, Simulador
from unittest.mock import patch
def test_define_class():
    class_definitions.clear()
    
    # Definir una clase sin superclase
    define_class('Clase1', ['metodo1', 'metodo2'])
    assert 'Clase1' in class_definitions
    assert class_definitions['Clase1']['methods'] == ['metodo1', 'metodo2']
    assert class_definitions['Clase1']['base_class'] is None
    
    # Intentar redefinir la misma clase
    define_class('Clase1', ['metodo3'])
    assert len(class_definitions) == 1  # No se debe redefinir
    
    # Definir una clase con superclase
    define_class('Clase2', ['metodo3'], 'Clase1')
    assert 'Clase2' in class_definitions
    assert class_definitions['Clase2']['methods'] == ['metodo3']
    assert class_definitions['Clase2']['base_class'] == 'Clase1'
    
    # Intentar definir una clase con superclase inexistente
    define_class('Clase3', ['metodo4'], 'NoExiste')
    assert 'Clase3' not in class_definitions

def test_check_cycle():
    class_definitions.clear()
    
    define_class('A', [])
    define_class('B', [], 'A')
    define_class('C', [], 'B')
    
    # Intentar definir una clase que cause un ciclo
    define_class('A', [], 'C')
    assert 'A' in class_definitions
    assert class_definitions['A']['base_class'] is None  # No debe cambiar

def test_describe_class():
    class_definitions.clear()
    
    define_class('Clase1', ['metodo1', 'metodo2'])
    define_class('Clase2', ['metodo3'], 'Clase1')
    
    # Capturar la salida de describe_class
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    describe_class('Clase2')
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert 'metodo3 -> Clase2 :: metodo3' in output
    assert 'metodo1 -> Clase1 :: metodo1' in output
    assert 'metodo2 -> Clase1 :: metodo2' in output

def test_handle_class_command():
    class_definitions.clear()
    
    handle_class_command(['Clase1', 'metodo1', 'metodo2'])
    assert 'Clase1' in class_definitions
    assert class_definitions['Clase1']['methods'] == ['metodo1', 'metodo2']
    
    handle_class_command(['Clase2', ':', 'Clase1', 'metodo3'])
    assert 'Clase2' in class_definitions
    assert class_definitions['Clase2']['methods'] == ['metodo3']
    assert class_definitions['Clase2']['base_class'] == 'Clase1'

def test_handle_describe_command():
    class_definitions.clear()
    
    define_class('Clase1', ['metodo1', 'metodo2'])
    
    # Capturar la salida de handle_describe_command
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    handle_describe_command(['Clase1'])
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert 'metodo1 -> Clase1 :: metodo1' in output
    assert 'metodo2 -> Clase1 :: metodo2' in output
@pytest.fixture   
def setup_classes():
    class_definitions.clear()
    yield
    class_definitions.clear()


def test_simulador_class_command(monkeypatch, setup_classes):
    inputs = iter(["CLASS Clase1 metodo1 metodo2", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('builtins.input', lambda _: next(inputs)):
        Simulador()

    assert 'Clase1' in class_definitions
    assert class_definitions['Clase1']['methods'] == ['metodo1', 'metodo2']

def test_simulador_describe_command(monkeypatch, capsys, setup_classes):
    inputs = iter(["CLASS Clase1 metodo1 metodo2", "DESCRIBIR Clase1", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('builtins.input', lambda _: next(inputs)):
        Simulador()

    captured = capsys.readouterr()
    assert "metodo1 -> Clase1 :: metodo1" in captured.out
    assert "metodo2 -> Clase1 :: metodo2" in captured.out

def test_simulador_invalid_command(monkeypatch, capsys):
    inputs = iter(["INVALID COMMAND", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('builtins.input', lambda _: next(inputs)):
        Simulador()

    captured = capsys.readouterr()
    assert "Error: Comando no valido" in captured.out

def test_simulador_exit(monkeypatch):
    inputs = iter(["SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('builtins.input', lambda _: next(inputs)):
        Simulador()

if __name__ == "__main__":
    pytest.main()