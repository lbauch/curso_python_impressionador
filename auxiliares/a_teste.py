# Arquivo destinado para realização de pequenos testes de funcionamento

import  numpy as np
vendas = np.array([250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

# Reorganizar os dados em uma matriz de 2x7
# É obrigatório os dados possuírem a mesma quantidade total de valores
# Caso contrário, resulta em erro.
vendas_reshaped = np.reshape(vendas, (2, 2, 3))
print(vendas_reshaped)

# Mostrar as dimensões da matriz ou array informado
print(vendas_reshaped.ndim)