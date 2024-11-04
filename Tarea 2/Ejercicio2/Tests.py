# CI-3641 Lenguajes de Programación
# Alumno: Jesus Gutierrez
# Carnet: 20-10332
# Pregunta 2 Pruebas Unitarias

import pytest
import coverage
from pre_post_fijo import Solver, Simulador

def test_simulador_calcular_prefijo(monkeypatch, capsys):
    inputs = iter(["EVAL PRE + * + 3 4 5 7", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "42" in captured.out
    
def test_simulador_mostrar_prefijo(monkeypatch, capsys):
    inputs = iter(["MOSTRAR PRE + * + 3 4 5 7", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "(3 + 4) * 5 + 7" in captured.out

def test_simulador_calcular_postfijo(monkeypatch, capsys):
    inputs = iter(["EVAL POST 8 3 - 8 4 4 + * +", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "69" in captured.out
    
def test_simulador_mostrar_postfijo(monkeypatch, capsys):
    inputs = iter(["MOSTRAR POST 8 3 - 8 4 4 + * +", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "8 - 3 + 8 * (4 + 4)" in captured.out
    
def test_simulador_error(monkeypatch, capsys):
    inputs = iter(["MOSTRAR asdasdsd", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Secuencia de comandos no valida" in captured.out
    
def test_simulador_error2(monkeypatch, capsys):
    inputs = iter(["aasfasf", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Secuencia de comandos no valida" in captured.out
    
def test_simulador_error3(monkeypatch, capsys):
    inputs = iter(["EVAL sadassd", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Secuencia de comandos no valida" in captured.out
    
def test_simulador_error4(monkeypatch, capsys):
    inputs = iter(["MOSTRAR PRE - a 5 6", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Operador ingresado no valido" in captured.out

def test_simulador_error5(monkeypatch, capsys):
    inputs = iter(["EVAL sadassd", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Secuencia de comandos no valida" in captured.out
    
def test_simulador_error6(monkeypatch, capsys):
    inputs = iter(["", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Secuencia de comandos no valida" in captured.out
    
def test_simulador_error4(monkeypatch, capsys):
    inputs = iter(["MOSTRAR POST 5 6 - a", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "Operador ingresado no valido" in captured.out
    
def test_simulador_mostrar_postfijo2(monkeypatch, capsys):
    inputs = iter(["MOSTRAR POST 5 6 + 2 3 * 4 - * ", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "(5 + 6) * (2 * 3 - 4)" in captured.out
    
def test_simulador_mostrar_postfijo2(monkeypatch, capsys):
    inputs = iter(["MOSTRAR POST 1 2 * 3 + 3 4 * 7 + 5 6 * 4 + / + ", "SALIR"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Simulador()
    captured = capsys.readouterr()
    assert "1 * 2 + 3 + (3 * 4 + 7) / (5 * 6 + 4)" in captured.out
