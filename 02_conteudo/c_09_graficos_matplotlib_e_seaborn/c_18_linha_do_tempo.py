import matplotlib.pyplot as plt

anos = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas = [0 for i in range(len(anos))]

plt.plot(anos, vendas, marker='o')
plt.title('Evolução dos Sistemas Operacionais')

for i, v in enumerate(vendas):
  plt.annotate(
    anos[i],
    color='blue',
    xy=(anos[i], vendas[i]),
    xytext=(0, 10),
    textcoords='offset points',
    ha='center', 
    rotation=60
  )

plt.gca().set_axis_off()
plt.show()