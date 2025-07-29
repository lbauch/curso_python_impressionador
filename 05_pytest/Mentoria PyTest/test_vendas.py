from main import calcular_faturamento, calcular_lucro

def test_calcular_faturamento():
    assert calcular_faturamento() > 0