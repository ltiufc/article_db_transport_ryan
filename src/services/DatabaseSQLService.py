
def droparBaseDeDados(conexao):
    conexao.cursor().execute('DROP TABLE IF EXISTS bairro,zona,paradas,cadastro_usuario,calendario,datas_calendario,atributos_tarifa,agencia,rotas,regras_tarifa')
    conexao.commit()


def criarBancosDeDados(conexao):
    cursor = conexao.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS PARADAS_MOVIMENTACAO('
                                        'ID_PARADA INT,'
                                        'DATA DATE,'
                                        'NOME_PARADA VARCHAR(255),'
                                        'ID_BILHETAGEM INT)')

                                        
    cursor.execute('CREATE TABLE IF NOT EXISTS  GPS_NOVEMBRO(ID_GPS INT PRIMARY KEY,'
                                            'ID_ZONA INT,'
                                            'ID_DICIONARIO INT,'
                                            'IDENTIFICADOR INT,'
                                            'DATA DATE,'
                                            'HORA TIME,'
                                            'LATITUDE DECIMAL(8,6),'
                                            'LONGITUDE DECIMAL(8,6))')

    cursor.execute('CREATE TABLE IF NOT EXISTS BILHETAGEM_NOVEMBRO(ID_BILHETAGEM INT PRIMARY KEY,'
                                        'NUMERO_LINHA INT,'
                                        'ID_DICIONARIO INT,'
                                        'NOME_CARTAO VARCHAR(20),'
                                        'SENTIDO VARCHAR(20),'
                                        'INTEGRACAO VARCHAR(20),'
                                        'NUMERO_CARTAO INT,'
                                        'ID_PARADA INT,'
                                        'DATA DATE,'
                                        'HORA TIME,'
                                        'LATITUDE DECIMAL(8,6),'
                                        'LONGITUDE DECIMAL(8,6))')


    cursor.execute('CREATE TABLE IF NOT EXISTS PARADAS(ID_PARADA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'NOME_PARADA VARCHAR(100),'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6))')

    cursor.execute('CREATE TABLE IF NOT EXISTS  DICIONARIO(ID_DICIONARIO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'VEICULO_GPS INT,'
                                         'VEICULO_BILHETAGEM INT)')

    '''
    #Criar tabela BAIRRO
    cursor.execute('CREATE TABLE IF NOT EXISTS BAIRRO(ID_BAIRRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NOME VARCHAR(50),'
                                         'COD_BAIRRO_IBGE BIGINT,'
                                         'REGIONAL VARCHAR(30))')


    #Criar tabela ZONA
    cursor.execute('CREATE TABLE IF NOT EXISTS ZONA(ID_ZONA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_BAIRRO INT,'
                                         'MUNICIPIO VARCHAR(50),'
                                         'USO_SOLO VARCHAR(50),'
                                         'CONSTRAINT fk_BAIRROZONA FOREIGN KEY (ID_BAIRRO) REFERENCES BAIRRO (ID_BAIRRO))')

    #Criar tabela PARADAS
    cursor.execute('CREATE TABLE IF NOT EXISTS PARADAS(ID_PARADA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'NOME_PARADA VARCHAR(100),'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAPARADAS FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA))')

    #Criar tabela CADASTRO_USUARIO
    cursor.execute('CREATE TABLE IF NOT EXISTS CADASTRO_USUARIO(NUMERO_SIGOM INT AUTO_INCREMENT PRIMARY KEY,'
                                         'TIPO_CARTAO VARCHAR(50),'
                                         'FREQ_ME_VAL DECIMAL(8,6),'
                                         'DES_FREQ_VAL_SD DECIMAL(8,6),'
                                         'DIST_TEMP_MED DECIMAL(8,6),'
                                         'DIST_TEMP_SD DECIMAL(8,6),'
                                         'N_DIAS_ANO INT,'
                                         'ANO INT,'
                                         'DATA_CADASTRO DATE,'
                                         'DATA_NASCIMENTO DATE,'
                                         'NUMERO_CARTAO VARCHAR(20),'
                                         'ENDERECO  VARCHAR(200),'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6))')





    #Criar tabela CALENDARIO
    cursor.execute('CREATE TABLE IF NOT EXISTS CALENDARIO(ID_CALENDARIO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'SEGUNDA INT,'
                                         'TERCA INT,'
                                         'QUARTA INT,'
                                         'QUINTA INT,'
                                         'SEXTA INT,'
                                         'SABADO INT,'
                                         'DOMINGO INT,'
                                         'DATA_INICIO DATE,'
                                         'DATA_FIM DATE)')

    #Criar tabela DATAS_CALENDARIO
    cursor.execute('CREATE TABLE IF NOT EXISTS DATAS_CALENDARIO(ID_DATAS_CALENDARIO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_SERVICO INT,'
                                         'DATA DATE,'
                                         'TIPO_EXCECAO INT,'
                                         'CONSTRAINT fk_CALENDARIODATAS FOREIGN KEY (ID_SERVICO) REFERENCES CALENDARIO (ID_CALENDARIO))')

    #Criar tabela ATRIBUTOS_TARIFA
    cursor.execute('CREATE TABLE IF NOT EXISTS ATRIBUTOS_TARIFA(ID_TARIFA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'PRECO DOUBLE,'
                                         'MOEDA VARCHAR(10),'
                                         'METODO_PAGAMENTO INT)')

    #Criar tabela AGENCIA
    cursor.execute('CREATE TABLE IF NOT EXISTS AGENCIA(ID_AGENCIA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NOME VARCHAR(20),'
                                         'URL VARCHAR(50),'
                                         'TIMEZONA VARCHAR(50),'
                                         'LINGUAGEM VARCHAR(10),'
                                         'TELEFONE BIGINT)')


    #Criar tabela ROTAS
    cursor.execute('CREATE TABLE IF NOT EXISTS ROTAS(ID_ROTAS INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_AGENCIA INT,'
                                         'NOME VARCHAR(250),'
                                         'TIPO INT,'
                                         'CONSTRAINT fk_AGENCIAROTA FOREIGN KEY (ID_AGENCIA) REFERENCES AGENCIA (ID_AGENCIA))')


    #Criar tabela REGRAS_TARIFA
    cursor.execute('CREATE TABLE IF NOT EXISTS REGRAS_TARIFA(ID_REGRAS_TARIFA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_TARIFA INT,'
                                         'ID_ROTAS INT,'
                                         'CONSTRAINT fk_ATRIBUTOSREGRAS FOREIGN KEY (ID_TARIFA) REFERENCES ATRIBUTOS_TARIFA (ID_TARIFA),'
                                         'CONSTRAINT fk_ROTASREGRAS FOREIGN KEY (ID_ROTAS) REFERENCES ROTAS (ID_ROTAS))')



    cursor.execute('CREATE TABLE IF NOT EXISTS  DICIONARIO(ID_DICIONARIO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'VEICULO_GPS INT,'
                                         'VEICULO_BILHETAGEM INT)')

    


    cursor.execute('CREATE TABLE IF NOT EXISTS BILHETAGEM_NOVEMBRO(ID_BILHETAGEM INT PRIMARY KEY,'
                                        'NUMERO_LINHA INT,'
                                        'ID_DICIONARIO INT,'
                                        'NOME_CARTAO VARCHAR(20),'
                                        'TIPO_CARTAO VARCHAR(20),'
                                        'SENTIDO VARCHAR(20),'
                                        'INTEGRACAO VARCHAR(20),'
                                        'NUMERO_CARTAO INT,'
                                        'ID_PARADA INT,'
                                        'DATA DATE,'
                                        'HORA TIME,'
                                        'LATITUDE DECIMAL(8,6),'
                                        'LONGITUDE DECIMAL(8,6))')


    
    #Criar tabela ZONA_COORDENADA 
    cursor.execute('CREATE TABLE ZONA_COORDENADA(ID_ZONA_COORD INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONACOORD FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA))')
    
    
    #Criar tabela TERMINAL
    cursor.execute('CREATE TABLE TERMINAL(ID_TERMINAL INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NOME VARCHAR(50),'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6))')                                 
    
    
    
    #Criar tabela EMBARQUE_TERMINAL
    cursor.execute('CREATE TABLE EMBARQUE_TERMINAL(ID_EMBARQUE_TERMINAL INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'PORTA_EMBARQUE VARCHAR(20),'
                                         'ID_TERMINAL INT,'
                                         'PREFIXO INT,'
                                         'EMBARQUES INT,'
                                         'PERIODO VARCHAR(20),'
                                         'HORA_PARTIDA TIME,'
                                         'SENTIDO VARCHAR(10),'
                                         'CONSTRAINT fk_TERMINALEMBARQUE FOREIGN KEY (ID_TERMINAL) REFERENCES TERMINAL (ID_TERMINAL),'
                                         'CONSTRAINT fk_ROTASEMBARQUE FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS))')
    
    
    #Criar tabela SHAPE_LINHAS
    cursor.execute('CREATE TABLE SHAPE_LINHAS(ID_SHAPE_LINHAS INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_LINHA INT,'
                                         'TIPO VARCHAR(50),'
                                         'PERIODO VARCHAR(10),'
                                         'COD_OPERACAO INT,'
                                         'CLASSE_VEICULO INT,'
                                         'ID_TERMINAL INT,'
                                         'CONSTRAINT fk_ROTASSHAPELINHA FOREIGN KEY (ID_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_TERMINALSHAPELINHA FOREIGN KEY (ID_TERMINAL) REFERENCES TERMINAL (ID_TERMINAL))')
    
    
    #Criar tabela SHAPE_LINHAS_COORDENADA 
    cursor.execute('CREATE TABLE SHAPE_LINHAS_COORDENADA(ID_SHAPE_LINHAS_COORD INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_SHAPE_LINHAS INT,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_SHAPECOORD FOREIGN KEY (ID_SHAPE_LINHAS) REFERENCES SHAPE_LINHAS (ID_SHAPE_LINHAS))')
    
    
    
    #Criar tabela TRANSBORDO_TERMINAIS
    cursor.execute('CREATE TABLE TRANSBORDO_TERMINAIS(ID_TRANSBORDO_TERMINAIS INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_TERMINAL INT,'
                                         'DATA DATE,'
                                         'PERIODO VARCHAR(10),'
                                         'COD_LINHA_CHEGADA INT,'
                                         'PREFIXO INT,'
                                         'SENTIDO VARCHAR(20),'
                                         'HORA_INICIO TIME,'
                                         'HORA_PARTIDA TIME,'
                                         'COD_LINHA_TRANSFERENCIA INT,'
                                         'TOTAL INT,'
                                         'OCUPACAO INT,'
                                         'CONSTRAINT fk_ROTASTRANSBORDO1 FOREIGN KEY (COD_LINHA_CHEGADA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_ROTASTRANSBORDO2 FOREIGN KEY (COD_LINHA_TRANSFERENCIA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_TERMINALTRANSBORDO FOREIGN KEY (ID_TERMINAL) REFERENCES TERMINAL (ID_TERMINAL))')
    
    
    #Criar tabela SHAPE_GTFS
    cursor.execute('CREATE TABLE SHAPE_GTFS(ID_SHAPE_GTFS INT AUTO_INCREMENT PRIMARY KEY,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'SEQUENCIA_PT INT,'
                                         'SENTIDO VARCHAR(5))')
    
    
    #Criar tabela VIAGENS
    
    cursor.execute('CREATE TABLE VIAGENS(ID_VIAGENS INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ROTAS INT,'
                                         'ID_SERVICO INT,'
                                         'ID_SHAPE_GTFS INT,'
                                         'ACESSIVEL_CADEIRANTE INT,'
                                         'CONSTRAINT fk_ROTASVIAGENS FOREIGN KEY (ID_ROTAS) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_CALENDARIOVIAGENS FOREIGN KEY (ID_SERVICO) REFERENCES CALENDARIO (ID_CALENDARIO),'
                                         'CONSTRAINT fk_SHAPEVIAGENS FOREIGN KEY (ID_SHAPE_GTFS) REFERENCES SHAPE_GTFS (ID_SHAPE_GTFS))')
    
    
    #Criar tabela HORARIO_PARADA
    cursor.execute('CREATE TABLE HORARIO_PARADA(ID_HORARIO_PARADA INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_VIAGENS INT,'
                                         'ID_PARADA INT,'
                                         'HORARIO_CHEGADA TIME,'
                                         'SEQUENCIA_PARADA INT,'
                                         'CONSTRAINT fk_VIAGENSHORARIO FOREIGN KEY (ID_VIAGENS) REFERENCES VIAGENS (ID_VIAGENS),'
                                         'CONSTRAINT fk_PARADASHORARIO FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    
    
    

    
    
    
    #Criar tabelaS de Bilhetagem
    cursor.execute('CREATE TABLE BILHETAGEM_JANEIRO(ID_BILHETAGEM_JANEIRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEM FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEM FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEM FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEM FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_FEVEREIRO(ID_BILHETAGEM_FEVEREIRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMFEV FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMFEV FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMFEV FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMFEV FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_MARCO(ID_BILHETAGEM_MARCO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMMAR FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMMAR FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMMAR FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMMARC FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_ABRIL(ID_BILHETAGEM_ABRIL INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMABR FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMABR FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMABR FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMABR FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_MAIO(ID_BILHETAGEM_MAIO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMMAI FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMMAI FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMMAI FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMMAI FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_JUNHO(ID_BILHETAGEM_JUNHO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMJUN FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMJUN FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMJUN FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMJUN FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_JULHO(ID_BILHETAGEM_JULHO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMJUL FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMJUL FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMJUL FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMJUL FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_AGOSTO(ID_BILHETAGEM_AGOSTO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMAGO FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMAGO FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMAGO FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMAGO FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_SETEMBRO(ID_BILHETAGEM_SETEMBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMSET FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMSET FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMSET FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMSET FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    cursor.execute('CREATE TABLE BILHETAGEM_OUTUBRO(ID_BILHETAGEM_OUTUBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMOUT FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMOUT FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMOUT FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMOUT FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    
    
    
    
    
    '
    cursor.execute('CREATE TABLE BILHETAGEM_DEZEMBRO(ID_BILHETAGEM_DEZEMBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'NUMERO_LINHA INT,'
                                         'ID_DICIONARIO INT,'
                                         'NOME_CARTAO VARCHAR(20),'
                                         'TIPO_CARTAO VARCHAR(20),'
                                         'SENTIDO VARCHAR(20),'
                                         'INTEGRACAO VARCHAR(20),'
                                         'NUMERO_CARTAO INT,'
                                         'ID_PARADA INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'CONSTRAINT fk_ROTASBILHETAGEMDEC FOREIGN KEY (NUMERO_LINHA) REFERENCES ROTAS (ID_ROTAS),'
                                         'CONSTRAINT fk_DICIONARIOBILHETAGEMDEC FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO),'
                                         'CONSTRAINT fk_CADASTROBILHETAGEMDEC FOREIGN KEY (NUMERO_CARTAO) REFERENCES CADASTRO_USUARIO (NUMERO_SIGOM),'
                                         'CONSTRAINT fk_PARADASBILHETAGEMDEC FOREIGN KEY (ID_PARADA) REFERENCES PARADAS (ID_PARADA))')
    
    
    
    #criação das tabelas de gps
    cursor.execute('CREATE TABLE GPS_JANEIRO(ID_GPS_JANEIRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSJAN FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSJAN FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_FEVEREIRO(ID_GPS_FEVEREIRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSFEV FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSFEV FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_MARCO(ID_GPS_MARCO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSMAR FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSMAR FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_ABRIL(ID_GPS_ABRIL INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSABR FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSABR FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_MAIO(ID_GPS_MAIO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSMAI FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSMAI FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_JUNHO(ID_GPS_JUNHO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSJUN FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSJUN FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_JULHO(ID_GPS_JULHO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSJUL FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSJUL FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_AGOSTO(ID_GPS_AGOSTO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSAGO FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSAGO FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_SETEMBRO(ID_GPS_SETEMBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSSET FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSSET FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_OUTUBRO(ID_GPS_OUTUBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSOUT FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSOUT FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_NOVEMBRO(ID_GPS_NOVEMBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSNOV FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSNOV FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    cursor.execute('CREATE TABLE GPS_DEZEMBRO(ID_GPS_DEZEMBRO INT AUTO_INCREMENT PRIMARY KEY,'
                                         'ID_ZONA INT,'
                                         'ID_DICIONARIO INT,'
                                         'IDENTIFICADOR INT,'
                                         'DATA DATE,'
                                         'HORA TIME,'
                                         'LATITUDE DECIMAL(8,6),'
                                         'LONGITUDE DECIMAL(8,6),'
                                         'CONSTRAINT fk_ZONAGPSDEZ FOREIGN KEY (ID_ZONA) REFERENCES ZONA (ID_ZONA),'
                                         'CONSTRAINT fk_DICIONARIOGPSDEZ FOREIGN KEY (ID_DICIONARIO) REFERENCES DICIONARIO (ID_DICIONARIO))')
    
    
    #cursor.execute("DROP TABLE janeiro")
    '''

    conexao.commit()