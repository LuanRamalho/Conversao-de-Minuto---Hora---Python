import tkinter as tk

def converter_minutos():
    try:
        # Pega a quantidade de minutos da caixa de texto
        minutos = int(entry_minutos.get())
        
        # Converte minutos para horas e minutos restantes
        horas = minutos // 60
        minutos_restantes = minutos % 60
        
        # Atualiza o rótulo de resultado com a conversão
        resultado_label.config(text=f"{horas} horas e {minutos_restantes} minutos")
    except ValueError:
        resultado_label.config(text="Por favor, insira um número válido.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Conversor de Minutos para Horas")
janela.config(bg="#f0f8ff")  # Cor de fundo suave

# Define o tamanho da janela
janela.geometry("350x250")

# Cria a caixa de texto para entrada de minutos com borda arredondada e cor de fundo
entry_minutos = tk.Entry(janela, font=("Arial", 14), width=15, bd=2, relief="solid", fg="black", bg="#fdfd96")
entry_minutos.pack(pady=15)

# Cria o botão para converter os minutos com cor de fundo chamativa
botao_converter = tk.Button(janela, text="Converter", font=("Arial", 14), command=converter_minutos,
                            bg="#4CAF50", fg="white", relief="raised", bd=2, padx=20, pady=10)
botao_converter.pack(pady=10)

# Cria um rótulo para mostrar o resultado com uma cor de fundo suave e borda arredondada
resultado_label = tk.Label(janela, text="", font=("Arial", 14), fg="blue", bg="#f0f8ff", width=25, height=2)
resultado_label.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
