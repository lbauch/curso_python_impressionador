while True:
    try:
        nota1 = float(input('digite a primeira nota:\n'))
        if nota1 <= 10 and nota1 >=0: 
            break
        else:
            print('Deve ser um valor real entre 0 e 10.')
    except ValueError:
        print('Deve ser um valor real entre 0 e 10.')
        #continue
while True:
    try:
        nota2 = float(input('digite a segunda nota:\n'))
        break
    except ValueError:
        print('Deve ser um valor real entre 0 e 10.')
if nr1 == nr2:
    print('são iguais')
elif nr1 > nr2:
    print(f'nr1 é maior: {nr1}')
else:
    print(f'nr2 é maior: {nr2}')