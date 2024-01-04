try:
    n1 = int(input("Valor 1: "))
    n2 = int(input("Valor 2: "))
    n3 = int(input("Valor 3: "))
    print(max(n1,n2,n3))
except Exception as e:
    print("Error: cannot read values.", e)