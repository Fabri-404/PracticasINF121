from D import D

x = int(input("Valor para x: "))
y = int(input("Valor para y: "))
z = int(input("Valor para z: "))

objeto = D(x, y, z)

print("Valores iniciales:")
print(objeto)
print("\nIncrementaXZ:")
objeto.incrementaXZ()
print(objeto)
print("\nIncrementaYZ:")
objeto.incrementaYZ()
print(objeto)
print("\nIncrementaXYZ:")
objeto.incrementaXYZ()
print(objeto)