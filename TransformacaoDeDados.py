import tabula
import pandas as pd

# Leitura no pdf 
quadro30 = tabula.read_pdf(
    'Padrão_TISS_Componente_Organizacional_202103.pdf',
    pages="79",
    lattice=True,
    pandas_options={"header": [1]},
    multiple_tables=False,
    area=[115,125,215,340]
)

# Correção das colunas
quadro30[0].columns = ['Código', 'Descrição da categoria', '','','']
quadro30 = quadro30[0]

# Remoção das colunas inválidas
quadro30.drop('', axis=1, inplace=True)

# Exportação do csv
quadro30.to_csv('Quadro30.csv', index=False)
print('Csv do Quadro 30 exportado com sucesso.')

quadro31 = tabula.read_pdf(
    'Padrão_TISS_Componente_Organizacional_202103.pdf',
    pages="79-84",
    pandas_options={"header": [8]},
    lattice=True,
    multiple_tables=False,
)
quadro31 = quadro31[0]
quadro31.to_csv('Quadro31.csv', index=False)
print('Csv do Quadro 31 exportado com sucesso.')

quadro32 = tabula.read_pdf(
    'Padrão_TISS_Componente_Organizacional_202103.pdf',
    pages=85,
    lattice=True,
    pandas_options={"header": [1]},
    multiple_tables=False,
    area=[130,125,200,300]
)
quadro32[0]
quadro32[0].columns = ['Código', 'Descrição da categoria', '','','']
quadro32 = quadro32[0]
quadro32.drop('', axis=1, inplace=True)
quadro32.to_csv('Quadro32.csv', index=False)
print('Csv do Quadro 32 exportado com sucesso.')

import os
import zipfile
# Cria um arquivo tipo zip para escrita
ZIP = zipfile.ZipFile('Teste_Intuitive_Care_{Felipe_Augusto_Souza}.zip', 'w')

# Para cada pasta do diretorio verifica se o final é .csv, se for adiciona no zip aberto
for pasta, subPasta, arquivos in os.walk('./'):
    for arquivo in arquivos:
        if arquivo.endswith('.csv'):
            ZIP.write(
                os.path.join(pasta, arquivo),
                arquivo, compress_type = zipfile.ZIP_DEFLATED
            ) 
# Fecha o arquivo após mexer nele..     
ZIP.close()
print('Arquivos compactados com sucesso.')
