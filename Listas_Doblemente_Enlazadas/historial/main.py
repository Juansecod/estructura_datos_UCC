from Lista import Lista

historial = Lista()
link = None

print("-"*100)
print("Navegador web")
print("Ingresa la url a la que deseas ir")
print("\t* Si deseas ir a la pagina anterior ingresa el comando prev")
print("\t* Si deseas ir a la pagina siguiente ingresa el comando next")
print("-"*100)

while link != 'exit':
    if link == "prev":
        prev = historial.previo()
        print("Redirigiendo a: " + prev if prev is not None else "No has ingresado a paginas previas...",)
    elif link == "next":
        next = historial.siguiente()
        print("Redirigiendo a: " + next if next is not None else "No has ingresado a mas links...",)
    elif link == None:
        pass
    else:
        historial.insertar(link)
    link = input()


