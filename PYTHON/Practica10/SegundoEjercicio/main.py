from Ministerio import Ministerio
# a)
ministerio1 = Ministerio("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio")
ministerio2 = Ministerio("Luna", "Estación Luna, Estación 16 de Julio")

empleados = [
    ("Pedro", 35, 2500),
    ("Rojas", 43, 3250),
    ("Lucy", 43, 3250),
    ("Ana", 26, 2700),
    ("Sosa", 26, 2700),
    ("Saul", 29, 2500),
    ("Arce", 29, 2500),
    ("Calle", 29, 2500)
]
for nombre, edad, sueldo in empleados:
    ministerio1.agregar_empleado(nombre, edad, sueldo)
# b)
ministerio1.eliminar_empleado("Rojas")
# c)
ministerio1.transferir_empleado(ministerio2, "Pedro")
# d)
print(ministerio1.mostrar_menor_edad())
print(ministerio1.mostrar_menor_sueldo())
print(ministerio2.mostrar_menor_edad())
print(ministerio2.mostrar_menor_sueldo())