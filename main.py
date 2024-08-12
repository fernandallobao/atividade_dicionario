
pessoa = {}

pessoa['Nome'] = input('Informe o nome: ')
pessoa['CPF'] = input('Informe o CPF: ')
pessoa['RG'] = input('Informe o RG: ')
pessoa['Data de nascimento'] = input('Informe a data de nascimento: ')
pessoa['Sexo'] = input('Informe o sexo: ')
pessoa['Signo'] = input('Informe o signo: ')
pessoa['Nome da Mae'] = input('Informe o nome da mãe: ')
pessoa['Nome do Pai'] = input('Informe o nome do pai: ')
pessoa['E-mail'] = input('Informe o e-mail: ')
pessoa['Senha'] = input('Informe a senha: ')
pessoa['CEP'] = input('Informe o CEP: ')
pessoa['Endereço'] = input('Informe o Endereço: ')
pessoa['Numero'] = input('Informe o Numero: ')
pessoa['Bairro'] = input('Informe o Bairro: ')
pessoa['Cidade'] = input('Informe o Cidade: ')
pessoa['Estados'] = input('Informe o Estado: ')
pessoa['Telefon'] = input('Informe o telefone: ')
pessoa['Celular'] = input('Informe o celular: ')
pessoa['Altura'] = input('Informe a altura: ')
pessoa['Peso'] = input('Informe o peo: ')
pessoa['Tipo sanguineo'] = input('Informe o tipo sanguineo: ')
pessoa['Cor favorita'] = input('Informe a cor favorita: ')

print('\n')

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')