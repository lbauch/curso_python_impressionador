# Arquivo destinado para realização de pequenos testes de funcionamento

import numpy as np
import matplotlib.pyplot as plt

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.scatter(meses, vendas)
plt.show()
plt.figure(1, figsize=(15, 3))
plt.subplot(1, 3, 1)
plt.plot(meses, vendas, color='red')
plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)
plt.subplot(1, 3, 3)
plt.bar(meses, vendas)
plt.show()