from docx.shared import Pt, Inches

class Layout:
    """
    Container global de formatação. 
    Altere os valores aqui para ajustar os limites do documento inteiro de uma vez.
    """
    # --- LIMITES DO CONTAINER (PADDINGS) ---
    RESPIRO_TOPO_PAGINA = Pt(20)       # Distância forçada do teto para o 1º título (após quebra de página)
    ESPACO_ENTRE_BLOCOS = Pt(18)       # Distância padrão entre um título e outro
    RECUO_ESQUERDA_NORMAL = Inches(0)  # Margem do texto padrão
    RECUO_ESQUERDA_TOPICO = Inches(0.4)# Recuo para empurrar os bullet points (•) para a direita
    RECUO_DIREITA_NORMAL = Inches(0.5)
    # --- TIPOGRAFIA PADRÃO ---
    TAMANHO_TITULO_PRINCIPAL = Pt(14)
    TAMANHO_TEXTO_NORMAL = Pt(11)