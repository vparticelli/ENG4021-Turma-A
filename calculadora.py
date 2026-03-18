import soma
import subtrai
import multiplica
import divide


def main():
    print('=== Calculadora de 4 operações ===')
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    op = input('Digite a operação (+, -, *, /): ').strip()

    if op == '+':
        resultado = soma.somaf(a, b)
    elif op == '-':
        resultado = subtrai.subtraif(a, b)
    elif op == '*':
        resultado = multiplica.multiplicaf(a, b)
    elif op == '/':
        resultado = divide.dividef(a, b)
    else:
        print('Operação inválida.')
        return

    print(f'Resultado: {resultado}')


if __name__ == '__main__':
    main()
