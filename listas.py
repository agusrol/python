edades = [15,18,59,71]
print(type(edades))
edades.append(35)
print(edades)
edades.remove(18)
edades.insert(1,18)
print(edades)
edades.clear()
print(edades)
edades.extend([16,17,18])
print(edades)

print(2 in edades)

# comprehension
edades_proximo_anio = [edad + 1 for edad in edades]
print(edades_proximo_anio)
mayores_proximo_anio = [edad for edad in edades if edad > 17]
print(mayores_proximo_anio)


print("_____________________________")
# MUTABILIDAD

def analisis_listas(lista):
    print(id(lista))
    print(len(lista))
    lista.append(13)
    return lista
print(analisis_listas(edades))


class CuentaCorriente:
    def __init__(self,codigo):
        self.codigo=codigo
        self.saldo=saldo = 0
    def deposita(self,valor):
        self.saldo += valor
    def __str__(self):
        return f'>>>>Código: {self.codigo} -- Saldo: {self.saldo}<<<<'
    
cuenta_alvaro = CuentaCorriente(16)
cuenta_alvaro.deposita(500.0)
cuenta_stef = CuentaCorriente(17)
cuenta_stef.deposita(1000.0)

cuentas = [cuenta_alvaro, cuenta_stef]

for cuenta in cuentas:
    print(f'El espacio de memoria es:  {id(cuenta)}')
    print(cuenta)

def deposita_a_todos(cuentas):
    for cuenta in cuentas:
        cuenta.deposita(100)

# cuentas.insert(0,76)
# deposita_a_todos(cuentas) #Da error, porque pusiste un int!


for cuenta in cuentas:
    print(f'El espacio de memoria es:  {id(cuenta)}')
    print(cuenta)


print(sorted(edades))
print(sorted(edades,reverse=True))

edades.sort()
print(edades)

nombres = ["A","S","P"]
for nombre in nombres:
    print(ord(nombre[0]))

for nombre in nombres:
    print(ord(nombre[0]))

from functools import total_ordering

@total_ordering
class CuentaSalario:
    def __init__(self,codigo):
        self._codigo=codigo
        self._saldo=saldo = 0
    def deposita(self,valor):
        self._saldo += valor
    def __eq__(self,otro):
        return self._codigo == otro._codigo and self._saldo==otro._saldo
    # def __lt__(self,otro):
    #     return self._saldo < otro._saldo
    def __le__(self,otro):
        return self._saldo <= otro._saldo

    def __str__(self):
        return f'>>>>Código: {self._codigo} -- Saldo: {self._saldo}<<<<'
    


cuentaS_alvaro = CuentaSalario(51)
cuentaS_alvaro.deposita(500)
cuentaS_stef = CuentaSalario(52)
cuentaS_stef.deposita(1000)
cuentaS_pablo = CuentaSalario(53)
cuentaS_pablo.deposita(500)
# sorted(cuentas)

cuentas = [cuentaS_alvaro,cuentaS_stef,cuentaS_pablo]

from operator import  attrgetter
print(type(cuenta_alvaro))

for cuenta in sorted(cuentas, key=attrgetter('_saldo')): #Esto es una forma, pero rompe encapsulamiento
    print(cuenta)

print(sorted(cuentas))

print(cuentaS_alvaro >= cuentaS_stef)

for cuenta in sorted(cuentas):
    print(cuenta)
