nome = str(input('Digite seu nome completo: ')).strip().title()
print('O seu nome é completo é {}.'.format(nome))
cont_letras = len(nome) - nome.count(' ')
nome_lista = nome.split()
print('O seu nome com letras miúsculas: {}.'.format(nome.upper()))
print('O seu nome com letras minúsculas: {}.'.format(nome.lower()))
print('O seu nome em forma de listas: {}.'.format(nome.split()))
print('O seu nome ao todo contém {} letras.'.format(cont_letras))
print('O seu primero nome é {}.'.format(nome_lista[0]))
print('O seu último nome é {}.'.format(nome_lista[-1]))
