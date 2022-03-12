listaNumeros=[]
for k in range(0,5,1):
    numeroIngresado = int(int('Ingrese el numero: '))
    listaNumeros.append(numeroIngresado)

buscarNumero = int(input('¿Qué número buscas? '))
if(buscarNumero in listaNumeros):
    print('Si esta en la lista')
else:
    print('No esta en la lislistaNumeros') 