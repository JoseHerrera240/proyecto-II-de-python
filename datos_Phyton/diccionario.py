estudiante={
    'Name':'Falcao',
    'Age':34, 
    'esFutbolista':True 
}
#Imprimir/acceder a todas las llaves
#Atributos de mi diccionario
print(estudiante)
#Necesito acceder a una propiedad de nuestro objeto(Diccionario)
print(estudiante['esFutbolista'])
print(estudiante.get('Age'))

#Recorre un diccionario y obtener sus valores

for valor in estudiante.values():
    print(valor)

