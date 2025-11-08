#Ernesto Daniel Piña Perez
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))

print(f"La suma de {x} + {y} es igual: {x + y}")
print(f"La resta de {x} - {y} es igual: {x - y}")
print(f"La multiplicación de {x} * {y} es igual: {x * y}")
print(f"La división de {x} / {y} es igual: {x / y}")
print(f"El módulo de {x} % {y} es igual: {x % y}")
print(f"El módulo de {y} % {x} es igual: {y % x}")
print(f"La potencia cúbica de {x} ** {y} es igual: {x ** y}")

a = int(input("Ingresa el primer número: "))
a += 2
print("La suma es:", a)
a -= 13
print("La resta es:", a)

b = int(input("Ingresa el segundo número: "))
b += 2
print("La suma es:", b)
b -= 13
print("La resta es:", b)

print(f"Es igualdad {a} y {b}: ", a == b)
print(f"Es desigualdad {a} y {b}: ", a != b)
print(f"{a} es mayor que {b}: ", a > b)
print(f"{a} menor que {b}: ", a < b)

print("\nTabla de verdad AND")
print("A\tB\tA and B")
for A in [True, False]:
    for B in [True, False]:
        print(f"{A}\t{B}\t{A and B}")

print("\nTabla de verdad OR")
print("A\tB\tA or B")
for A in [True, False]:
    for B in [True, False]:
        print(f"{A}\t{B}\t{A or B}")

print("\nTabla de verdad NOT")
print("A\tnot A")
for A in [True, False]:
    print(f"{A}\t{not A}")