"""Cree un programa que selecciones dos vectores de longitud
n (dada por el usuario al principio) y halle su producto
escalar."""

longitud = int(input("Ingrese la longitud n de los dos vectores >>> "))
vector1 = []
vector2 = []

for i in range(longitud):
    numero = int(input(f"Ingrese el valor {i+1} del vector 1 >>> "))
    vector1.append(numero)
print()
for j in range(longitud):
    numero = int(input(f"Ingrese el valor {j+1} del vector 2 >>> "))
    vector2.append(numero)
print()
productoEscalar =  0
for k in range(longitud):
    producto = vector1[k] * vector2[k]
    productoEscalar += producto  


print(f"el producto escalar entre el vector 1 ({vector1}) y el vector 2 ({vector2}) es "
      f">>> {productoEscalar}")