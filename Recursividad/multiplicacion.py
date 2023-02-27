def multiplicacion(n, m):
    if m == 1:
        return n
    return n + multiplicacion(n, m-1)

print(f"3 x 2 = {multiplicacion(3,2)}")
print(f"3 x 3 = {multiplicacion(3,3)}")
print(f"3 x 4 = {multiplicacion(3,4)}")
print(f"3 x 5 = {multiplicacion(3,5)}")
