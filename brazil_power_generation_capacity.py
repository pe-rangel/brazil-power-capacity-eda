import pandas as pd
import plotly.express as px

def brazil_pwr_generation_capacity():
    url_ons = 'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/capacidade-geracao/CAPACIDADE_GERACAO.csv'
    table = pd.read_csv(url_ons, sep=';', decimal='.' ,encoding='utf-8')

    table = table.drop(columns=['id_subsistema', 'id_estado', 'nom_modalidadeoperacao', 'nom_agenteproprietario', 'nom_agenteoperador', 'nom_usina', 'ceg', 'nom_unidadegeradora',
                                'cod_equipamento', 'num_unidadegeradora', 'dat_entradateste', 'dat_entradaoperacao'])

    table = table[table['dat_desativacao'].isna()]

    graphic1 = px.histogram(table, x='nom_estado', y='val_potenciaefetiva', color='nom_tipousina',
                            title='Brazil Installed Power Generation Capacity by State', 
                            labels={'nom_estado':'State Names', 'val_potenciaefetiva':'installed capacity (in MW)', 'nom_tipousina':'Power Plant Type'})

    graphic2 = px.histogram(table, x='nom_subsistema', y='val_potenciaefetiva', color='nom_tipousina',
                            title='Brazil Installed Power Generation Capacity by Region',
                            labels={'nom_subsistema':'Region Names', 'val_potenciaefetiva':'installed capacity (in MW)', 'nom_tipousina':'Power Plant Type'})

    graphic3 = px.pie(table, names='nom_tipousina', title='Proportion of Existent Power Plants in Brazil', color='nom_tipousina', labels= {'nom_tipousina':'Power Plant Type'})

    graphic4 = px.pie(table, names='nom_tipousina', values='val_potenciaefetiva' , title='Installed Generation Capacity by Power Plants in Brazil', color='nom_tipousina', labels={'nom_tipousina':'Power Plant Type'})
    
    graphic1.show()
    graphic2.show()
    graphic3.show()
    graphic4.show()

if __name__ == "__main__":
    brazil_pwr_generation_capacity()
