

while True:
    u=int(input("Digite la cantidad de elementos de el conjunto Universal (U) <<< "))
    conjuntoU=set()
    for i in range(u):
        elemento=float(input(f"Escriba el elemento {i+1}: "))
        conjuntoU.add(elemento)
    print("U: ",conjuntoU)

    a=int(input("Digite la cantidad de elementos de el subconjunto A <<< "))
    conjuntoA=set()
    for i in range(a):
        elemento=float(input(f"Escriba el elemento {i+1}: "))
        conjuntoA.add(elemento)
    print("A: ",conjuntoA)
    
    
    if conjuntoA <= conjuntoU:
        print("El conjunto A si es subconjunto de el conjunto universal:")
        operacion1= (conjuntoU | conjuntoA) & conjuntoA
        print(f"(U u A) ∩ A: {operacion1}")
        
        operacion2= (conjuntoU & conjuntoA) ^ conjuntoA
        print(f"(U ∩ A) ∆ A: {operacion2}")
        
        operacion3= (conjuntoU - conjuntoA) ^ conjuntoA  
        print(f"(U - A) ∆ A: {operacion3}")
    else:
        print("El conjunto A no es subconjunto de el conjunto universal, intente nuevamente.")
    
     

    