tupla = ()
type(tupla)

alvaro = ('Alvaro', 39,1984)
stef  = ('Alvaro', 37,1984)
pablo = ('Pablo',50,1973)

# pablo[0] = 'Paulo' #Es inmutable

clientes = [alvaro,stef,pablo]
# clientes[1][1] = 34

clientes.append(('Jorge',20,2000))

for cliente in clientes:
    print(cliente)

print(alvaro.index(39)) #Encuentro índice de elemento