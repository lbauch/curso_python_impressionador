import pytest
from main import calcular_lucro, calcular_faturamento, calcular_custo

@pytest.fixture
def cotacao_dolar():
    return 5 # pode pegar da própria API msm direto


def test_calcular_custo(cotacao_dolar):
    assert calcular_custo(cotacao_dolar) > 0


def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(faturamento, 50) > 0