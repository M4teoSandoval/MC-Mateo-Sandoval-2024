a=int(input("Digite la cantidad de elementos de el conjunto A <<< "))
conjuntoA=set()
for i in range(a):
    elemento=float(input(f"Escriba el elemento {i+1}: "))
    conjuntoA.add(elemento)
print("A: ",conjuntoA)

b=int(input("Digite la cantidad de elementos de el conjunto B <<< "))
conjuntoB=set()
for i in range(b):
    elemento=float(input(f"Escriba el elemento {i+1}: "))
    conjuntoB.add(elemento)
print("B: ",conjuntoB)

while True:
    op=int(input("Cual operacion quieres realizar?\n1. Union\n2. Interseccion\n3. Diferencia\n4. Diferencia Simetrica\n5. Salir"))
    if op==1:
        unionAB= conjuntoA | conjuntoB
        print(f"A u B: {unionAB}")
    elif op==2:
        interseccionAB= conjuntoA & conjuntoB
        print(f"A ∩ B: {interseccionAB}")
    elif op==3:
        op3=int(input("Que quieres realizar:\n1. Conjunto A - Conjunto B\n2. Conjunto B - Conjunto A"))
        if op3== 1:
            direnciaAB= conjuntoA - conjuntoB
            print(f"A - B: {direnciaAB}")
        elif op3== 2:
            direnciaAB= conjuntoB - conjuntoA
            print(f"B - A: {direnciaAB}")
            
    elif op== 4:
        diferenciaSimetricaAB= conjuntoA ^ conjuntoB
        print(f"A ∆ B: {diferenciaSimetricaAB}")
    elif op== 5:
        print("saliendo... ")
        break
    else:
        print("opcion incorrecta, intente nuevamente.")
    