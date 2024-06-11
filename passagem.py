import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Dados da passagem
passageiro = {
    "Nome": "Henrique Oliveira Silva",
    "Data de Nascimento": "08 de maio de 1999",
    "Passaporte": "BR987654321"
}

voo_ida = {
    "Companhia": "Lufthansa",
    "Número do Voo": "LH507",
    "Data": "15 de dezembro de 2025",
    "Partida": "18:00 (horário de Brasília)",
    "Chegada": "10:00 (horário local) no dia 16 de dezembro de 2025",
    "Duração": "11 horas",
    "Classe": "Econômica",
    "Assento": "22A"
}

voo_volta = {
    "Companhia": "Lufthansa",
    "Número do Voo": "LH506",
    "Data": "30 de dezembro de 2025",
    "Partida": "22:00 (horário local)",
    "Chegada": "05:00 (horário de Brasília) no dia 31 de dezembro de 2025",
    "Duração": "12 horas",
    "Classe": "Econômica",
    "Assento": "22B"
}

pagamento = {
    "Preço Total": "R$ 4.500,00",
    "Forma de Pagamento": "Cartão de Crédito",
    "Parcelamento": "5x sem juros"
}

contato = {
    "E-mail": "henriquetech.83@gmail.com",
    "Telefone": "+55 11 98765-4321"
}

reserva = {
    "Código da Reserva": "HOS123456",
    "Política de Cancelamento": "Cancelamento gratuito até 24 horas após a reserva. Taxa de cancelamento de R$ 300,00 após esse período."
}

def criar_interface():
    root = tk.Tk()
    root.title("Passagem Aérea")

    # Frame principal com canvas e scrollbar
    mainframe = ttk.Frame(root)
    mainframe.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(mainframe)
    scrollbar = ttk.Scrollbar(mainframe, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Carregar o ícone da companhia aérea
    try:
        img = Image.open("lufthansa.png")
        img = img.resize((200, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        photo = None

    # Exibir o ícone da companhia aérea, se carregado com sucesso
    if photo:
        ttk.Label(scrollable_frame, image=photo).pack(pady=10)

    ttk.Label(scrollable_frame, text="Confirmação de Reserva", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Dados do Passageiro
    ttk.Label(scrollable_frame, text="Passageiro:", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, pady=5)
    ttk.Label(scrollable_frame, text=f"Nome: {passageiro['Nome']}").pack(anchor=tk.W)
    ttk.Label(scrollable_frame, text=f"Data de Nascimento: {passageiro['Data de Nascimento']}").pack(anchor=tk.W)
    ttk.Label(scrollable_frame, text=f"Passaporte: {passageiro['Passaporte']}").pack(anchor=tk.W)

    # Dados do Voo de Ida
    ttk.Label(scrollable_frame, text="Voo de Ida:", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, pady=5)
    for key, value in voo_ida.items():
        ttk.Label(scrollable_frame, text=f"{key}: {value}").pack(anchor=tk.W)

    # Dados do Voo de Volta
    ttk.Label(scrollable_frame, text="Voo de Volta:", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, pady=5)
    for key, value in voo_volta.items():
        ttk.Label(scrollable_frame, text=f"{key}: {value}").pack(anchor=tk.W)

    # Pagamento
    ttk.Label(scrollable_frame, text="Pagamento:", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, pady=5)
    for key, value in pagamento.items():
        ttk.Label(scrollable_frame, text=f"{key}: {value}").pack(anchor=tk.W)

    # Contato
    ttk.Label(scrollable_frame, text="Contato:", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, pady=5)
    for key, value in contato.items():
        ttk.Label(scrollable_frame, text=f"{key}: {value}").pack(anchor=tk.W)

    # Reserva
    ttk.Label(scrollable_frame, text="Reserva:", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, pady=5)
    for key, value in reserva.items():
        ttk.Label(scrollable_frame, text=f"{key}: {value}").pack(anchor=tk.W)

    root.mainloop()

# Executa a interface
criar_interface()