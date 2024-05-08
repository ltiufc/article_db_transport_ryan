import csv
import simplejson as json
import pandas as pd
from bson.decimal128 import Decimal128
from time import perf_counter, mktime, strptime
from datetime import datetime, date
from sys import maxsize
import pytz

def converterParaSegundos(time):
    return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])


def aproximacaoDeLatitudeELongitudeSQL(conexao, id_dicionario, hora, data):
    lower_difference = maxsize
    cursor = conexao.cursor()
    next_value = None
    first_value = None

    com_sql = "SELECT HORA,LATITUDE,LONGITUDE FROM gps_novembro where ID_DICIONARIO=%s AND DATA=%s"
    values = (id_dicionario, data)
    cursor.execute(com_sql, values)
    gps = cursor.fetchall()
    index = 0
    for row in gps:
        difference = (row[0] - hora).total_seconds()
        if difference > lower_difference:
            continue
        else:
            lower_difference = difference
            first_value = row
            index_next = index + 1
            next_value = gps[index_next]
        index = index + 1
    try:
        if first_value is not None:

            next_value_1 = float(next_value[1])
            first_value_1 = float(first_value[1])

            next_value_2 = float(next_value[2])
            first_value_2 = float(first_value[2])

            longitude = (((next_value_1 - first_value_1) * \
                          first_value[0].total_seconds() - hora.total_seconds())) / (
                                 next_value[0].total_seconds() - first_value[0].total_seconds()) + \
                         first_value_1

            latitude = (((next_value_2 - first_value_2) * \
                         first_value[0].total_seconds() - hora.total_seconds())) / (
                                next_value[0].total_seconds() - first_value[0].total_seconds()) + \
                        first_value_2

            return [longitude, latitude]

        else:
            return [00, 00]
    except ValueError:
        return [00, 00]


def aproximacaoDeLatitudeELongitudeMongoDB(database_mongo, id_dicionario, timestamp):

    gps = database_mongo.gps_novembro.find({'ID_DICIONARIO': int(id_dicionario)})
    gps = pd.DataFrame(list(gps))

    lower_difference = maxsize
    selected = None

    first_value = None
    next_value = None
    index = 0
    if 'POSICOES' in gps:
        for value in gps['POSICOES']:
            for v in value:
                difference = (v['timestamp'] - timestamp.replace(tzinfo=None)).total_seconds()
                if difference > lower_difference:
                    continue
                else:
                    selected = index
                    lower_difference = difference
                    first_value = v
                    next_value = value[index+1]
                index = index + 1

        if selected is not None:
            longitude = (((next_value['coordinates'][0] - first_value['coordinates'][0]) * \
                          (first_value['timestamp'] - timestamp.replace(tzinfo=None)).total_seconds()) / (
                                 next_value['timestamp'] - first_value['timestamp']).total_seconds()) + \
                        first_value['coordinates'][0]

            latitude = (((next_value['coordinates'][1] - first_value['coordinates'][1]) * \
                         (first_value['timestamp'] - timestamp.replace(tzinfo=None)).total_seconds()) / (
                                next_value['timestamp'] - first_value['timestamp']).total_seconds()) + \
                       first_value['coordinates'][1]

            updated_coordinates = [longitude, latitude]
            return updated_coordinates
        else:
            return None
    else:
        return None

def aproximacaoDeLatitudeELongitudeAninhadoMongoDB(timestamp, gps):
    gps = pd.DataFrame(list(gps))

    lower_difference = maxsize
    selected = None

    first_value = None
    next_value = None
    index = 0
    if 'POSICOES' in gps:
        for value in gps['POSICOES']:
            for v in value:
                difference = (v['timestamp'] - timestamp.replace(tzinfo=None)).total_seconds()
                if difference > lower_difference:
                    continue
                else:
                    selected = index
                    lower_difference = difference
                    first_value = v
                    next_value = value[index+1]
                index = index + 1

        if selected is not None:
            longitude = (((next_value['coordinates'][0] - first_value['coordinates'][0]) * \
                          (first_value['timestamp'] - timestamp.replace(tzinfo=None)).total_seconds()) / (
                                 next_value['timestamp'] - first_value['timestamp']).total_seconds()) + \
                        first_value['coordinates'][0]

            latitude = (((next_value['coordinates'][1] - first_value['coordinates'][1]) * \
                         (first_value['timestamp'] - timestamp.replace(tzinfo=None)).total_seconds()) / (
                                next_value['timestamp'] - first_value['timestamp']).total_seconds()) + \
                       first_value['coordinates'][1]

            updated_coordinates = [longitude, latitude]
            return updated_coordinates
        else:
            return None
    else:
        return None


def inserirLatitudeELongitudeSQL(conexao, hora_inicial, hora_final):
    inicio = perf_counter()
    cursor = conexao.cursor()

    sql = "SELECT * FROM bilhetagem_novembro where HORA BETWEEN %s AND %s;"
    valor = (hora_inicial, hora_final)
    cursor.execute(sql, valor)
    bilhetagem = cursor.fetchall()

    for row in bilhetagem:
        com_sql = "SELECT LATITUDE,LONGITUDE FROM gps_novembro where DATA=%s AND HORA=%s AND ID_DICIONARIO=%s"
        valor = (row[8], row[9], row[2])
        cursor.execute(com_sql, valor)
        gps = cursor.fetchone()

        if (gps == None):
            lat_log_gps = aproximacaoDeLatitudeELongitudeSQL(conexao, row[2],
                                                                     row[9],
                                                                     row[8])  # fazer aproximação para receber as informaçoes de lat e long de gps
            com_sql2 = "UPDATE bilhetagem_novembro SET LATITUDE=%s , LONGITUDE=%s WHERE ID_BILHETAGEM=%s"
            try:
                valor = (lat_log_gps[0], lat_log_gps[1], row[0])
                cursor.execute(com_sql2, valor)
                conexao.commit()
            except Exception:
                valor = (None, None, row[0])
                cursor.execute(com_sql2, valor)
                conexao.commit()
        else:
            com_sql2 = "UPDATE bilhetagem_novembro SET LATITUDE=%s , LONGITUDE=%s WHERE ID_BILHETAGEM=%s"
            valor = (gps[0], gps[1], row[0])
            cursor.execute(com_sql2, valor)
            conexao.commit()
        fim = perf_counter()
        return fim - inicio


def inserirLatitudeELongitudeNaPlanar(database_mongo,hora_inicial,hora_final):
    inicio = perf_counter()

    fuso_horario = pytz.timezone('UTC')
    data_inicial = fuso_horario.localize(datetime(2018, 11, 5, hora_inicial, 30, 0))
    data_final = fuso_horario.localize(datetime(2018, 11, 5, hora_final, 30, 0))

    filtro = {'TIMESTAMP': {'$gte': data_inicial, '$lte': data_final}}

    bilhetagem = database_mongo['bilhetagem_novembro_planar'].find(filtro)
    bilhetagem = pd.DataFrame(list(bilhetagem))
    for index, row in bilhetagem.iterrows():
        gps_data = aproximacaoDeLatitudeELongitudeMongoDB(database_mongo, row['ID_DICIONARIO'], row['TIMESTAMP'])
        if gps_data != None:
            row['LATITUDE'] = gps_data[1]
            row['LONGITUDE'] = gps_data[0]
        else:
            row['LATITUDE'] = None
            row['LONGITUDE'] = None

    nova_bilhetagem_planar = database_mongo['bilhetagem_novembro_planar_atualizada']
    documentos = bilhetagem.to_dict('records')
    nova_bilhetagem_planar.insert_many(documentos)
    fim = perf_counter()
    nova_bilhetagem_planar.drop()
    return fim - inicio


def inserirLatitudeELongitudeNaAninhadaMongoDB(database_mongo, hora_inicial, hora_final):
    inicio = perf_counter()

    fuso_horario = pytz.timezone('UTC')
    data_inicial = fuso_horario.localize(datetime(2018, 11, 5, hora_inicial, 30, 0))
    data_final = fuso_horario.localize(datetime(2018, 11, 5, hora_final, 30, 0))

    filtro = {'VALIDACOES.TIMESTAMP': {'$gte': data_inicial, '$lte': data_final}}
    bilhetagem = database_mongo['bilhetagem_novembro_aninhada'].find(filtro)
    bilhetagem = pd.DataFrame(list(bilhetagem))

    for index, row in bilhetagem.iterrows():
        gps = database_mongo.gps_novembro.find({'ID_DICIONARIO': int(row['ID_DICIONARIO'])})
        for row2 in row['VALIDACOES']:
            gps_data = aproximacaoDeLatitudeELongitudeAninhadoMongoDB(row2['TIMESTAMP'],gps)
            if gps_data != None:
                row2['PONTO'] = {'type': 'Point',  'coordinates': [gps_data]}
            else:
                row2['PONTO'] = {'type': 'Point',  'coordinates': None}

    nova_bilhetagem_aninhada = database_mongo['bilhetagem_novembro_aninhada_atualizada']
    documentos = bilhetagem.to_dict('records')
    nova_bilhetagem_aninhada.insert_many(documentos)
    fim = perf_counter()
    nova_bilhetagem_aninhada.drop()
    return fim - inicio

def inserirLatitudeELongitudeComIndiceMongoDB(database_mongo,hora_inicial,hora_final):
    inicio = perf_counter()

    fuso_horario = pytz.timezone('UTC')
    data_inicial = fuso_horario.localize(datetime(2018, 11, 5, hora_inicial, 30, 0))
    data_final = fuso_horario.localize(datetime(2018, 11, 5, hora_final, 30, 0))

    filtro = {'VALIDACOES.TIMESTAMP': {'$gte': data_inicial, '$lte': data_final}}
    bilhetagem = database_mongo['bilhetagem_novembro_indice'].find(filtro)
    bilhetagem = pd.DataFrame(list(bilhetagem))

    for index, row in bilhetagem.iterrows():
        gps = database_mongo.gps_novembro.find({'ID_DICIONARIO': int(row['ID_DICIONARIO'])})
        for row2 in row['VALIDACOES']:
            gps_data = aproximacaoDeLatitudeELongitudeAninhadoMongoDB(row2['TIMESTAMP'], gps)
            if gps_data != None:
                row2['PONTO'] = {'type': 'Point', 'coordinates': [gps_data]}
            else:
                row2['PONTO'] = {'type': 'Point', 'coordinates': None}

    nova_bilhetagem_aninhada = database_mongo['bilhetagem_novembro_indice_atualizada']
    documentos = bilhetagem.to_dict('records')
    nova_bilhetagem_aninhada.insert_many(documentos)
    fim = perf_counter()
    nova_bilhetagem_aninhada.drop()
    return fim - inicio

def inserirBilhetagemPlanarMongoDB(database_mongo, file_path):
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

                timestamp = str(split_row[8] + 'T' + split_row[9] + '.000-0300')
                format_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

                bilhetagem_data = {
                    'ID_BILHETAGEM': int(split_row[0]),
                    'NUMERO_LINHA': int(split_row[1]),
                    'ID_DICIONARIO': int(split_row[2]),
                    'NOME_CARTAO': split_row[3],
                    'SENTIDO': split_row[4],
                    'INTEGRACAO': split_row[5],
                    'NUMERO_CARTAO': int(split_row[6]),
                    'ID_PARADA': int(split_row[7]),
                    'TIMESTAMP': format_date,
                    'LATITUDE': None,
                    'LONGITUDE': None,
                }

                database_mongo.bilhetagem_novembro_planar.insert_one(bilhetagem_data)
                cont = 0
                split_row = {}

            verification = 1


def inserirBilhetagemAninhadaMongoDB(database_mongo, file_path):
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

                timestamp = str(split_row[8] + 'T' + split_row[9] + '.000-0300')
                format_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

                bilhetagem = {'ID_DICIONARIO': int(split_row[2]), 'NUMERO_LINHA': int(split_row[1]),
                              'SENTIDO': split_row[4]}

                validacao = {
                    'ID_BILHETAGEM': int(split_row[0]),
                    'NOME_CARTAO': split_row[3],
                    'INTEGRACAO': split_row[5],
                    'NUMERO_CARTAO': int(split_row[6]),
                    'ID_PARADA': int(split_row[7]),
                    'PONTO': {'type': 'Point', 'coordinates': None},
                    'TIMESTAMP': format_date
                }

                check = database_mongo.bilhetagem_novembro_aninhada.find_one({}, bilhetagem)

                if check == None:
                    bilhetagem_data = {
                        'ID_DICIONARIO': int(split_row[2]),
                        'NUMERO_LINHA': int(split_row[1]),
                        'SENTIDO': split_row[4],
                        'VALIDACOES': []
                    }

                    database_mongo.bilhetagem_novembro_aninhada.insert_one(bilhetagem_data)

                database_mongo.bilhetagem_novembro_aninhada.update_one(bilhetagem, {'$push': {'VALIDACOES': validacao}},
                                                                       upsert=True)

                cont = 0
                split_row = {}

            verification = 1


def inserirBilhetagemComIndiceMongoDB(database_mongo, file_path):
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

                timestamp = str(split_row[8] + 'T' + split_row[9] + '.000-0300')
                format_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

                bilhetagem = {'ID_DICIONARIO': int(split_row[2]), 'NUMERO_LINHA': int(split_row[1]),
                              'SENTIDO': split_row[4]}

                validacao = {
                    'ID_BILHETAGEM': int(split_row[0]),
                    'NOME_CARTAO': split_row[3],
                    'INTEGRACAO': split_row[5],
                    'NUMERO_CARTAO': int(split_row[6]),
                    'ID_PARADA': int(split_row[7]),
                    'PONTO': {'type': 'Point', 'coordinates': None},
                    'TIMESTAMP': format_date
                }

                check = database_mongo.bilhetagem_novembro_indice.find_one({}, bilhetagem)

                if check == None:
                    bilhetagem_data = {
                        'ID_DICIONARIO': int(split_row[2]),
                        'NUMERO_LINHA': int(split_row[1]),
                        'SENTIDO': split_row[4],
                        'VALIDACOES': []
                    }

                    database_mongo.bilhetagem_novembro_indice.insert_one(bilhetagem_data)

                database_mongo.bilhetagem_novembro_indice.update_one(bilhetagem, {'$push': {'VALIDACOES': validacao}},
                                                                     upsert=True)
                database_mongo.bilhetagem_novembro_indice.create_index(
                    [('ID_DICIONARIO', 1), ('VALIDACOES.TIMESTAMP', 1)])

                cont = 0
                split_row = {}

            verification = 1


def selecionarIntervaloDeTempoDeBilhetagem(file_path):
    with open(file_path, 'r', encoding='UTF-8') as csv_arq:
        csv_dict = csv.reader(csv_arq)

        with open('../../resources/tratados/bilhetagem/dia19_hora.csv', 'w', newline='',
                  encoding='UTF-8') as new_csv_arq:
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

                    hora = split_row[10]
                    if hora[0:2] == '21':
                        minutos = hora[3:5]

                        if int(minutos) < 15:  # 14:59
                            new_csv.writerow(row)

                    cont = 0
                    split_row = {}

                verification = 1


def inserirBilhetagemSQL(conexao, file_path):
    with open(file_path, 'r', encoding='UTF-8') as csv_arq:
        csv_dict = csv.reader(csv_arq)
        cursor = conexao.cursor()
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

                com_sql = "INSERT INTO bilhetagem_novembro(ID_BILHETAGEM,NUMERO_LINHA,ID_DICIONARIO,NOME_CARTAO,SENTIDO,INTEGRACAO,NUMERO_CARTAO,ID_PARADA,DATA,HORA,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                valor = (
                    split_row[0], split_row[1], split_row[2], split_row[3], split_row[4], split_row[5], split_row[6],
                    split_row[7], split_row[8], split_row[9], None, None)
                cursor.execute(com_sql, valor)
                conexao.commit()

                cont = 0
                split_row = {}

            verification = 1


def selecionarCoordinatesDaBaseComIndiceMongoDB(database_mongo):
    indice = database_mongo.bilhetagem_novembro_indice.find()
    lat = []
    long = []
    for documento in indice:
        for v in documento['VALIDACOES']:
            try:
                lat.append(json.dumps(v['PONTO']['coordinates'][0]))
                long.append(json.dumps(v['PONTO']['coordinates'][1]))
            except TypeError:
                lat.append(0)
                long.append(0)
    return lat, long
