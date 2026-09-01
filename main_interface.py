import customtkinter as ctk
from ui_asbuilt import criar_tela_asbuilt
from ui_tap import criar_tela_tap

def criar_tela_home(app, comando_abrir_asbuilt, comando_abrir_tap):
    frame = ctk.CTkScrollableFrame(app, fg_color="transparent")
    
    titulo = ctk.CTkLabel(frame, text="Central de Documentos", font=("Roboto", 28, "bold"))
    titulo.pack(pady=(100, 10))
    subtitulo = ctk.CTkLabel(frame, text="Engenharia de Projetos - OLS", text_color="gray", font=("Roboto", 16))
    subtitulo.pack(pady=(0, 50))

    btn_asbuilt = ctk.CTkButton(frame, text="📄 Gerador de As-Built", font=("Roboto", 16, "bold"), height=60, width=300, command=comando_abrir_asbuilt)
    btn_asbuilt.pack(pady=15)
    
    btn_tap = ctk.CTkButton(frame, text="📝 Gerador de TAP", font=("Roboto", 16, "bold"), height=60, width=300, fg_color="#2b2b2b", hover_color="#3b3b3b", command=comando_abrir_tap)
    btn_tap.pack(pady=15)

    return frame

def iniciar_aplicacao():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("600x750")
    app.title("OLS - Central de Documentos")
    app.resizable(False, False)

    # REGRAS DE NAVEGAÇÃO
    def mostrar_asbuilt():
        tela_home.pack_forget()
        tela_tap.pack_forget()
        tela_asbuilt.pack(fill="both", expand=True)

    def mostrar_tap():
        tela_home.pack_forget()
        tela_asbuilt.pack_forget()
        tela_tap.pack(fill="both", expand=True)

    def mostrar_home():
        tela_asbuilt.pack_forget()
        tela_tap.pack_forget()
        tela_home.pack(fill="both", expand=True)

    # INSTANCIANDO AS TELAS (Usando as funções importadas!)
    tela_home = criar_tela_home(app, mostrar_asbuilt, mostrar_tap)
    tela_asbuilt = criar_tela_asbuilt(app, mostrar_home)
    tela_tap = criar_tela_tap(app, mostrar_home)

    # Inicia pela Home
    tela_home.pack(fill="both", expand=True)
    app.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()