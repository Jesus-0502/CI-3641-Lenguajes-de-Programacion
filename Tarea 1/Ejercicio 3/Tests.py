import pytest
import coverage
from Simulador import Programa, Traductor, Interprete, Maquina, Simulador

def test_programa():
    programa = Programa("fibonacci", "Python")
    assert programa.nombre == "fibonacci"
    assert programa.lenguaje == "Python"

def test_interprete():
    interprete = Interprete("Python", "Java")
    assert interprete.lenguaje_base == "Python"
    assert interprete.lenguaje_target == "Java"

def test_traductor():
    traductor = Traductor("Python", "Java", "C")
    assert traductor.lenguaje_base == "Python"
    assert traductor.lenguaje_origen == "Java"
    assert traductor.lenguaje_destino == "C"
    
def test_maquina0():
    maquina = Maquina()
    maquina.definirPrograma("fibonacci", "Python")
    assert maquina.esEjecutable("fibonacci") == False
    
    maquina.definirPrograma("factorial", "LOCAL")
    assert maquina.esEjecutable("factorial") == True

def test_maquina1():
    maquina = Maquina()
    maquina.definirPrograma("fibonacci", "Python")
    maquina.definirInterprete("Java", "Python")
    maquina.definirInterprete("LOCAL", "Java")
    assert maquina.esEjecutable("fibonacci") == True

def test_maquina2():
    maquina = Maquina()
    
    maquina.definirPrograma("factorial", "Java")
    assert maquina.esEjecutable("factorial") == False
    maquina.definirInterprete("C", "Java")
    maquina.definirTraductor("C", "Java", "C")
    assert maquina.esEjecutable("factorial") == False
    maquina.definirInterprete("LOCAL", "C")
    assert maquina.esEjecutable("factorial") == True
    
    maquina.definirPrograma("holamundo", "Python3")
    maquina.definirTraductor("wtf42", "Python3", "LOCAL")
    assert maquina.esEjecutable("holamundo") == False
    maquina.definirTraductor("C", "wtf42", "Java")
    assert maquina.esEjecutable("holamundo") == True
    

def test_maquinaErrores():
    maquina = Maquina()
    maquina.definirPrograma("factorial", "Java")
    assert maquina.definirPrograma("factorial", "Python") == None
    
    assert maquina.esEjecutable("holamundo") == None
    
def test_definir_programa(capsys):
    maquina = Maquina()
    maquina.definirPrograma("Programa1", "Python")
    captured = capsys.readouterr()
    assert "Se definió el programa 'Programa1', ejecutable en 'Python'" in captured.out

def test_definir_programa_duplicado(capsys):
    maquina = Maquina()
    maquina.definirPrograma("Programa1", "Python")
    maquina.definirPrograma("Programa1", "Python")
    captured = capsys.readouterr()
    assert "Error: El programa 'Programa1' ya está definido" in captured.out

def test_definir_interprete(capsys):
    maquina = Maquina()
    maquina.definirInterprete("Python", "Java")
    captured = capsys.readouterr()
    assert "Se definió un intérprete para 'Java', escrito en 'Python'" in captured.out

def test_definir_traductor(capsys):
    maquina = Maquina()
    maquina.definirTraductor("Python", "Java", "C++")
    captured = capsys.readouterr()
    assert "Se definió un traductor de 'Java' hacia 'C++', escrito en 'Python'" in captured.out

def test_esEjecutable_programa_no_definido(capsys):
    maquina = Maquina()
    maquina.esEjecutable("Programa1")
    captured = capsys.readouterr()
    assert "Error: El programa 'Programa1' no está definido" in captured.out

def test_esEjecutable_programa_ejecutable(capsys):
    maquina = Maquina()
    maquina.definirPrograma("Programa1", "LOCAL")
    assert maquina.esEjecutable("Programa1") == True

def test_esEjecutable_programa_no_ejecutable(capsys):
    maquina = Maquina()
    maquina.definirPrograma("Programa1", "Python")
    assert maquina.esEjecutable("Programa1") == False

def test_simulador_definir_programa(capsys, monkeypatch):
    inputs = iter(["DEFINIR PROGRAMA Programa1 Python", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Se definió el programa 'Programa1', ejecutable en 'Python'" in captured.out

def test_simulador_definir_interprete(capsys, monkeypatch):
    inputs = iter(["DEFINIR INTERPRETE Python Java", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Se definió un intérprete para 'Java', escrito en 'Python'" in captured.out

def test_simulador_definir_traductor(capsys, monkeypatch):
    inputs = iter(["DEFINIR TRADUCTOR Python Java C++", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Se definió un traductor de 'Java' hacia 'C++', escrito en 'Python'" in captured.out

def test_simulador_ejecutable(capsys, monkeypatch):
    inputs = iter(["DEFINIR PROGRAMA Programa1 LOCAL", "EJECUTABLE Programa1", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Sí, es posible ejecutar el programa 'Programa1'" in captured.out

def test_simulador_no_ejecutable(capsys, monkeypatch):
    inputs = iter(["DEFINIR PROGRAMA Programa1 Python", "EJECUTABLE Programa1", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "No es posible ejecutar el programa 'Programa1'" in captured.out
    
    