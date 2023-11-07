import serial
import mysql.connector
from datetime import datetime
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from matplotlib.figure import Figure
import mysql.connector
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from tkinter import *

# Configuração da porta serial
ser = serial.Serial('COM6', 9600)  # Substitua 'COMX' pela porta serial correta

# Conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="34456110",
    database="bdprojeto"
)

cursor = db.cursor()

# Função para coletar dados do sensor e atualizar o banco de dados
def collect_sensor_data():
    while True:
        distancia_cm = int(ser.readline().strip())
        altura_reservatorio = 35
        porcentagem = round(((altura_reservatorio - (distancia_cm - 4.5)) * 100) / 35)
        data_leitura = datetime.now()

        cursor.execute("INSERT INTO leitura_nivel (data_leitura, distancia_cm, porcentagem) VALUES (%s, %s, %s)",
                       (data_leitura, distancia_cm, porcentagem))
        db.commit()

        with open("log.txt", "a") as log_file:
            log_file.write(f"Data: {data_leitura}, Distancia: {distancia_cm}, Porcentagem: {round(porcentagem, 2)}%\n")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Documents\GitHub\reservatorio-sonar\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_plot():
    porcentagem, datas = get_latest_data_from_db()
    ax.clear()
    #margem de porcentagem critica/risco
    ax.plot(datas, porcentagem, marker='o', linewidth=2.0)
    cmap, norm = mcolors.from_levels_and_colors([0, 2, 5, 6], ['red', 'green', 'blue'])
    plt.scatter(datas, porcentagem, cmap=cmap, norm=norm)
    ax.set_xlabel("Data de leitura")
    ax.set_ylabel("Porcentagem")
    ax.set_title("Leituras do Sensor Ultrassônico")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)
    ax.set_ylim(0, 100)
    canvas.draw()

def get_latest_data_from_db():
    # Conectar ao banco de dados
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="34456110",
        database="bdprojeto"
    )

    cursor = db.cursor()

    # Executar a consulta SQL para buscar os últimos dados inseridos
    cursor.execute("SELECT porcentagem, data_leitura FROM leitura_nivel ORDER BY data_leitura DESC LIMIT 10")  # Seleciona os últimos 10 registros por exemplo

    # Obter os resultados
    resultados = cursor.fetchall()

    # Separar os resultados em porcentagem e datas
    porcentagem = [resultado[0] for resultado in resultados]
    datas = [resultado[1] for resultado in resultados]

    # Fechar a conexão com o banco de dados
    db.close()

    return porcentagem, datas

# Configuração da interface gráfica
def setup_gui():
    # Declaração das variaveis globais
    global fig, ax, canvas, window

    window = tk.Tk()
    window.geometry("1000x550")

    canvas = tk.Canvas(window, bg="#505A8C", height=550, width=1000)
    canvas.pack()

    canvas = Canvas(
    window,
    bg = "#505A8C",
    height = 550,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
    
    canvas = Canvas(
        window,
        bg = "#505A8C",
        height = 550,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )   

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1000.0,
        60.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        209.0,
        6.0,
        anchor="nw",
        text="Dashboard de Nível de Reservatório",
        fill="#000000",
        font=("Noto Sans TC", 32 * -1)
    )

    canvas.create_rectangle(
        0.0,
        60.0,
        713.0,
        550.0,
        fill="#5B5B5B",
        outline="")

    canvas.create_text(
        230.0,
        70.0,
        anchor="nw",
        text="Leitura do tanque por minuto",
        fill="#FFFFFF",
        font=("Noto Sans TC", 20 * -1)
    )

    canvas.create_text(
        810.0,
        91.0,
        anchor="nw",
        text="Nível Atual",
        fill="#FFFFFF",
        font=("Noto Sans TC", 20 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        856.0,
        304.0,
        image=image_image_1
    )

    window.geometry("1000x550")

    fig, ax = plt.subplots(figsize=(6, 4.3))
    ax.set_ylim(0, 100)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=60, y=100)

    # Inicia a atualização do gráfico
    animate()

    window.mainloop()

def animate():
    update_plot()
    window.after(1000, animate)  # Atualiza a cada 2 segundos (2000 milissegundos)

# Inicialização da coleta de dados do sensor em uma thread separada
# Para executar em paralelo com a interface gráfica
# Essa funcionalidade requer a biblioteca threading
import threading
data_thread = threading.Thread(target=collect_sensor_data)
data_thread.daemon = True  # Encerrar a thread quando o programa principal terminar
data_thread.start()

# Inicialização da interface gráfica
setup_gui()
