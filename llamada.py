print("----------------------------------")
print("-------Costo de la llamada--------")
print("----------------------------------")

# input
dl = int(input("Ingrese la duración de la llamada: "))

# processing
if dl <= 3:
    cl = 300
else:
    m = dl - 3
    cl = 300 + (50 * m)

# output
print("----------------------------------")
print("El costo de la llamada es de " +str(cl)+"$")
print("----------------------------------")
