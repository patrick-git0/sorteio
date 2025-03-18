import random

def sorteio():
    print("### SORTEIO ###")
    participantes = []

    # Coletando os nomes dos participantes
    while True:
        nome = input("Digite o nome do participante (ou pressione Enter para finalizar): ").strip()
        if nome == "":
            break
        participantes.append(nome)

    # Verifica se há participantes suficientes
    if len(participantes) == 0:
        print("Nenhum participante cadastrado. Sorteio cancelado!")
        return

    # Realiza o sorteio
    vencedor = random.choice(participantes)
    print("\n🎉 O vencedor do sorteio é:", vencedor, "🎉")

# Executa o sorteio
if __name__ == "__main__":
    sorteio()