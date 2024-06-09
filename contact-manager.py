from Main import calcular_media

def calcular_boletim(notas_por_disciplina, nota_minima_aprovacao):
    medias_por_disciplina = {}
    for disciplina, notas in notas_por_disciplina.items():
        media = calcular_media(notas)
        medias_por_disciplina[disciplina] = media
    
    media_geral = sum(medias_por_disciplina.values()) / len(medias_por_disciplina)
    
    if media_geral >= nota_minima_aprovacao:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    
    return media_geral, resultado

def main():
    num_disciplinas = int(input("Quantas disciplinas você deseja inserir? "))
    
    notas_por_disciplina = {}
    for i in range(num_disciplinas):
        disciplina = input(f"Informe o nome da disciplina {i+1}: ")
        notas = []
        num_notas = int(input(f"Quantas notas você deseja inserir para {disciplina}? "))
        for j in range(num_notas):
            nota = float(input(f"Informe a nota {j+1} para {disciplina}: "))
            notas.append(nota)
        notas_por_disciplina[disciplina] = notas
    
    nota_minima_aprovacao = float(input("Informe a nota mínima para aprovação: "))
    
    media_geral, resultado = calcular_boletim(notas_por_disciplina, nota_minima_aprovacao)
    
    print("---- Boletim ----")
    for disciplina, media in notas_por_disciplina.items():
        print(f"{disciplina}: {media}")
    print(f"Média Geral: {media_geral:.2f}")
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
