# Tabelas

## Zonas

    import csv


    def zonas_sql(conexao, file_path):
        with open(file_path, 'r', encoding='UTF-8') as csv_arq:
            csv_dict = csv.reader(csv_arq)

            verification = 0
            split_row = {}
            cont = 0

            for row in csv_dict:
                if verification == 0:
                    pass
                if verification == 1:
                    for row2 in row:
                        split_row[cont] = row2
                        cont += 1

                    com_sql = 'INSERT INTO zona(ID_ZONA,MUNICIPIO) VALUES(%s,%s)'
                    valor = (int(split_row[2]), 'FORTALEZA')
                    conexao.cursor().execute(com_sql, valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Rotas

    import csv

    def rotas_sql(conexao,file_path):
        with open(file_path, 'r',encoding='UTF-8') as csv_arq:

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

                    com_sql = "INSERT INTO rotas(ID_ROTAS,ID_AGENCIA,NOME,TIPO) VALUES(%s,%s,%s,%s)"
                    valor = (split_row[0],split_row[1],split_row[3],split_row[5])
                    conexao.cursor().execute(com_sql, valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Regras de Tarifa

    import csv

    def regras_tarifa_sql(conexao,file_path):
        with open(file_path, 'r') as csv_arq:
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

                    com_sql = "INSERT INTO regras_tarifa(ID_TARIFA,ID_ROTAS) VALUES(%s,%s)"
                    valor = (split_row[0],split_row[1])
                    conexao.cursor().execute(com_sql, valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Paradas

    import csv

    def paradas_sql(conexao,file_path):
        with open(file_path, 'r',encoding='UTF-8') as csv_arq:
            csv_dict = csv.reader(csv_arq)
            verification = 0
            split_row = {}
            cont = 0

            for row in csv_dict: 
                if verification == 0:
                    pass
                if verification == 1:

                    for row2 in row:
                        split_row[cont] = row2
                        cont += 1

                    com_sql = "INSERT INTO paradas(ID_PARADA,NOME_PARADA,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s)"
                    valor = (int(split_row[0]),split_row[2],split_row[4],split_row[5])
                    conexao.cursor().execute(com_sql,valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Data do Calendário

    import csv

    def data_calendario_sql(conexao,file_path):
        with open(file_path, 'r') as csv_arq:
            csv_dict = csv.reader(csv_arq)
            verification = 0
            split_row = {}
            cont = 0

            for row in csv_dict:
                if verification == 0:
                    pass
                if verification == 1:

                    for row2 in row:
                        split_row[cont] = row2
                        cont += 1

                    com_sql = 'INSERT INTO datas_calendario(ID_SERVICO,DATA,TIPO_EXCECAO) VALUES(%s,%s,%s)'
                    valor = (split_row[0], split_row[1], split_row[2])
                    conexao.cursor().execute(com_sql, valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

            verification = 1

## Calendário

    import csv

    def calendario_sql(conexao,file_path):
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

                    com_sql = "INSERT INTO calendario(ID_CALENDARIO,SEGUNDA,TERCA,QUARTA,QUINTA,SEXTA,SABADO,DOMINGO,DATA_INICIO,DATA_FIM) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    valor = (split_row[0],split_row[1],split_row[2],split_row[3],split_row[4],split_row[5],split_row[6],split_row[7],split_row[8],split_row[9])
                    conexao.cursor().execute(com_sql, valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Cadastro de usuários

    import csv

    def transformar_data(data_antiga):
        data_processo = str(data_antiga)
        data_nova = data_processo[6:10] + "-" + data_processo[3:5] + "-" + data_processo[0:2]
        return data_nova


    def cadastro_usuario_sql(conexao,file_path):
            with open(file_path, 'r') as csv_arq:
                csv_dict = csv.reader(csv_arq,delimiter=';')
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


                        data_cadastro =  transformar_data(split_row[8])
                        data_nascimento = transformar_data(split_row[9])
                        print("Sigon: ",split_row[0])



                        try:

                            com_sql = "INSERT INTO cadastro_usuario(NUMERO_SIGOM,TIPO_CARTAO,FREQ_ME_VAL,DES_FREQ_VAL_SD,DIST_TEMP_MED,DIST_TEMP_SD,N_DIAS_ANO,,ANO,DATA_CADASTRO,DATA_NASCIMENTO,NUMERO_CARTAO,ENDERECO,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            valor = (split_row[0],split_row[1],split_row[2],split_row[3],split_row[4],split_row[5],split_row[6],split_row[7],data_cadastro,data_nascimento,split_row[10],split_row[11],split_row[12],split_row[13])
                            conexao.cursor().execute(com_sql,valor)
                            conexao.commit()

                        except IndexError:
                            com_sql = "INSERT INTO cadastro_usuario(NUMERO_SIGOM,TIPO_CARTAO,FREQ_ME_VAL,DES_FREQ_VAL_SD,N_DIAS_ANO,DATA_CADASTRO,DATA_NASCIMENTO,NUMERO_CARTAO,ENDERECO,LATITUDE,LONGITUDE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            valor = (split_row[0], split_row[1], split_row[2], split_row[3], split_row[4], data_cadastro,
                                    data_nascimento, split_row[7], split_row[8], split_row[9], split_row[10])
                            conexao.cursor().execute(com_sql, valor)
                            conexao.commit()
                            print("não existe esse index!")
                            pass


                        cont = 0
                        split_row = {}
                    verification = 1

## Bairro

    import csv


    def bairro_sql(conexao, file_path):
        with open(file_path, 'r',encoding='UTF-8') as csv_arq:
            csv_dict = csv.reader(csv_arq)
            verification = 0
            split_row = {}
            cont = 0

            for row in csv_dict:
                if verification == 0:
                    pass
                if verification == 1:
                    for row2 in row:
                        split_row[cont] = row2
                        cont += 1

                    com_sql = "INSERT INTO bairro(ID_BAIRRO,NOME,COD_BAIRRO_IBGE,REGIONAL) VALUES(%s,%s,%s,%s)"
                    valor = (split_row[0], split_row[1], split_row[2], split_row[3])
                    conexao.cursor().execute(com_sql, valor)

                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Atributo de tarifa
  
    import csv


    def atributo_tarifa_sql(conexao,file_path):
        with open(file_path, 'r') as csv_arq:
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
                        print(split_row)

                    com_sql = "INSERT INTO atributos_tarifa(PRECO,MOEDA,METODO_PAGAMENTO) VALUES(%s,%s,%s)"
                    valor = (split_row[1],split_row[2],split_row[3])
                    conexao.cursor().execute(com_sql,valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1

## Agencia

    import csv

    def agencia_sql(conexao,file_path):
        with open(file_path, 'r') as csv_arq:
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

                    com_sql = "INSERT INTO agencia(NOME,URL,TIMEZONA,LINGUAGEM,TELEFONE) VALUES(%s,%s,%s,%s,%s)"
                    valor = (split_row[1], split_row[2], split_row[3], split_row[4], split_row[5])
                    conexao.cursor().execute(com_sql, valor)
                    conexao.commit()
                    cont = 0
                    split_row = {}

                verification = 1