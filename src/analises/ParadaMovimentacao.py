import csv
from time import perf_counter
from datetime import datetime

import src.analises.GpsToBilhetagem


def converterParaSegundos(time):
    return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])

def inserirBilhetagemPlanarMongoDB(database_mongo,file_path):
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

                bilhetagem_data = {
                    'ID_BILHETAGEM': int(split_row[0]),
                    'NUMERO_LINHA': int(split_row[1]),
                    'ID_DICIONARIO': int(split_row[2]),
                    'NOME_CARTAO': split_row[3],
                    'TIPO_CARTAO': split_row[4],
                    'SENTIDO':split_row[5],
                    'INTEGRACAO':split_row[6],
                    'NUMERO_CARTAO':int(split_row[7]),
                    'ID_PARADA':int(split_row[8]),
                    'DATA': split_row[9],
                    'LATITUDE': None,
                    'LONGITUDE': None,
                }

                database_mongo.bilhetagem_novembro_planar_data.insert_one(bilhetagem_data)
                cont = 0
                split_row = {}

            verification = 1

def inserirBilhetagemAninhadaMongoDB(database_mongo,file_path):
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

                timestamp = str(split_row[9] + 'T' + split_row[10] + '.000-0300')
                format_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

                bilhetagem = {'ID_DICIONARIO': int(split_row[2]), 'NUMERO_LINHA': int(split_row[1]), 'SENTIDO': split_row[5]}

                validacao = {
                    'ID_BILHETAGEM': int(split_row[0]),
                    'NOME_CARTAO': split_row[3],
                    'TIPO_CARTAO': split_row[4],
                    'INTEGRACAO': split_row[6],
                    'NUMERO_CARTAO': int(split_row[7]),
                    'ID_PARADA': int(split_row[8]),
                    'PONTO': {'type': 'Point', 'coordinates': None},
                    'TIMESTAMP': format_date
                }

                check = database_mongo.bilhetagem_novembro_aninhada.find_one({},bilhetagem)

                if check == None:

                    bilhetagem_data = {
                        'ID_DICIONARIO': int(split_row[2]),
                        'NUMERO_LINHA': int(split_row[1]),
                        'SENTIDO': split_row[5],
                        'VALIDACOES': []
                    }

                    database_mongo.bilhetagem_novembro_aninhada.insert_one(bilhetagem_data)

                database_mongo.bilhetagem_novembro_aninhada.update_one( bilhetagem, {'$push': { 'VALIDACOES': validacao } }, upsert = True)

                cont = 0
                split_row = {}

            verification = 1

def inserirBilhetagemComIndiceMongoDB(database_mongo,file_path):
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

                timestamp = str(split_row[9] + 'T' + split_row[10] + '.000-0300')
                format_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')

                bilhetagem = {'ID_DICIONARIO': int(split_row[2]), 'NUMERO_LINHA': int(split_row[1]),
                              'SENTIDO': split_row[5]}

                validacao = {
                    'ID_BILHETAGEM': int(split_row[0]),
                    'NOME_CARTAO': split_row[3],
                    'TIPO_CARTAO': split_row[4],
                    'INTEGRACAO': split_row[6],
                    'NUMERO_CARTAO': int(split_row[7]),
                    'ID_PARADA': int(split_row[8]),
                    'PONTO': {'type': 'Point', 'coordinates': None},
                    'TIMESTAMP': format_date
                }

                check = database_mongo.bilhetagem_novembro_indice.find_one({}, bilhetagem)

                if check == None:
                    bilhetagem_data = {
                        'ID_DICIONARIO': int(split_row[2]),
                        'NUMERO_LINHA': int(split_row[1]),
                        'SENTIDO': split_row[5],
                        'VALIDACOES': []
                    }

                    database_mongo.bilhetagem_novembro_indice.insert_one(bilhetagem_data)

                database_mongo.bilhetagem_novembro_indice.update_one(bilhetagem, {'$push': {'VALIDACOES': validacao}}, upsert=True)
                database_mongo.bilhetagem_novembro_indice.create_index([('ID_DICIONARIO', 1),('VALIDACOES.TIMESTAMP', 1)])

                cont = 0
                split_row = {}

            verification = 1

def selecionarIntervaloDeTempoDeBilhetagem(file_path):
    with open(file_path, 'r', encoding='UTF-8') as csv_arq:
        csv_dict = csv.reader(csv_arq)

        with open('../../resources/tratados/bilhetagem/dia19_hora.csv', 'w', newline='', encoding='UTF-8') as new_csv_arq:
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

                        if int(minutos) < 15: #14:59
                            new_csv.writerow(row)

                    cont = 0
                    split_row = {}

                verification = 1

def inserirBilhetagemSQL(conexao, file_path):
    with open(file_path,'r', encoding='UTF-8') as csv_arq:
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

                com_sql = "INSERT INTO bilhetagem_novembro(ID_BILHETAGEM,NUMERO_LINHA,ID_DICIONARIO,NOME_CARTAO,TIPO_CARTAO,SENTIDO,INTEGRACAO,NUMERO_CARTAO,ID_PARADA,DATA,HORA,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                valor = (
                    split_row[0],split_row[1], split_row[2], split_row[3], split_row[4], split_row[5], split_row[6],
                    split_row[7],split_row[8], split_row[9], split_row[10], None,None)
                cursor.execute(com_sql, valor)
                conexao.commit()

                cont = 0
                split_row = {}

            verification = 1

def inserirParadasSQL(conexao, file_path):
    with open(file_path,'r', encoding='UTF-8') as csv_arq:
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

                com_sql = "INSERT INTO PARADAS(ID_PARADA,ID_ZONA,NOME_PARADA,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s,%s)"
                valor = (
                    split_row[0],split_row[1], split_row[2], split_row[3], split_row[4])
                cursor.execute(com_sql, valor)
                conexao.commit()

                cont = 0
                split_row = {}

            verification = 1

def movimentacaoPorParadasPartindoDeBilhetagemSQL(conexao,data, file_path):
    inicio = perf_counter()
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
                com_sql = "SELECT ID_BILHETAGEM,DATA FROM bilhetagem_novembro where ID_PARADA=%s AND DATA=%s"
                valor = (split_row[0], data)
                cursor.execute(com_sql, valor)
                bilhetagemParadas = cursor.fetchall()
                for parada in bilhetagemParadas:
                    com_sql = 'INSERT INTO bigdata_tp.paradas_movimentacao(ID_PARADA, DATA, NOME_PARADA, ID_BILHETAGEM) VALUES(%s, %s, %s, %s);'
                    valor = (split_row[0],data,split_row[2],parada[0])
                    cursor.execute(com_sql,valor)
                    conexao.commit()


                cont = 0
                split_row = {}

            verification = 1
        fim = perf_counter()
        return fim - inicio


def inserirParadasMongoDB(database_mongo,file_path):
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

                data = {
                    'ID_PARADA':int(split_row[0]),
                    'ID_ZONA':split_row[1],
                    'NOME_PARADA':split_row[2],
                    'LATITUDE':split_row[3],
                    'LONGITUDE': split_row[4]
                }

                database_mongo.paradas.insert_one(data)

                cont = 0
                split_row = {}

            verification = 1


def movimentacaoPorParadasPartindoDeBilhetagemMongoDB(database_mongo,data,idParada: int):
    inicio = perf_counter()

    bilhetagem_filter = {'ID_PARADA': idParada, 'DATA': data}
    bilhetagens = database_mongo.bilhetagem_novembro_planar_data.find_one(bilhetagem_filter)
    paradas = database_mongo.paradas.find_one({'ID_PARADA': idParada})

    if bilhetagens != None:
        for key, bilhetagem in bilhetagens.items():
            if key == 'ID_BILHETAGEM' and bilhetagem != None:
                if paradas != None:
                    for key,parada in paradas.items():
                        if key == 'NOME_PARADA' and parada != None:
                            bilhetagem_data = {
                                'ID_PARADA': idParada,
                                'DATA': data,
                                'NOME_PARADA': parada,
                                'ID_BILHETAGEM': int(bilhetagem)
                            }
                            database_mongo.paradas_movimentacao_planar.insert_one(bilhetagem_data)

    fim = perf_counter()
    return fim - inicio
