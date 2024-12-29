# Arquivo destinado para realização de pequenos testes de funcionamento

import pandas as pd
from tqdm import tqdm
from IPython.display import display

vendas_df = pd.read_csv(r'C:\Users\user\Desktop\Python impressionador\Curso-Python-Impressionador\auxiliares\arquivos_base\Contoso - Vendas - 2017.csv', sep=';', encoding='ISO-8859-1')


# O total indica quantos itens há no total, neste caso, os itens da coluna ID Loja
# Position= 0 e leave= True - juntos combinam para que a barra de progresso seja sobrescrita.
# Ou seja, não escreve mais de uma barra de progresso
# pbar é o nome padrão utilizado para a variável de barra de progresso - progress bar
pbar = tqdm(total=len(vendas_df['ID Loja']), position=0, leave=True)

for i, id_loja in enumerate(vendas_df['ID Loja']):
    # Atualiza a visualização da barra de progresso
    pbar.update()
    if id_loja == 222:
        # vendas_df.loc[linha, coluna]
        vendas_df.loc[i, 'Quantidade Devolvida'] += 1
        
display(vendas_df)