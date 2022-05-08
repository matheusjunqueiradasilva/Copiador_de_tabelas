# copiador_de_Tabelas
Código que copia tabela de um banco pro outro.

## Importante!

*Crie uma variável de ambiente para os seus endpoints e modifique as variáveis no __init__.*



### Running
self.engine = create_engine("") -> a engine do banco de dados que o sqlachemy vai abrir a conexão, o banco que tem a tabela a ser copiada.

self.engine2 = create_engine("") ->a engine do banco de dados que o sqlachemy vai abrir a conexão, o banco que vai receber a cópia .

### exemplos:

show_data = dbMidlleware() -> chama as conexões criadas a cima.

show_data.copy_db("tabela1"," SELECT * FROM tabela1") -> o primeiro argumento recebe o nome da tabela ser copiado, e o segundo o a query.

### References

SQLAlchemy -> https://docs.sqlalchemy.org/en/14/

Pandas -> https://pandas.pydata.org

Numpy -> https://numpy.org/doc/stable/reference/routines.array-manipulation.html

psycopg2 -> https://pypi.org/project/psycopg2/



