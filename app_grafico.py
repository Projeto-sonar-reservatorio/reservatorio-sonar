import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Função para buscar dados do banco de dados
def buscar_dados():
    try:
        # Conectar ao banco de dados
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha",
            database="seu_banco_de_dados"
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

        # Criar o gráfico
        criar_grafico(porcentagem, datas)
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao buscar dados do banco de dados: {e}")

# Função para criar o gráfico
def criar_grafico(porcentagem, datas):
    plt.figure(figsize=(10, 6))
    plt.plot(datas, porcentagem, marker='o', linestyle='-')
    plt.xlabel("Data de Leitura")
    plt.ylabel("Porcentagem")
    plt.title("Leituras do Sensor Ultrassônico")
    plt.xticks(rotation=45)
    plt.grid(True)

    # Incorporar o gráfico no aplicativo Tkinter
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Configuração da janela principal
root = tk.Tk()
root.title("Gráfico de Leituras do Reservatório")

# Botão para buscar dados e criar o gráfico
buscar_button = ttk.Button(root, text="Buscar Dados", command=buscar_dados)
buscar_button.pack(ipadx=5, ipady=5, expand=True)

# Loop principal do Tkinter
root.mainloop()
