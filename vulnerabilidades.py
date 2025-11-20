import os
import re

# Vulnerabilidad 1: Inyección de comandos
def ejecutar_comando(cmd):
    os.system(cmd)


# Vulnerabilidad 2: Expresión regular peligrosa (ReDoS)
def validar_usuario(texto):
    patron = r'(a+)+$'
    return re.match(patron, texto)


# Vulnerabilidad 3: evaluación insegura de expresiones
def calcular(expresion):
    return eval(expresion)


# Vulnerabilidad 4: escritura insegura de archivos
def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as f:
        f.write(contenido)


# Vulnerabilidad 5: salida sin sanitizar
def saludar(usuario):
    print("Bienvenido " + usuario)
