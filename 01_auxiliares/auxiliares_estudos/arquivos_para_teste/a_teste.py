# Arquivo destinado para realização de pequenos testes de funcionamento

#! pip install pandas
#! pip install pandas
#! pip install pandas

from pathlib import Path
from IPython.display import display
import pandas as pd

arquivo = Path(__file__).parent / "NotasEmitir.xlsx"

tabela = pd.read_excel(arquivo) 
display(tabela)

for coluna in tabela:
  print(coluna)

for linha in tabela.index:
  print(linha)
