import os
from automacoes.gerador_tap import rodar_automacao_tap  # Exemplo de como chamaremos depois
from automacoes.gerador_asbuilt import rodar_automacao_asbuilt

def menu_principal():
    print("\n" + "="*40)
    print("🤖 CENTRAL DE AUTOMAÇÃO DE ENGENHARIA - OLS")
    print("="*40)
    print("[1] Gerar Termo de Abertura de Projeto (TAP)")
    print("[2] Gerar Relatório de As-Built")
    print("[3] Gerar Projeto Executivo")
    print("[0] Sair")
    print("="*40)
    
    opcao = input("Escolha o documento que deseja gerar: ").strip()
    
    if opcao == "1":
        print("\n🚀 Iniciando Automação da TAP...")
        rodar_automacao_tap()
    elif opcao == "2":
        print("\n🚀 Iniciando Automação do As-Built...")
        rodar_automacao_asbuilt()
    elif opcao == "3":
        print("\n🚀 Iniciando Automação do Projeto Executivo...")
    elif opcao == "0":
        print("\n👋 Saindo do sistema. Até logo!")
    else:
        print("\n Opção inválida! Tente novamente.")
        menu_principal()

if __name__ == "__main__":
    menu_principal()