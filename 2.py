# ==========================================
# Projeto: Pesquisa de Satisfação - TudoWeb
# ==========================================

def executar_pesquisa():
    total_entrevistados = 10 
    
    qtd_excelente = 0
    qtd_ruim = 0

    print("=========================================")
    print("   SISTEMA DE PESQUISA DE SATISFAÇÃO")
    print("=========================================")

    for i in range(1, total_entrevistados + 1):
        print(f"\n--- Entrevistado {i} de {total_entrevistados} ---")
        
        nome = input("Digite o nome do cliente: ")
        
        while True:
            try:
                idade = int(input("Digite a idade do cliente: "))
                break
            except ValueError:
                print("⚠️ Digite um número inteiro válido para a idade.")

        opiniao = 0
        while opiniao not in [1, 2, 3]:
            print("Opções de Atendimento:")
            print(" [1] EXCELENTE")
            print(" [2] BOM")
            print(" [3] RUIM")
            
            try:
                opiniao = int(input("Digite o código da opinião (1, 2 ou 3): "))
                if opiniao not in [1, 2, 3]:
                    print("⚠️ Opção inválida! Escolha apenas 1, 2 ou 3.\n")
            except ValueError:
                print("⚠️ Digite apenas números inteiros.\n")

        if opiniao == 1:
            qtd_excelente += 1
        elif opiniao == 3:
            qtd_ruim += 1

    print("\n=========================================")
    print("          RESULTADO FINAL")
    print("=========================================")
    print(f"Total de entrevistados: {total_entrevistados}")
    print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
    print("=========================================")

if __name__ == "__main__":
    executar_pesquisa()
