class Aluno:
    
    def __init__(self):
        self.notas = []
 
        while True:
            nome  = input("Digite o nome do aluno: ")
            
            if nome.replace(" ", "").isalpha():
                self.nome = nome
                break
            else:
                print(f"{nome} nao é um nome válido. Por favor, tente novamente.")
        
        while True:
            matricula = input(f"Olá, {self.nome}! Por favor, digite sua matrícula: ")
            
            try:
                matricula = int(matricula)
                self.matricula = matricula
                break
            except ValueError:
                print(f"{matricula} nao é uma matricula válida. Por favor, tente novamente.")
                
        while True:
            idade = input(f"Certo, {self.nome}, agora nos informe sua idade, por favor: ")
            
            try:
                idade = int(idade)
                self.idade = idade
                break
            except ValueError:
                print(f"{idade} nao é uma idade válida. Por favor, tente novamente.")
                
        for i, texto in enumerate(["primeira", "segunda", "terceira"], start=1):
            while True:
                nota = input(f"Digite a {texto} nota: ")
                try:
                    nota = float(nota)
                    self.notas.append(nota)
                    break
                except ValueError:
                    print(f"{nota} nao é uma nota válida. Por favor, tente novamente.")
    
    def calc_media(self):
        media = sum(self.notas) / len(self.notas)
        self.media = media
        
        if media >= 7:
            print(f"Parabens, com media de {media:.2f} voce está aprovado(a)!")
        elif 4 <= media < 7:
            print(f"Você ficou de recuperaçao com media de {media:.2f}, mas tudo bem, ainda da pra recuperar! Voce consegue.")
        else:
            print(f"Infelizmente voce foi reprovado com media de {media:.2f}, mais foco próximo ano. Boa sorte quando seus pais souberem.")
            
alunos = []

while True:
    aluno = Aluno()
    aluno.calc_media()
    alunos.append(aluno)

    while True:
        escolha = input("Deseja cadastrar outro(a) aluno(a)[S/N]? ").upper()[0]
        if escolha in ("S", "N"):
            break
        print("Escolha inválida, por favor, tente novamente.")

    if escolha == "N":
        break

# Depois de cadastrar todos os alunos
melhor_aluno = max(alunos, key=lambda aluno: aluno.media)
print(f"\nO aluno com a maior média é {melhor_aluno.nome} (matrícula {melhor_aluno.matricula}), com média {melhor_aluno.media:.2f}")
        