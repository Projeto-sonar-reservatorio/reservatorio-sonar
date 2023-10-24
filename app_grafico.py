from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
import mysql.connector
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Documents\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Função para buscar dados do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="34456110",
    database="bdprojeto"
    )

cursor = db.cursor()

# Executar a consulta SQL para buscar dados
cursor.execute("SELECT porcentagem, data_leitura FROM leitura_nivel")

# Obter os resultados
resultados = cursor.fetchall()

# Separar os resultados em porcentagem e datas
porcentagem = [resultado[0] for resultado in resultados]
datas = [resultado[1] for resultado in resultados]

# Fechar a conexão com o banco de dados
db.close()

window = Tk()

window.geometry("1000x550")
window.configure(bg = "#505A8C")


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

fig, ax = plt.subplots(figsize=(6, 4.3))
ax.plot(datas, porcentagem, marker='o', linestyle='-')
ax.set_xlabel("Data de leitura")
ax.set_ylabel("Porcentagem")
ax.set_title("Leituras do Sensor Ultrassônico")
ax.tick_params(axis='x', rotation=45)
ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=60, y=100)

window.resizable(False, False)
window.mainloop()
