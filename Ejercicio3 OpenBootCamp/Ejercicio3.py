def primos_hasta_n(n):
    primos = []
    for num in range(2, n+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primos.append(num)
    return primos

n = int(input("Ingrese un número para calcular los números primos hasta ese valor: "))
print(primos_hasta_n(n))
