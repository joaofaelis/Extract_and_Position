# Sistema de Automação para mapeamento em arquivo .xls 

"extract and position" é um serviço de ETL que foi desenvolvido para 
facilitar um mapeamento de sistemas internos e suas dependências com outros sistemas dentro
da empresa, visando que surgiu a necessidade de realizar esse mapeamento
organizacional em planilha e salvamento das informações em banco de dados.

- O banco de dados utilizado foi MongoDB, para facilitar o salvamento de dados em forma de documentos.
- Para criação da infraestrutura do banco de dados foi utilizado a lib Pymongo.
- Biblioteca utilizada para manipulação de dados e arquivo .xls foi OpenPyXL
- Para ocultação de informações de conexão com o banco de dados e nomes de arquivos foi utilizado o arquivo .env com a biblioteca Python-Decouple