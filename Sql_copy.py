from numpy import save
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

class dbMidlleware:
    def _init_(self):
        # cria as stings de conexão
        self.engine=create_engine("")
        self.engine2=create_engine("")
        
        # a função exige 2 parâmetros: 1- o nome que voce quer dar a tabela, e 2 - a query do banco.  
    def copy_db(self,nome_tabela = "export_default",query =" "):
        #cria a query e usa na primeira conexão para salvar em dataframe
        _query = query
        _dataFrame_conect = pd.read_sql(_query,self.engine)
        # e salva o dataframe na segunda conexão
        _dataFrame_conect.to_sql(nome_tabela,self.engine2,if_exists='replace')
        print(f"a tabela {nome_tabela} foi copiada com sucesso")



show_data = dbMidlleware()
show_data.copy_db(""," SELECT * FROM ")
