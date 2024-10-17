- Cuaternion.cpp: Archivo que contiene la libreria Cuaternion
- Tests.cpp: Archivo de pruebas unitarias

Para las pruebas unitarias se hizo el intento de utilizar la libreria `Google Tests` sin embargo por fallas
tecnicas se procedio a hacer un cliente de forma manual. Para la cobertura del codigo, se utilizó la libreria `gcov`

Compilar y Ejecutar:
1. g++ -o Tests Tests.cpp
2. g++ -fprofile-arcs -ftest-coverage -o Tests Tests.cpp
3. .\Tests.exe
4. gcov Tests.cpp