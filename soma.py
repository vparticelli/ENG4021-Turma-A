def somaf(a, b):
    """Retorna a soma de dois números reais."""
    return a + b


def teste_somaf():
    assert somaf(2, 3) == 5
    assert somaf(-1, 1) == 0
    assert somaf(2.5, 0.5) == 3.0


if __name__ == '__main__':
    teste_somaf()
    print('Testes de soma.py passaram com sucesso!')
