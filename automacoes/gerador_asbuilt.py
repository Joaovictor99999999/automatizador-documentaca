from automacoes.asbuilt_blocos.cabecalho import capturar_e_gerar_cabecalho
from automacoes.asbuilt_blocos.sumario import gerar_sumario_dinamico
from automacoes.asbuilt_blocos.introducao_asbuilt import gerar_bloco_introducao
from automacoes.asbuilt_blocos.dados_telefonia import gerar_bloco_telefonia
from automacoes.asbuilt_blocos.sistema_geo import gerar_bloco_geo
from automacoes.asbuilt_blocos.sistema_cftv import gerar_bloco_cftv
from automacoes.asbuilt_blocos.sistema_lte import gerar_bloco_lte
from automacoes.asbuilt_blocos.cronograma_execucao import gerar_bloco_cronograma
from automacoes.asbuilt_blocos.oficinas import gerar_bloco_oficinas
from automacoes.asbuilt_blocos.lista_materiais import gerar_bloco_materiais
from automacoes.asbuilt_blocos.consideracoes_finais import gerar_bloco_consideracoes
from automacoes.asbuilt_blocos.sistema_leo import gerar_bloco_leo

# (Mantenha todos os seus imports lá em cima como já estavam)

# A função agora recebe os pacotes de dados da Interface!
def rodar_automacao_asbuilt(dados_cabecalho, matriz_escopo, dados_sistemas, dados_introducao, dados_fotos):
    
    # 1. Injeta os dados no cabeçalho
    doc = capturar_e_gerar_cabecalho(dados_cabecalho)
    if doc is None: return  
        
    # 2. Gera sumário e introdução
    doc = gerar_sumario_dinamico(doc, matriz_escopo)
    
    # OBS: Se a introdução ainda precisar de dados, adicione aqui como fizemos nos sistemas
    dados_introducao = {"anotacoes": "", "sistemas_unifilar": ""}
    doc = gerar_bloco_introducao(doc, dados_introducao)

    # 3. OS GATES DE SISTEMAS
    if matriz_escopo["telefonia"]:
        doc = gerar_bloco_telefonia(doc, dados_fotos["telefonia"])
      
    if matriz_escopo["leo"]:
        # Passa a quantidade de antenas LEO
        doc = gerar_bloco_leo(doc, dados_sistemas["leo_qtd"], dados_fotos["leo"])
        
    if matriz_escopo["geo"]:
        # Passa a quantidade de antenas GEO
        doc = gerar_bloco_geo(doc, dados_sistemas["geo_qtd"], dados_fotos["geo"]) 
        
    if matriz_escopo["cftv"]:
        # Corrigido: acessa direto os valores do dicionário dados_sistemas
        doc = gerar_bloco_cftv(doc, dados_sistemas["cftv_encodes"], dados_sistemas["cftv_cameras"], dados_fotos["cftv"])
    
    if matriz_escopo["lte"]:
        doc = gerar_bloco_lte(doc, dados_fotos["lte"])
        
    # 4. BLOCOS OBRIGATÓRIOS FINAIS
    doc = gerar_bloco_cronograma(doc, dados_fotos["cronograma"])
    doc = gerar_bloco_oficinas(doc)
    doc = gerar_bloco_materiais(doc, dados_fotos["materiais"])
    doc = gerar_bloco_consideracoes(doc)

    # ... (restante do código de salvar)

    nome_saida = "Relatorio_AsBuilt_Final.docx"
    
    # O try/except agora não usa print(), porque a interface vai capturar o erro lá na tela
    doc.save(nome_saida)