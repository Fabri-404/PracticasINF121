from D import D
x = int(input("Valor para x: "))
y = int(input("Valor para y: "))
z = int(input("Valor para z: "))

objeto = D(x, y, z)
print("-----------------------------")
print("IncrementaXZ:")
objeto.incrementaXZ()
print(f"x: {objeto.x}, y: {objeto.y}, z: {objeto.z}")
print("-----------------------------")
print("IncrementaYZ:")
objeto.incrementaYZ()
print(f"x: {objeto.x}, y: {objeto.y}, z: {objeto.z}")
print("-----------------------------")
print("IncrementaXYZ:")
objeto.incrementaXYZ()
print(f"x: {objeto.x}, y: {objeto.y}, z: {objeto.z}")

