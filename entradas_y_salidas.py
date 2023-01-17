## Forma antigua
numero = 514
texto = "quijote"
otromas = 1.2
print("El numero es %d y el texto es %s y tiene %f" % (numero, texto, otromas))
## forma moderna python 3.6
print("El numero es {} y el texto es {} y tiene {}" .format(numero, texto, otromas))
## forma actual
print(f'EL NUMERO ES {numero} Y EL TEXTO ES {texto.upper()} Y TIENE {otromas}')

## Un ejemplo de como se puede manipular utilizando esta forma.

def suma(a, b):
    return a + b

txt = f'El numero es {suma(numero, numero)} y el texto es {texto.upper()} y tiene {otromas}'
print(txt)
