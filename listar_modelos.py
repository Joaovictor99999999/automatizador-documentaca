from google import genai

# Lembre-se de colocar a sua chave real aqui
client = genai.Client(api_key="AQ.Ab8RN6IJbFB7xuGm7A87mIhrX2QKxq46NnlFKygjTI2lu_rX5w")

print("🔍 Modelos de texto disponíveis para a sua chave:")
for modelo in client.models.list():
    # Filtra apenas os modelos principais para facilitar a leitura
    if "flash" in modelo.name or "pro" in modelo.name:
        print(f"- {modelo.name}")