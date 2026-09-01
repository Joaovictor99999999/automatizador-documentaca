from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Configura a sua chave (depois colocamos isso escondido num arquivo .env por segurança)
genai.configure(api_key="api_key")

def gerar_descricao_inteligente(anotacoes_brutas):
    modelo = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    Você é um engenheiro da OLS Offshore Link Sat escrevendo a seção '1. Descrição' 
    de um documento As-Built naval.
    
    Aqui estão exemplos de como você escreve (Base de Conhecimento OLS):
    - Instalação do sistema de CFTV com 10 câmeras IP Axis, configuração e comissionamento.
    - Substituição das antenas VSAT GEO pelas antenas modernas Intellian vX100 (Rede BR).
    - Adequação do rack de Telecom, aumento da rede de dados e voz.
    - Instalação do sistema LTE 4G/5G com gateway Fortinet, configuração e testes.
    - Instalação do sistema de replicação de imagem nas salas operacionais.
    
    Agora, transforme as seguintes anotações de campo de um técnico em uma lista de 
    tópicos pontuados em português formal e técnico de engenharia.
    
    ANOTAÇÕES DO TÉCNICO:
    {anotacoes_brutas}
    """
    
    resposta = modelo.generate_content(prompt)
    return resposta.text