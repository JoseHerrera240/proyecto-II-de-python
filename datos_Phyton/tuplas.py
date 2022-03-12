#creando tuplas en python
estudiantes=('Carlos','Juan Carlos')
print(estudiantes)

#El append no se puede utilizar en tuplas, ya que las tuplas son inmutables

#Recorriendo tuplas
for estudiante in estudiantes:
    print(estudiante)

#Convertir una tupla en una lista
listaEstudiantes=list(estudiantes)
print(listaEstudiantes)

listaEstudiantes.append('Martha')
print(listaEstudiantes)