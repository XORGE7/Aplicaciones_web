# Importación de un módulo que se encuentra en la misma ruta:
from modulos1 import multiplicar, dividir, canal
# Importación desde un paquete:
# import mi_paquete.funciones_matematicas
import mi_paquete.funciones_matematicas as fun_mat
# from mi_paquete.funciones_matematicas import calcular_factorial, frase
# Importación de un sub paquete:
from mi_paquete.sub_paquete1.funciones_avanzadas import contar_letras

import datetime
from datetime import datetime

import modulos1

print(modulos1.multiplicar(7, 8))
print(modulos1.sumar(7, 8))
print(modulos1.restar(7, 8))
print(modulos1.dividir(7, 8))
""""

print(multipliar(19, 2))
print(canal)
print(fun_mat.calcular_factorial(5))
print(fun_mat.frase)

texto = "Gracias por apoyar mi canal!"
print(contar_letras(texto))