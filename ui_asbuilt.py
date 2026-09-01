import os
import customtkinter as ctk
from tkinter import filedialog
from automacoes.gerador_asbuilt import rodar_automacao_asbuilt

def criar_bloco_anexo(parent_frame, titulo_sistema):
    frame_anexo = ctk.CTkFrame(parent_frame, fg_color="#2b2b2b")
    frame_anexo.pack(pady=5, fill="x", padx=20)
    
    ctk.CTkLabel(frame_anexo, text=f"📸 Fotos: {titulo_sistema}", font=("Roboto", 14, "bold")).pack(pady=(10,5))
    
    lista_fotos = [] 
    
    def add_foto():
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
        if caminho:
            nome_arquivo = os.path.basename(caminho)
            dialog = ctk.CTkInputDialog(text=f"Digite a legenda para a foto:\n{nome_arquivo}", title="Legenda da Foto")
            legenda_digitada = dialog.get_input()
            
            if not legenda_digitada:
                legenda_digitada = "Foto do Sistema"
                
            lista_fotos.append({"caminho": caminho, "legenda": legenda_digitada.strip()})
            label_status.configure(text=f"{len(lista_fotos)} foto(s) adicionada(s)!")

    ctk.CTkButton(frame_anexo, text="Adicionar Foto", height=30, width=150, command=add_foto).pack(pady=5)
    label_status = ctk.CTkLabel(frame_anexo, text="Nenhuma foto adicionada", text_color="gray")
    label_status.pack(pady=(0,10))
    
    return lista_fotos

def criar_tela_asbuilt(app, comando_voltar):
    frame = ctk.CTkScrollableFrame(app, fg_color="transparent")

    btn_voltar = ctk.CTkButton(frame, text="⬅ Voltar", font=("Roboto", 12, "bold"), width=80, height=30, fg_color="gray", hover_color="#555555", command=comando_voltar)
    btn_voltar.pack(pady=(10, 0), padx=20, anchor="nw")

    titulo = ctk.CTkLabel(frame, text="Gerador de As-Built", font=("Roboto", 24, "bold"))
    titulo.pack(pady=(5, 5))

    # --- FORMULÁRIO DE CABEÇALHO ---
    frame_inputs = ctk.CTkFrame(frame, fg_color="transparent")
    frame_inputs.pack(pady=5)

    input_navio = ctk.CTkEntry(frame_inputs, placeholder_text="Navio (Ex: CBO MANUELLA)", width=230)
    input_navio.grid(row=0, column=0, padx=10, pady=5)
    input_projeto = ctk.CTkEntry(frame_inputs, placeholder_text="Nº PROJETO (Ex: CCV2511-1172)", width=230)
    input_projeto.grid(row=0, column=1, padx=10, pady=5)

    input_emitente = ctk.CTkEntry(frame_inputs, placeholder_text="EMITENTE (Ex: FABIO DUTRA)", width=230)
    input_emitente.grid(row=1, column=0, padx=10, pady=5)
    input_gerencia = ctk.CTkEntry(frame_inputs, placeholder_text="GERÊNCIA (Ex: CARLOS DA MATTA)", width=230)
    input_gerencia.grid(row=1, column=1, padx=10, pady=5)

    input_data = ctk.CTkEntry(frame_inputs, placeholder_text="DATA (Ex: 16/09/2025)", width=230)
    input_data.grid(row=2, column=0, padx=10, pady=5)
    input_modificacao = ctk.CTkEntry(frame_inputs, placeholder_text="DATA MODIFICAÇÃO (30/06/2026)", width=230)
    input_modificacao.grid(row=2, column=1, padx=10, pady=5)

    input_folha = ctk.CTkEntry(frame_inputs, placeholder_text="FOLHA (Ex: 1 a 58)", width=230)
    input_folha.grid(row=3, column=0, padx=10, pady=5)

    frame_rev_versao = ctk.CTkFrame(frame_inputs, fg_color="transparent")
    frame_rev_versao.grid(row=3, column=1, padx=10, pady=5)
    input_rev = ctk.CTkEntry(frame_rev_versao, placeholder_text="REV (01)", width=110)
    input_rev.pack(side="left", padx=(0, 10))
    input_versao = ctk.CTkEntry(frame_rev_versao, placeholder_text="VERSÃO (01)", width=110)
    input_versao.pack(side="left")

    # --- CHECKBOXES DO ESCOPO ---
    ctk.CTkLabel(frame, text="Selecione os sistemas que compõem o escopo:", text_color="gray").pack(pady=(10, 5))
    frame_checkboxes = ctk.CTkFrame(frame, fg_color="transparent")
    frame_checkboxes.pack(pady=0)

    check_telefonia = ctk.CTkCheckBox(frame_checkboxes, text="Sistema de Telefonia", font=("Roboto", 14))
    check_telefonia.pack(pady=5, anchor="w")
    check_leo = ctk.CTkCheckBox(frame_checkboxes, text="Sistema LEO", font=("Roboto", 14))
    check_leo.pack(pady=5, anchor="w")
    check_geo = ctk.CTkCheckBox(frame_checkboxes, text="Sistema GEO", font=("Roboto", 14))
    check_geo.pack(pady=5, anchor="w")
    check_cftv = ctk.CTkCheckBox(frame_checkboxes, text="Sistema de CFTV", font=("Roboto", 14))
    check_cftv.pack(pady=5, anchor="w")
    check_lte = ctk.CTkCheckBox(frame_checkboxes, text="Sistema LTE", font=("Roboto", 14))
    check_lte.pack(pady=5, anchor="w")

    # --- QUANTIDADES (Grid 2x2) ---
    frame_quantidades = ctk.CTkFrame(frame, fg_color="transparent")
    frame_quantidades.pack(pady=10)

    input_qtd_leo = ctk.CTkEntry(frame_quantidades, placeholder_text="Qtd Antenas LEO", width=200)
    input_qtd_leo.grid(row=0, column=0, padx=5, pady=5)
    input_qtd_geo = ctk.CTkEntry(frame_quantidades, placeholder_text="Qtd Antenas GEO", width=200)
    input_qtd_geo.grid(row=0, column=1, padx=5, pady=5)
    input_qtd_cameras = ctk.CTkEntry(frame_quantidades, placeholder_text="Qtd Câmeras CFTV", width=200)
    input_qtd_cameras.grid(row=1, column=0, padx=5, pady=5)
    input_qtd_encoldes = ctk.CTkEntry(frame_quantidades, placeholder_text="Qtd Encoders CFTV", width=200)
    input_qtd_encoldes.grid(row=1, column=1, padx=5, pady=5)

    # --- ANOTAÇÕES DO ESCOPO ---
    ctk.CTkLabel(frame, text="📝 Anotações do Escopo (Para a IA processar):", text_color="gray").pack(pady=(15, 5))
    input_anotacoes = ctk.CTkTextbox(frame, width=480, height=120)
    input_anotacoes.pack(pady=5)
    
    input_unifilar = ctk.CTkEntry(frame, placeholder_text="Sistemas no Unifilar (Padrão: rede, voz, Vsat LEO, GEO e CFTV)", width=480)
    input_unifilar.pack(pady=5)

    # --- BLOCOS DE FOTOS ---
    lista_fotos_telefonia = criar_bloco_anexo(frame, "Sistema Telefonia") # <-- NOVO
    lista_fotos_leo = criar_bloco_anexo(frame, "Sistema LEO")
    lista_fotos_geo = criar_bloco_anexo(frame, "Sistema GEO")
    lista_fotos_cftv = criar_bloco_anexo(frame, "Sistema CFTV")
    lista_fotos_lte = criar_bloco_anexo(frame, "Sistema LTE") # <-- NOVO
    lista_fotos_cronograma = criar_bloco_anexo(frame, "Cronograma de Execução")
    lista_fotos_materiais = criar_bloco_anexo(frame, "Lista de Materiais")

    # --- CONSOLE DE STATUS ---
    ctk.CTkLabel(frame, text="Console de Status do Sistema:", text_color="gray").pack(pady=(20, 0))
    caixa_texto = ctk.CTkTextbox(frame, width=480, height=100, font=("Consolas", 12), text_color="#00FF00", fg_color="#1e1e1e")

    # ⚡ LÓGICA DO BOTÃO "GERAR RELATÓRIO"
    def botao_gerar_clicado():
        caixa_texto.insert("end", "Lendo dados da interface...\n")
        app.update()
        
        sufixo_titulo = input_navio.get().strip().upper()
        
        dados_cabecalho = {
            "num_projeto": input_projeto.get().strip().upper(),
            "emitente": input_emitente.get().strip().upper(),
            "folha": input_folha.get().strip() or "1 a 58",
            "rev": input_rev.get().strip() or "01",
            "gerencia": input_gerencia.get().strip().upper(),
            "titulo": f"ADEQUAÇÃO ANEXO III – {sufixo_titulo}",
            "data": input_data.get().strip(),
            "versao": input_versao.get().strip() or "01",
            "data_modificacao": input_modificacao.get().strip(),
            "titulo_meio_1": "ASBUILT",
            "titulo_meio_2": "ADEQUAÇÃO DE ANEXO III-BR",
            "titulo_meio_3": sufixo_titulo
        }
        
        matriz_escopo = {
            "telefonia": check_telefonia.get() == 1,
            "leo": check_leo.get() == 1,
            "geo": check_geo.get() == 1,
            "cftv": check_cftv.get() == 1,
            "lte": check_lte.get() == 1
        }
        
        dados_sistemas = {
            "leo_qtd": input_qtd_leo.get().strip() or "1",
            "geo_qtd": input_qtd_geo.get().strip() or "1",
            "cftv_cameras": input_qtd_cameras.get().strip() or "0",
            "cftv_encodes": input_qtd_encoldes.get().strip() or "0"
        }
        
        dados_introducao = {
            "anotacoes": input_anotacoes.get("0.0", "end").strip(),
            "sistemas_unifilar": input_unifilar.get().strip() or "rede, voz, Vsat LEO, GEO e CFTV"
        }
        
        dados_fotos = {
            "telefonia": lista_fotos_telefonia,
            "leo": lista_fotos_leo,
            "geo": lista_fotos_geo,
            "cftv": lista_fotos_cftv,
            "lte": lista_fotos_lte,
            "cronograma": lista_fotos_cronograma,
            "materiais": lista_fotos_materiais
        }
        
        try:
            rodar_automacao_asbuilt(dados_cabecalho, matriz_escopo, dados_sistemas, dados_introducao, dados_fotos)
            caixa_texto.insert("end", "✅ Documento gerado com sucesso!\n")
        except Exception as e:
            caixa_texto.insert("end", f"❌ Erro: {e}\n")

    btn_gerar = ctk.CTkButton(frame, text="🚀 GERAR RELATÓRIO", font=("Roboto", 16, "bold"), height=50, command=botao_gerar_clicado)
    btn_gerar.pack(pady=20)
    
    caixa_texto.pack(pady=5)
    caixa_texto.insert("0.0", "Aguardando comando...\n")

    return frame