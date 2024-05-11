# attaia

Algoritmos pra trânsito e transporte público de passageiros

# Detalhamento das consultas

1. Incluir a informação de latitude e longitude na base de bilhetagem. 

# Detalhamento das bases

## Paradas

stop_id:	Identificador da parada  
stop_code:	Inexistente  
stop_name:	Endereço da parada  
stop_desc:	Inexistente  
stop_lat:	Latitude  
stop_lon:	Longitude  
zone_id:	Inexistente  
stop_url:	Inexistente  
location_type:	Tipo de Localização  
parent_station:	Inexistente  
stop_timezone:	Inexistente  
wheelchair_boarding:	Inexistente  

## Bairros

COD_BAIRRO:	Identificador do Bairro  
NOME:	Nome do bairro  
COD_BA_IBG:	Código do IBGE para o bairro  
REGIONAL:	Número da divisão Regional (2018)  
ZONA:	Região da cidade  

## Data do calendário

service_id:	Identificador do serviço  
date:	Data  
exception_type:	Tipo de Exceção  

## Calendário

service_id:	Identificador do tipo de serviço   
monday:	Identificador binário (1 – Sim, 0 - Não)   
tuesday:	Identificador binário (1 – Sim, 0 - Não)  
wednesday:	Identificador binário (1 – Sim, 0 - Não)  
thursday:	Identificador binário (1 – Sim, 0 - Não)  
friday:	Identificador binário (1 – Sim, 0 - Não)  
saturday:	Identificador binário (1 – Sim, 0 - Não)  
sunday:	Identificador binário (1 – Sim, 0 - Não)  
start_date:	Data de início do calendário   
end_date:	Data final do calendário  

## Cadastro dos Usuários

CIA:	Identificador geral do cadastro  
Nome:	Nome do usuário  
DataCadastro:	Data do Cadastro  
Endereco:	Nome da rua e número do endereço do usuário  
Bairro:	Bairro do endereço do usuário  
Cidade:	Cidade do endereço do usuário  
UF:	Código do estado do endereço do usuário  
Cep:	CEP do endereço do usuário  
TipoCartao:	Identificador do tipo de cartão  
NumeroSigom:	Identificador do Smartcard  
NumeroChip:	Número do chip  
Empresa:	Nome da empresa/universidade solicitante  
EnderecoEmpresa:	Nome da rua e número do endereço da empresa/universidade  
BairroEmpresa:	Bairro do endereço da empresa/universidade  
CidadeEmpresa:	Cidade do endereço da empresa/universidade  
UFEmpresa:	Código do estado do endereço da empresa/universidade  


## Regras de Tarifa

fare_id:	Identificador da regra de tarifa  
route_id:	Identificador da rota  
origin_id:	Inexistente  
destination_id:	Inexistente  
contains_id:	Inexistente  
route_type:	Inexistente  
route_url:	Inexistente  
route_color:	Inexistente  
route_text_color:	Inexistente  

## Atributos de Tarifa

fare_id:	Identificador da tarifa  
price:	Valor da tarifa  
currency_type:	Moeda  
payment_method:	Método de pagamento  
transfers:	Inexistente  
transfer_duration:	Inexistente  

## GPS

direction:	Azimute  
latitude:	Latitude  
longitude:	Longitude  
metrictimestamp:	Data e hora agregados   
odometer:	Distância percorrida  
routecode:	Inexistente   
speed:	Velocidade média  
device_deviceid:	Número do dispositivo  
vehicle_vehicleid:	Identificador do veículo  

## Rotas

route_id:	Identificador da rota   
agency_id:	Identificador da agência   
route_short_name:	Nome reduzido da rota    
route_long_name:	Nome completo da rota   
route_desc:	Inexistente  
route_type:	Tipo de rota   
route_url:	Inexistente  
route_color:	Inexistente  
route_text_color:	Inexistente  

## Agência

agency_id:	Identificador da Agência  
agency_name:	Nome da agência reguladora  
agency_url:	Endereço web  
agency_timezone:	Timezona  
agency_lang:	Idioma  
agency_phone:	Telefone  
agency_fare_url:	Inexistente  

## Bilhetagem

id:	Identificador do Smartcard  
linha:	Número da linha  
nome_linha:	Nome da Linha  
prefixo_carro:	Prefixo do carro  
Dia:	Data e hora da validação  
tipo_cartao:	Número do tipo de cartão  
nome_cartao:	Descrição do tipo de cartão  
sentido_viagem:	Sentido da viagem  
integracao:	Integração  

## Dicionario

Contém as informações dos ônibus para o uso em bilhetagem e em GPS  

vehicleid:	Identificador do veículo - GPS  
numbus:	Prefixo do carro - Bilhetagem  
