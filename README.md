# Descrição do projeto

Este trabalho apresenta uma solução visando o desenvolvimento de um sistema de monitoramento de nível de água em caixas d'água de baixo custo. Foi simulado um circuito microcontrolado que faz a interface entre um sensor sonar e um sistema computacional. O sonar é responsável por estimar o volume de água da cisterna ou caixa d'água.  O objetivo é criar um sistema para facilitar a visualização do nível do controle de reservatórios. 


# Python 3.11.5

# Para instalar os requirements
```
pip install -r requirements.txt
```

Os requirements nada mais é do que as bibliotecas python que serão necessárias para rodar os programas do projeto.

# sonar-reservatorio
Este repositório abriga o código-fonte e recursos para um sistema de monitoramento baseado em Arduino que coleta dados de um sensor ultrassônico e os apresenta em um gráfico.

# Principais Recursos
Arduino: Utilizamos a plataforma Arduino para criar uma interface eficiente com o sensor ultrassônico e para processar os dados coletados.

Sensor Ultrassônico: O sistema integra um sensor ultrassônico para medir distâncias com precisão e rapidez.

Comunicação Serial: Os dados coletados são transmitidos por meio da comunicação serial para um dispositivo de exibição, no caso foi utilizado um computador.

Configuração Flexível: O código pode ser facilmente configurado para se adaptar a diferentes cenários de monitoramento.

# Sobre os arquivos .py
Ao utilizar os códigos fornecidos é preciso configura-los para funcionarem em seu determinado sistema. Os códigos possuem configurações para um banco de dados MySQL, então tenha em mente de adicionar corretamente as informações de banco de dados para que o programa não venha ter nenhum erro.

Para rodar os programas.py basta digitar:

python app.py --> para testar o programa de colhimento de dados do sensor.

python app_grafico.py --> para testar o programa de exibição do gráfico do nível de água medido pelo sensor.

# Implementação do sistema

Para implementação do sistema, precisa-se criar uma estrutura de banco de dados no programa MySQL com base nos dados do sensor sonar, é necessario configurar uma conexão com o banco de dados e, em seguida, escrever o código para inserir os dados do sensor no banco de dados.

## Conexão com o banco de dados

Primeiro de tudo, deve-se criar um banco de dados MySQL para esse sistema, pode-se criar um baixando os pacotes de ferramentas direto do site do MySQL que irá facilitar a criação do banco de dados.
Para esse sistema, os dados foram colocados em uma tabela e organaizados em data_de_leitura, distancia e porcentagem.
No arquivo app.py, deverá ser modificado o código de acordo com as especificações do banco de dados onde o sistema será implementado. Por exemplo, no código abaixo, é necessário substituir __"seu_host"__, __"seu_usuario"__, __"sua_senha"__, e __"seu_banco_de_dados"__ pelos valores corretos do banco de dados.

```
import mysql.connector

db = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = db.cursor()
```
## Conexão da porta serial do arduino

Para conectar o arduino ao sistema é preciso ver qual porta o microcontrolador irá funcionar. No arquivo app.py, deverá ser modificado o seguinte código abaixo:

```
# Configuração da porta serial
ser = serial.Serial('COMX', 9600)  # Substitua 'COMX' pela porta serial correta
```


## Este repositório é uma solução versátil e de fácil implementação para monitoramento de distância usando um sensor ultrassônico com Arduino. Aproveite e personalize conforme suas necessidades específicas.
