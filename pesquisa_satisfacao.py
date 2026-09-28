# ==========================================
# Projeto: Pesquisa de Satisfação - TudoWeb
# Descrição: Coleta dados de atendimento e exibe estatísticas.
# ==========================================

def executar_pesquisa():
    # Definição do total de entrevistados
    # DICA: Altere para 50 na entrega final, conforme solicitado no enunciado.
    TOTAL_ENTREVISTADOS = 10 

    # Contadores e acumuladores
    qtd_excelente = 0
    qtd_ruim = 0

    print("=" * 45)
    print("   SISTEMA DE PESQUISA DE SATISFAÇÃO - TUDOWEB")
    print("=" * 45)

    # Estrutura de repetição (for) para coletar os dados
    for i in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
        
        # Coleta de dados básicos
        nome = input("Digite o nome do cliente: ")
        
        # Tratamento simples para garantir idade numérica
        try:
            idade = int(input("Digite a idade do cliente: "))
        except ValueError:
            print("Idade inválida. Considerando 0 por padrão para este teste.")
            idade = 0

        # Validação da opinião usando estrutura de decisão (while + if/elif/else)
        opiniao = 0
        while opiniao not in [1, 2, 3]:
            print("Opções de Atendimento:")
            print(" [1] EXCELENTE")
            print(" [2] BOM")
            print(" [3] RUIM")
            
            try:
                opiniao = int(input("Digite o código da sua opinião (1, 2 ou 3): "))
                if opiniao not in [1, 2, 3]:
                    print("⚠️ Opção inválida! Escolha apenas 1, 2 ou 3.\n")
            except ValueError:
                print("⚠️ Digite apenas números inteiros válidos.\n")

        # Estrutura de decisão para contabilizar as respostas
        if opiniao == 1:
            qtd_excelente += 1
        elif opiniao == 3:
            qtd_ruim += 1
        # Nota: A opção 2 (BOM) foi coletada, mas não exige contador específico pelo enunciado.

    # Exibição dos resultados finais consolidados
    print("\n" + "=" * 45)
    print("       RESULTADO FINAL DA PESQUISA")
    print("=" * 45)
    print(f"Total de entrevistados processados: {TOTAL_ENTREVISTADOS}")
    print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
    print("=" * 45)

# Ponto de entrada do programa
if __name__ == "__main__":
    executar_pesquisa()
