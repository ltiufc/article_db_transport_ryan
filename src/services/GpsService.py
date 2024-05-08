import csv
from datetime import datetime, timedelta
import pandas as pd

def transformarData(data_antiga):
    data_processo = str(data_antiga)
    data_nova = data_processo[6:10] + "-" + data_processo[3:5] + "-" + data_processo[0:2]
    return data_nova


def quebraDataHora(data_hora_antiga):
    data_hora = str(data_hora_antiga)
    data = data_hora[0:10]
    hora = data_hora[11:19]
    return data, hora

def inserirGpsSQL(conexao,file_path):
    with open(file_path, 'r', encoding='UTF-8') as csv_arq:
        csv_dict = csv.reader(csv_arq)

        cont = 0
        split_row = {}
        verification = 0

        for row in csv_dict:
            if verification == 0:
                pass

            if verification == 1:
                for row2 in row:
                    split_row[cont] = row2
                    cont += 1

                com_sql = "INSERT INTO gps_novembro(ID_GPS,ID_DICIONARIO,IDENTIFICADOR,DATA,HORA,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                valor = (split_row[0],split_row[1], split_row[2], split_row[3], split_row[4], split_row[5], split_row[6])
                conexao.cursor().execute(com_sql, valor)
                conexao.commit()
                #print(split_row[0])
                cont = 0
                split_row = {}

            verification = 1

def inserirGpsAninhadoMongoDB(linha,database_mongo):
    timestamp = str(linha['DATA'] + 'T' + linha['HORA'] + '.000-0300')
    format_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

    gps = {'ID_DICIONARIO': int(linha['ID_DICIONARIO']), 'DATA': str(linha['DATA'])}
    check = database_mongo.gps_novembro.find_one(gps)

    if check == None:
        gps_data = {
            'ID_DICIONARIO': int(linha['ID_DICIONARIO']),
            'DATA': str(linha['DATA']),
            'SALTO': int(1),
            'POSICOES': []
        }

        database_mongo.gps_novembro.insert_one(gps_data)

    elif int(check['SALTO']) == 0:
        gps = {'ID_DICIONARIO': int(linha['ID_DICIONARIO']), 'DATA': str(linha['DATA']), 'SALTO': int(0)}
        posicao = {
            'type': 'Point',
            'timestamp': format_date,
            'coordinates': [linha['LONGITUDE'], linha['LATITUDE']]
        }

        database_mongo.gps_novembro.update_one(gps, {'$push': {'POSICOES': posicao}}, upsert=True)
        database_mongo.gps_novembro.update_one(gps, {'$set': {'SALTO': int(1)}}, upsert=True)
    else:
        salto = int(check['SALTO'])
        salto -= 1
        database_mongo.gps_novembro.update_one(gps, {'$set': {'SALTO': int(salto)}}, upsert=True)

def inserirGpsMongoDB(database_mongo,file_path):
    dataframe = pd.read_csv(file_path)
    dataframe['timestamp'] = pd.to_datetime(dataframe['DATA'] + 'T' + dataframe['HORA'] + '.000-0300')
    dataframe = dataframe.sort_values(by=['ID_DICIONARIO', 'timestamp'])
    dicionarios = [{'ID_DICIONARIO': None,
                    'DATA': None,
                    'POSICOES': [
                        {
                            'type': 'Point',
                            'timestamp': None,
                            'coordinates': [None, None]
                        }
                    ]}]

    for index, row in dataframe.iterrows():
        novo_dicionario = {'ID_DICIONARIO': row['ID_DICIONARIO'],
                           'DATA': row['DATA'],
                           'POSICOES': [
                               {
                                   'type': 'Point',
                                   'timestamp': row['timestamp'],
                                   'coordinates': [row['LONGITUDE'], row['LATITUDE']]
                               }]
                           }
        chave_repetida = False
        for dicionario in dicionarios:
            if  row['ID_DICIONARIO'] == dicionario['ID_DICIONARIO'] and row['DATA'] == dicionario['DATA'] \
                    and  dicionario['DATA'] is not None and dicionario['ID_DICIONARIO']:
                index = dicionarios.index(dicionario)
                atualizar_dicionario = dicionarios[index]
                ultimo_timestamp = atualizar_dicionario['POSICOES'][-1]['timestamp']
                if row['timestamp'] - ultimo_timestamp > timedelta(minutes=5):
                    atualizar_dicionario['POSICOES'].append({'type': 'Point',
                                                             'timestamp': row['timestamp'],
                                                             'coordinates': [row['LONGITUDE'], row['LATITUDE']]
                                                             })
                    dicionarios[index] = atualizar_dicionario
                    # print(atualizar_dicionario['POSICOES'])
                chave_repetida = True
                break

        if not chave_repetida:
            dicionarios.append(novo_dicionario)

    database_mongo.gps_novembro.insert_many(dicionarios)

    #
    # for linha in dataframe:
    #
    # dici
    # gps = {'ID_DICIONARIO': None , 'DATA': None, 'POSICOES': [] }


    # print(chunk)
    # read_csv = pd.concat(chunk)
    # return read_csv.apply(inserirGpsAninhadoMongoDB,axis=1, args=(database_mongo,))

def gpsSelecionarIntervaloDeTempo(file_path):
    with open(file_path, 'r', encoding='UTF-8') as csv_arq:
        csv_dict = csv.reader(csv_arq)

        with open('../resources/tratados/gps/dia19_hora.csv','w',newline='', encoding='UTF-8') as new_csv_arq:
            new_csv = csv.writer(new_csv_arq)

            verification = 0
            split_row = {}
            cont = 0

            for row in csv_dict:
                if verification == 0:
                    new_csv.writerow(row)
                    pass
                if verification == 1:
                    for row2 in row:

                        split_row[cont] = row2
                        cont += 1

                    hora = split_row[4]
                    if(hora[0:2] == '21'):
                        minutos = hora[3:5]
                        if (int(minutos) < 15):
                            new_csv.writerow(row)

                    cont = 0
                    split_row = {}

                verification = 1

