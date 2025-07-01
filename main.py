# SISTEMA DE SAQUE
valor = int(input('Digite o valor em R$: '))

while True: # laço de codigo infinito
    if (valor >= 100):# verifica se o valoor é >= 100
        conta100 = valor // 100  #retorna a divisao da parte inteira (elimina as casas decimais e o resto do valor)
        valor = valor - conta100 * 100 #pega valor inicial(do input) e desconta a variavel quantidade
        print(f'Cédulas de 100 :{conta100}')
        
        # enquanto nao for 0 é verdadeiro
        if not valor:
            break

    if (valor >= 50):
        conta50 = valor // 50
        valor = valor - conta50 * 50
        print(f'Cédulas de 50 :{conta50}')
        if not valor:
            break

    if (valor >= 20):
        conta20 = valor // 20
        valor = valor - conta20 * 20
        print(f'Cédulas de 20 :{conta20}')
        if not valor: 
            break

    if (valor >= 10):
        conta10 = valor // 10
        valor = valor - conta10 * 10
        print(f'Cédulas de 10 :{conta10}')
        if not valor:
            break

    if (valor >= 5):
        conta5 = valor // 5
        valor = valor - conta5 * 5
        print(f'Cédulas de 5 :{conta5}')
        if not valor:
            break

    if valor: #valor falsey 
        conta1 = valor // 1
        print(f'Cédulas de 1 :{conta1}')
        break