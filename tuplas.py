tupla = ()
type(tupla)

alvaro = ('Alvaro', 39,1984)
stef  = ('Stefani', 37,1984)
pablo = ('Pablo',50,1973)

# pablo[0] = 'Paulo' #Es inmutable

clientes = [alvaro,stef,pablo]
# clientes[1][1] = 34

clientes.append(('Jorge',20,2000))


for i in range(len(clientes)):
    print(1,clientes[i])
for cliente in clientes:
    print(cliente)

print(alvaro.index(39)) #Encuentro índice de elemento

# for i in range(len(clientes)):
#     print(i,clientes[i][0])

nuevos_clientes = list(enumerate(clientes,start=1000))

for codigo,informacion in nuevos_clientes:
    print(codigo,informacion[0])
# Siempre consultar la documentación


class Cuenta:
    def __init__(self,codigo):
        self._codigo=codigo
        self._saldo=saldo = 0
    def deposita(self,valor):
        self._saldo += valor
    def pasa_mes(self):
        self._saldo*= 1.005
    def __str__(self):
        return f'>>>>Código: {self._codigo} -- Saldo: {self._saldo}<<<<'
    

class CuentaCorriente(Cuenta):
    def pasa_mes(self):
        self._saldo -= 2

class CuentaAhorros(Cuenta):
    def pasa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class CuentaInversiones(Cuenta):
    pass

cuenta_alvaro = CuentaCorriente(16)
cuenta_alvaro.deposita(500)
cuenta_stefi = CuentaCorriente(17)
cuenta_stefi.deposita(1000)
cuenta_inversiones = CuentaInversiones(18)
cuentas = [cuenta_alvaro, cuenta_stefi,cuenta_inversiones]


cuenta_alvaro.pasa_mes()
cuenta_stefi.pasa_mes()
cuenta_inversiones.pasa_mes()

for cuenta in cuentas:
    print(cuenta)






class CuentaSalario:
    def __init__(self,codigo):
        self._codigo=codigo
        self._saldo=saldo = 0
    def deposita(self,valor):
        self._saldo += valor
    def __eq__(self,otro):
        return self._codigo == otro._codigo
    def __str__(self):
        return f'>>>>Código: {self._codigo} -- Saldo: {self._saldo}<<<<'
    
salario_alvaro = CuentaSalario(15)
salario_stefani = CuentaSalario(15)

print(salario_alvaro == salario_stefani) #Si yo no defino eq, compara las id (los espacio de memoria)
print(salario_alvaro.__eq__(salario_stefani))

##Problema:
corriente_alvaro = CuentaCorriente(15)
print(corriente_alvaro == salario_alvaro) #Está mal, para corregirlo podría poner en __eq__ un if(type==...)


