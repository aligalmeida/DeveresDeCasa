def obter_frase():
    """
    Solicita uma frase ao usuário e verifica se a entrada não está vazia.
    Retorna a frase válida inserida pelo usuário.
    """
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("A entrada não pode estar vazia. Tente novamente.")


def analisar_frase(frase):
    """
    Realiza a análise da frase e retorna os dados processados.
    """
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    palavra_mais_longa = max(palavras, key=len) if palavras else ""
    frase_invertida_por_caracteres = frase[::-1]
    frase_invertida_por_palavras = " ".join(reversed(palavras))
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(palavras)
    
    return {
        "num_caracteres": num_caracteres,
        "num_palavras": num_palavras,
        "palavra_mais_longa": palavra_mais_longa,
        "frase_invertida_por_caracteres": frase_invertida_por_caracteres,
        "frase_invertida_por_palavras": frase_invertida_por_palavras,
        "frase_maiuscula": frase_maiuscula,
        "frase_minuscula": frase_minuscula,
        "tupla_palavras": tupla_palavras
    }


def exibir_resultados(analise):
    """
    Exibe os resultados da análise da frase de maneira formatada.
    """
    print("\n--- Análise da Frase ---")
    print(f"Número de caracteres: {analise['num_caracteres']}")
    print(f"Número de palavras: {analise['num_palavras']}")
    print(f"Palavra mais longa: {analise['palavra_mais_longa']}")
    print(f"Frase invertida por caracteres: {analise['frase_invertida_por_caracteres']}")
    print(f"Frase invertida por palavras: {analise['frase_invertida_por_palavras']}")
    print(f"Frase em maiúsculas: {analise['frase_maiuscula']}")
    print(f"Frase em minúsculas: {analise['frase_minuscula']}")
    print(f"Tupla de palavras: {analise['tupla_palavras']}")


def main():
    """
    Função principal do programa.
    """
    frase = obter_frase()
    analise = analisar_frase(frase)
    exibir_resultados(analise)


if __name__ == "__main__":
    main()