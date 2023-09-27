# Python 3.11.5

# Para instalar os requirements
pip install -r requirements.txt
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

# Este repositório é uma solução versátil e de fácil implementação para monitoramento de distância usando um sensor ultrassônico com Arduino. Aproveite e personalize conforme suas necessidades específicas.
