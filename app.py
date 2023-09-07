import serial
import mysql.connector
from datetime import datetime

# Configuração da porta serial
ser = serial.Serial('COMX', 9600)  # Substitua 'COMX' pela porta serial correta

# Conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = db.cursor()

while True:
    # Ler a distância da porta serial
    distancia_cm = int(ser.readline().strip())
    
    # Calcular a porcentagem
    porcentagem = round(100-(distancia_cm * 100 / 360), 2)
    
    # Obter a data atual
    data_leitura = datetime.now()
    
    # Inserir dados no banco de dados / tabelas do banco de dados : data_leitura, distancia_cm e porcentagem
    cursor.execute("INSERT INTO leitura_nivel (data_leitura, distancia_cm, porcentagem) VALUES (%s, %s, %s)",
                   (data_leitura, distancia_cm, porcentagem))
    
    db.commit()  # Salvar as alterações no banco de dados
    
    # Escrever no arquivo de log
    with open("log.txt", "a") as log_file:
        log_file.write(f"Data: {data_leitura}, distancia: {distancia_cm}, Porcentagem: {round(porcentagem, 2)}%\n")

