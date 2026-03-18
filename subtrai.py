def subtraif(a, b):
    """Retorna a subtração de dois números reais."""
    return a - b


def teste_subtraif():
    assert subtraif(5, 3) == 2
    assert subtraif(0, 4) == -4
    assert subtraif(2.5, 0.5) == 2.0


if __name__ == '__main__':
    teste_subtraif()
    print('Testes de subtrai.py passaram com sucesso!')
