def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def main():
    num_notas = int(input("Quantas notas você deseja inserir? "))
    
    notas = []
    for i in range(num_notas):
        nota = float(input(f"Informe a nota {i+1}: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    main()
