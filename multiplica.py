def multiplicaf(a, b):
    """Retorna a multiplicação de dois números reais."""
    return a * b


def teste_multiplicaf():
    assert multiplicaf(2, 3) == 6
    assert multiplicaf(-1, 4) == -4
    assert multiplicaf(2.5, 2) == 5.0


if __name__ == '__main__':
    teste_multiplicaf()
    print('Testes de multiplica.py passaram com sucesso!')
