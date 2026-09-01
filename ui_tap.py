import customtkinter as ctk
from automacoes.gerador_tap import rodar_automacao_tap

def criar_tela_tap(app, comando_voltar):
    frame = ctk.CTkScrollableFrame(app, fg_color="transparent")

    # Botão Voltar
    btn_voltar = ctk.CTkButton(frame, text="⬅ Voltar", font=("Roboto", 12, "bold"), width=80, height=30, fg_color="gray", hover_color="#555555", command=comando_voltar)
    btn_voltar.pack(pady=(10, 0), padx=20, anchor="nw")

    titulo = ctk.CTkLabel(frame, text="Gerador de TAP (Termo de Abertura)", font=("Roboto", 24, "bold"))
    titulo.pack(pady=(5, 15))

    # =========================================================
    # BLOCO 1: DADOS BÁSICOS DO CABEÇALHO
    # =========================================================
    ctk.CTkLabel(frame, text="1. Dados Básicos e Cronograma", font=("Roboto", 16, "bold"), text_color="#1f6AA5").pack(anchor="w", padx=20)
    f_dados = ctk.CTkFrame(frame, fg_color="transparent")
    f_dados.pack(pady=5, padx=10)

    input_codigo = ctk.CTkEntry(f_dados, placeholder_text="Código (ex: REPR001-25)", width=230)
    input_codigo.grid(row=0, column=0, padx=5, pady=5)
    input_projeto = ctk.CTkEntry(f_dados, placeholder_text="Nome do Projeto", width=230)
    input_projeto.grid(row=0, column=1, padx=5, pady=5)

    input_versao = ctk.CTkEntry(f_dados, placeholder_text="Versão (ex: 01)", width=230)
    input_versao.grid(row=1, column=0, padx=5, pady=5)
    input_ccv = ctk.CTkEntry(f_dados, placeholder_text="Nº do Projeto (CCV)", width=230)
    input_ccv.grid(row=1, column=1, padx=5, pady=5)

    input_data_abertura = ctk.CTkEntry(f_dados, placeholder_text="Data de Abertura (DD/MM/AAAA)", width=230)
    input_data_abertura.grid(row=2, column=0, padx=5, pady=5)
    input_folha = ctk.CTkEntry(f_dados, placeholder_text="Folha (Opcional)", width=230)
    input_folha.grid(row=2, column=1, padx=5, pady=5)

    input_inicio = ctk.CTkEntry(f_dados, placeholder_text="Início Estimado (DD/MM/AAAA)", width=230)
    input_inicio.grid(row=3, column=0, padx=5, pady=5)
    input_fim = ctk.CTkEntry(f_dados, placeholder_text="Término Estimado (DD/MM/AAAA)", width=230)
    input_fim.grid(row=3, column=1, padx=5, pady=5)

    # =========================================================
    # BLOCO 2: ASSINATURAS E RESPONSÁVEIS
    # =========================================================
    ctk.CTkLabel(frame, text="2. Responsáveis e Assinaturas", font=("Roboto", 16, "bold"), text_color="#1f6AA5").pack(anchor="w", padx=20, pady=(15,0))
    f_ass = ctk.CTkFrame(frame, fg_color="transparent")
    f_ass.pack(pady=5, padx=10)

    input_gerencia = ctk.CTkEntry(f_ass, placeholder_text="Gerência do Contrato (Ex: LUCAS COSTA)", width=470)
    input_gerencia.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Elaboração
    input_elab_nome = ctk.CTkEntry(f_ass, placeholder_text="Elaborado por", width=150)
    input_elab_nome.grid(row=1, column=0, padx=5, pady=5)
    input_elab_data = ctk.CTkEntry(f_ass, placeholder_text="Data Elaboração", width=150)
    input_elab_data.grid(row=1, column=1, padx=5, pady=5)
    input_elab_cargo = ctk.CTkEntry(f_ass, placeholder_text="Cargo [Project Manager]", width=150)
    input_elab_cargo.grid(row=1, column=2, padx=5, pady=5)

    # Revisão
    input_rev_nome = ctk.CTkEntry(f_ass, placeholder_text="Revisado por", width=150)
    input_rev_nome.grid(row=2, column=0, padx=5, pady=5)
    input_rev_data = ctk.CTkEntry(f_ass, placeholder_text="Data Revisão", width=150)
    input_rev_data.grid(row=2, column=1, padx=5, pady=5)
    input_rev_cargo = ctk.CTkEntry(f_ass, placeholder_text="Cargo [Project Manager]", width=150)
    input_rev_cargo.grid(row=2, column=2, padx=5, pady=5)

    # Aprovação
    input_aprov_nome = ctk.CTkEntry(f_ass, placeholder_text="Aprovado por", width=150)
    input_aprov_nome.grid(row=3, column=0, padx=5, pady=5)
    input_aprov_data = ctk.CTkEntry(f_ass, placeholder_text="Data Aprovação", width=150)
    input_aprov_data.grid(row=3, column=1, padx=5, pady=5)
    input_aprov_cargo = ctk.CTkEntry(f_ass, placeholder_text="Cargo [Project Manager]", width=150)
    input_aprov_cargo.grid(row=3, column=2, padx=5, pady=5)

    # =========================================================
    # BLOCO 3: CONTEXTO PARA A INTELIGÊNCIA ARTIFICIAL
    # =========================================================
    ctk.CTkLabel(frame, text="3. Contexto (Para a IA redigir o texto)", font=("Roboto", 16, "bold"), text_color="#1f6AA5").pack(anchor="w", padx=20, pady=(15,0))
    f_ia = ctk.CTkFrame(frame, fg_color="transparent")
    f_ia.pack(pady=5, padx=10)

    input_tipo_emp = ctk.CTkEntry(f_ia, placeholder_text="Tipo (Navio, Plataforma, Datacenter...)", width=230)
    input_tipo_emp.grid(row=0, column=0, padx=5, pady=5)
    input_nome_emp = ctk.CTkEntry(f_ia, placeholder_text="Nome (Ex: CBO Varazze, SE Macaé)", width=230)
    input_nome_emp.grid(row=0, column=1, padx=5, pady=5)

    input_objetivo = ctk.CTkEntry(f_ia, placeholder_text="Objetivo principal (Ex: Modernização da rede)", width=470)
    input_objetivo.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    
    input_descricao = ctk.CTkEntry(f_ia, placeholder_text="Descreva o projeto em uma frase rápida", width=470)
    input_descricao.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # =========================================================
    # BLOCO 4: MATRIZ DE RESPONSABILIDADE E PARTICIPANTES
    # =========================================================
    ctk.CTkLabel(frame, text="4. Matriz e Participantes (Desmarque para remover)", font=("Roboto", 16, "bold"), text_color="#1f6AA5").pack(anchor="w", padx=20, pady=(15,0))
    
    # 4.1 MATRIZ DE ATIVIDADES
    f_matriz = ctk.CTkFrame(frame, fg_color="#2b2b2b")
    f_matriz.pack(pady=5, fill="x", padx=20)
    ctk.CTkLabel(f_matriz, text="🔧 Atividades do Projeto:", font=("Roboto", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))

    # Dicionário e laço rápido para criar os checkboxes das atividades
    atividades = [
        "Materiais e Equipamentos", "Logistica", "Montagem de rack e Rede BR",
        "Sistema Satelitais – LEO", "Sistema Satelitais – GEO", "Sistema de CFTV",
        "Sistema de replicação de Imagens", "Sistema de telefonia", "Sistema de TV UHF", "Sistema de LTE"
    ]
    check_vars_atividades = {}
    for atv in atividades:
        chk = ctk.CTkCheckBox(f_matriz, text=atv)
        chk.pack(pady=2, padx=15, anchor="w")
        chk.select() # Já vem marcado
        check_vars_atividades[atv] = chk

    # 4.2 PARTICIPANTES
    f_equipe = ctk.CTkFrame(frame, fg_color="#2b2b2b")
    f_equipe.pack(pady=5, fill="x", padx=20)
    ctk.CTkLabel(f_equipe, text="👥 Equipe e Aprovadores:", font=("Roboto", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))

    participantes = [
        "Gestor do Projeto (@carlosdamatta)", "Operações (@Andrenorte)", "TI (@Alberto)", 
        "HUB (@jairoferreira)", "Financeiro (@franciscojonas)", "Escritório de Projetos (@fabiodutra)"
    ]
    check_vars_participantes = {}
    for part in participantes:
        chk = ctk.CTkCheckBox(f_equipe, text=part)
        chk.pack(pady=2, padx=15, anchor="w")
        chk.select() # Já vem marcado
        check_vars_participantes[part] = chk
    # =========================================================
    # BLOCO 5: CONSOLE E BOTÃO GERAR
    # =========================================================
    ctk.CTkLabel(frame, text="Console de Status:", text_color="gray").pack(pady=(15, 0))
    caixa_texto = ctk.CTkTextbox(frame, width=480, height=100, font=("Consolas", 12), text_color="#00FF00", fg_color="#1e1e1e")
    caixa_texto.pack(pady=5)
    caixa_texto.insert("0.0", "Aguardando preenchimento do TAP...\n")

    def botao_gerar_tap():
        caixa_texto.insert("end", "\nEmpacotando dados...\n")
        app.update() 
        
        # 1. PACOTE DADOS BÁSICOS
        dados_basicos = {
            "codigo": input_codigo.get().strip(),
            "projeto": input_projeto.get().strip(),
            "versao": input_versao.get().strip() or "01",
            "ccv": input_ccv.get().strip(),
            "data_abertura": input_data_abertura.get().strip(),
            "folha": input_folha.get().strip(),
            "inicio": input_inicio.get().strip(),
            "fim": input_fim.get().strip()
        }
        
        # 2. PACOTE ASSINATURAS
        assinaturas = {
            "gerencia": input_gerencia.get().strip(),
            "elab_nome": input_elab_nome.get().strip(),
            "elab_data": input_elab_data.get().strip(),
            "elab_cargo": input_elab_cargo.get().strip() or "Project Manager",
            "rev_nome": input_rev_nome.get().strip(),
            "rev_data": input_rev_data.get().strip(),
            "rev_cargo": input_rev_cargo.get().strip() or "Project Manager",
            "aprov_nome": input_aprov_nome.get().strip(),
            "aprov_data": input_aprov_data.get().strip(),
            "aprov_cargo": input_aprov_cargo.get().strip() or "Project Manager"
        }
        
        # 3. PACOTE CONTEXTO (PARA A IA)
        contexto = {
            "tipo": input_tipo_emp.get().strip(),
            "nome_emp": input_nome_emp.get().strip(),
            "objetivo": input_objetivo.get().strip(),
            "descricao": input_descricao.get().strip()
        }
        
        # 4. LÊ QUAIS CHECKBOXES FICARAM MARCADOS
        atividades_selecionadas = [nome for nome, checkbox in check_vars_atividades.items() if checkbox.get() == 1]
        participantes_selecionados = [nome for nome, checkbox in check_vars_participantes.items() if checkbox.get() == 1]

        # 5. CHAMA O MOTOR!
        caixa_texto.insert("end", "⚠️ A IA (Ollama) foi acionada. Isso pode levar de 5 a 15 segundos. Aguarde...\n")
        app.update()
        
        try:
            # Chama a função que importamos lá em cima!
            from automacoes.gerador_tap import rodar_automacao_tap
            rodar_automacao_tap(dados_basicos, assinaturas, contexto, atividades_selecionadas, participantes_selecionados)
            caixa_texto.insert("end", "✅ TAP gerado com SUCESSO!\n")
        except Exception as e:
            caixa_texto.insert("end", f"❌ Erro na geração: {e}\n")

    btn_gerar = ctk.CTkButton(frame, text="🚀 GERAR TAP COM INTELIGÊNCIA ARTIFICIAL", font=("Roboto", 16, "bold"), height=50, fg_color="#28a745", hover_color="#218838", command=botao_gerar_tap)
    btn_gerar.pack(pady=20)

    return frame