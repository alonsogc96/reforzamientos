# 1. Crear una lista de 6 objetos y mostrar en pantalla
cursos = ["Matemáticas", "Programación", "Física", "Química", "Lenguaje", "Inglés"]
print("Lista de cursos:", cursos)

# Invertir y mostrar la lista de cursos
cursos_invertidos = cursos[::-1]
print("Lista de cursos invertida:", cursos_invertidos)

# 2. Agregar 4 objetos nuevos a la lista y quitar 2 por valor
cursos.append("Reds")
cursos.append("Business Intelligence")
cursos.append("Seguridad Informática")
cursos.append("Proyecto Integrador")

# Quitar 2 elementos por valor
cursos.remove("Lenguaje")
cursos.remove("Inglés")
print("Lista de cursos después de agregar y quitar:", cursos)

# 3. Obtener la cantidad total de ítems
cantidad_cursos = len(cursos)
print("Cantidad total de ítems en la lista:", cantidad_cursos)

# 4. Contar repeticiones de un curso y eliminar el primer ítem
cursos.append("Matemáticas")  # Agregamos "Matemáticas" nuevamente
repeticiones = cursos.count("Matemáticas")
print("Cantidad de veces que se repite 'Matemáticas':", repeticiones)

# Eliminar el primer ítem de la lista
del cursos[0]
print("Lista después de eliminar el primer ítem:", cursos)

# 5. Crear una nueva lista vacía y agregar 4 ítems de diferentes tipos de datos
nueva_lista = []
nueva_lista.append(3.14)  # float
nueva_lista.append(42)     # int
nueva_lista.append(True)   # bool
nueva_lista.append("Hola")  # string

# 6. Sumar las dos listas y mostrar el resultado
lista_total = cursos + nueva_lista
print("Lista total después de sumar:", lista_total)

# 7. Crear una lista desordenada y usar métodos de orden
lista_desordenada = [3, 1, 4, 2, 5]
lista_desordenada.sort()  # Ordenar la lista
print("Lista ordenada:", lista_desordenada)

# 8. Crear una lista con floats y bools, e imprimir penúltimo y último valor
lista_floats_bools = [3.14, 2.71, True, False, 1.62, 1.41]
print("Penúltimo valor:", lista_floats_bools[-2])
print("Último valor:", lista_floats_bools[-1])

# 9. Reconocer los tipos de cada dato en la lista
tipos_datos = [type(item) for item in lista_floats_bools]
print("Tipos de cada dato en la lista:", tipos_datos)

# 10. Eliminar todos los elementos de la lista creada previamente
lista_floats_bools.clear()
print("Lista después de eliminar todos los elementos:", lista_floats_bools) 

# 12. Crear una lista con los 15 primeros números impares
numeros_impares = [i for i in range(1, 30, 2)][:15]
numeros_impares.append(3.0)  # Agregar flotante repetido
numeros_impares.append(5.0)   # Agregar flotante repetido
numeros_impares.append(7.0)    # Agregar flotante repetido
numeros_impares.insert(3, "Python")  # Agregar cadena en la posición 3
del numeros_impares[3]  # Eliminar la cadena
print("Lista de números impares:", numeros_impares)

# 11. Mostrar datos entre la posición 10 y 35
# Datos entre la posición 5 y 10
print("Datos entre la posición 5 y 10:", numeros_impares[5:11])

# 13. Crear una lista vacía y pedir valores
ultima_lista = [0] * 10
for i in range(10):
    ultima_lista[i] = float(input(f"Ingrese el valor {i + 1}: "))
suma = sum(ultima_lista)
media = suma / len(ultima_lista)
print("Suma de los números:", suma)
print("Media de los números:", media)
