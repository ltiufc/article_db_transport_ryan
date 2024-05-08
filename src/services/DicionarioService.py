import csv

def inserirDicionarioSQL(conexao, file_path):
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

                com_sql = 'INSERT INTO dicionario(VEICULO_GPS,VEICULO_BILHETAGEM) VALUES(%s,%s)'
                valor = (split_row[1], split_row[2])
                conexao.cursor().execute(com_sql, valor)
                conexao.commit()
                cont = 0
                split_row = {}

            verification = 1
