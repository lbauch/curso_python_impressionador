# Arquivo destinado para realização de pequenos testes de funcionamento

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
# Todos os elementos devem ser do mesmo tipo, então ele traduz para a interpretação do elemento informado em outro.
# Obedece a ordem de transformação conforme abaixo:
array = np.array([False, "2", 3.0, 4, 5])
print(array)
array = np.array([False, 2, 3.1, 4, 5])
print(array)
array = np.array([False, 2, 3, 4, 5])
print(array)