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
cuentas.insert(0,76)
deposita_a_todos(cuentas)
for cuenta in cuentas:
    print(f'El espacio de memoria es:  {id(cuenta)}')
    print(cuenta)

