# Sobre

Esse repositório tem como objetivo realizar um ETL simples da [AviationStack API](https://aviationstack.com/). Além disso, o repositório também realiza uma análise dos dados processados, [contidas no notebook analysis_etl_aviationstack.ipynb](./notebooks/analysis_etl_aviationstack.ipynb), fornecendo insights e visualizações úteis.

## Principais tecnologias usadas:

- Python: Linguagem de programação principal para o desenvolvimento do ETL e da análise de dados.
- Jupyter Notebook: Ambiente interativo para criação e compartilhamento de notebooks com código e visualizações.
- PostgreSQL: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar e consultar dados.
- psycopg2: Biblioteca para conectar e interagir com o banco de dados PostgreSQL a partir do Python.
- Pandas: Biblioteca para manipulação e análise de dados.
- GitHub Actions: Configurado para executar a lintagem do código automaticamente sempre que houver um push para o repositório.
- unittest: Framework para realização de testes unitários, assegurando a funcionalidade do código.
- coverage: Ferramenta para medir a cobertura dos testes, ajudando a identificar partes do código não testadas.
- folium: Biblioteca para visualização de dados geoespaciais em mapas.
- matplotlib: Biblioteca para criação de gráficos e visualizações estáticas em Python