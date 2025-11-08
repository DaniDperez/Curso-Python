x=int(input("Ingresa el primer número:"))
y=int(input("Ingresa el segundo número:"))

print(f"La suma de {x} + {y} es igual: {x + y}")
print(f"La resta de {x} - {y} es igual: {x - y}")
print(f"La multiplicación de {x} * {y} es igual: {x * y}")
print(f"La división de {x} / {y} es igual: {x / y}")
print(f"El modulo de {x} % {y} es igual: {x % y}")
print(f"El modulo de {y} % {x} es igual: {y % x}")
print(f"La potencia cúbica de {x} ** {y} es igual: {x ** y}")

a=int(input("Ingresa el primer número:"))
a += 2
print(f"La suma es: ",a)
a -= 13
print(f"La resta es: ",a)

b=int(input("Ingresa el segundo número:"))

b += 2
print(f"La suma es: ",b)
b -= 13
print(f"La resta es: ",b)

print(f"Es igualdad  {a} y {b}: ",a == b)

print(f"Es desgualdad  {a} y {b}: ",a != b)

print(f"{a} es mayor que {b}: ",a > b)

print(f"{a} menor que {b}: ",a < b)

