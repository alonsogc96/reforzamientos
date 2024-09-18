# 1. Crear un diccionario con los campos: nombre, edad, salario
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "salario": 5000
}
print("Diccionario inicial:", diccionario)

# 2. Convertir el diccionario a una lista
lista = list(diccionario.items())
print("Lista convertida del diccionario:", lista)

# 3. Agregar un nuevo key llamado “dni” y mostrar el valor de salario
diccionario["dni"] = "01237454"
print("Salario:", diccionario["salario"])

# 4. Eliminar el key 'edad' del diccionario
del diccionario["edad"]
print("Diccionario después de eliminar 'edad':", diccionario)

# 5. Convertir el diccionario a una lista y mostrar el tipo de datos final
lista_final = list(diccionario.items())
print("Lista final del diccionario:", lista_final)
print("Tipo de datos de la lista final:", type(lista_final))

# 6. Crear un diccionario con los mismos valores sin apuntar a una variable
nuevo_diccionario = dict([("nombre", "Juan"), ("salario", "5000"), ("dni", "01237454")])
print("Nuevo diccionario:", nuevo_diccionario)

# 7. Crear un diccionario con 6 departamentos
departamentos = {
    "Departamento1": "Lima",
    "Departamento2": "Junín",
    "Departamento3": "Arequipa",
    "Departamento4": "Cusco",
    "Departamento5": "Loreto",
    "Departamento6": "Ica"
}

# Borrar un departamento usando 'del'
del departamentos["Departamento3"]
print("Departamentos después de borrar uno:", departamentos)

# Comprobar que no existe el departamento borrado
if "Departamento3" not in departamentos:
    print("Departamento3 no existe en el diccionario.")

# 8. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario
carrera = "Ingeniería Empresarial y de Sistemas"
nuevo_diccionario["carrera"] = carrera

# Mostrar en consola los valores del diccionario final
print("Diccionario final:", nuevo_diccionario)
