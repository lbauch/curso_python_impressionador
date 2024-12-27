# Arquivo destinado para realização de pequenos testes de funcionamento

import pandas as pd

vendas_df = pd.read_csv(r'C:\Users\user\Desktop\Python impressionador\Curso-Python-Impressionador' + \
                        r'\auxiliares\Contoso - Vendas - 2017.csv', sep=';')

vendas_df.info()

#lista_clientes = vendas_df['ID Cliente'][:10]

lista_clientes = vendas_df[['ID Cliente', 'Numero da Venda', 'Data da Venda']]
print(f'Cheguei na lista\n{lista_clientes}')

lista_clientes = lista_clientes.drop(['Data da Venda', 'Numero da Venda'], axis= 1)

from IPython.display import display
display(vendas_df)

novo_dataframe = lista_clientes.merge(vendas_df, on='ID Cliente')
display(novo_dataframe)