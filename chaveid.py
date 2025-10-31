#!/usr/bin/env python3

def chave_identificacao():
    class_veg = input("\nSua planta é monocotiledônea ou eudicotiledônea?: ").rstrip().lower()

    if class_veg in ["monocotiledonea", "monocotiledônea"]:  #aceita com e sem acento, minúscula ou maiúscula

        while True:
            try:
                tipo_morfo = int(input('''\nQual a aparência da sua planta?
1. Palmeira
2. Orquídea
3. Bromélia
4. Outro

Digite sua resposta: '''))

                if tipo_morfo in [1,2,3,4]:
                    break  #sai do loop se a entrada for válida
                else:
                    print("Opção inválida. Por favor, digite um número de 1 a 4.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um NÚMERO de 1 a 4")


        if tipo_morfo == 1:
            familia = "Arecaceae"
        elif tipo_morfo == 2:
            familia = "Orchidaceae"
        elif tipo_morfo == 3:
            familia = "Bromeliaceae"
        else:  #tipo_morfo == 4 (Outro)

            while True:
                flor_visto = input("\nSua planta possui flores vistosas (sim/não)?: ").lower().rstrip()

                if flor_visto == "sim":

                    while True:
                        try:
                            n_estame = int(input("\nA flor da sua planta possui 3 ou 6 estames?: "))

                            if n_estame == 3:
                                familia = "Iridaceae"
                                break
                            elif n_estame == 6:
                                familia = "Amaryllidaceae"
                                break
                            else:
                                print("Resposta inválida. Por favor, digite 3 ou 6")

                        except ValueError:
                            print("Entrada inválida. Por favor, digite '3' ou '6'")

                    break

                elif flor_visto in ["não","nao"]:

                    while True:
                        try:
                            monocot_naovisto = int(input('''\nQual descrição abaixo melhor representa sua planta?: 
1. Bainha fechada, caule triangular e folhas alternas espiraladas
2. Bainha aberta, caule achatado ou circular e folhas alternas dísticas

Digite sua resposta: '''))


                            if monocot_naovisto == 1:
                                familia = "Cyperaceae"
                                break
                            elif monocot_naovisto == 2:
                                familia = "Poaceae"
                                break
                            else:
                                print("Opção inválida. Por favor, digite 1 ou 2.")

                        except ValueError:
                            print("Entrada inválida. Por favor, digite o NÚMERO 1 ou 2")
                    break

                else:
                    print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

    else:
        print("\nTrabalho em construção. Chave para eudicotiledôneas ainda não implementada.")

    if familia:
        print(f"\nSua planta pertence à família {familia}.")
    else:
        print("\nNão foi possível identificar a família da sua planta com as opções fornecidas.")

#-------------------------------------------------------------------------------------------

print('''🌿 Bem-vindo(a) à chave interativa de identificação das principais famílias de monocotiledôneas e eudicotiledôneas!

O que você gostaria de fazer?
----------------------------------------
1. Iniciar a chave de identificação
2. Conhecer melhor o projeto
----------------------------------------
''')

while True:
    try:
        escolha = int(input("Digite sua resposta (1 ou 2): "))
        if escolha not in [1,2]:
            print("⚠️  Opção inválida! Por favor, digite 1 ou 2.\n")
            continue
        break
    except ValueError:
        print("⚠️  Entrada inválida! Digite apenas o número 1 ou 2.\n")

#-------------------------------------------------------------------------------------------

if escolha == 1:
    print('''Antes de começarmos, é importante lembrar que esta chave é um **resumo** — ou seja, não contempla todas as famílias botânicas existentes.

Ela reúne as principais famílias de uso didático e prático, mas o resultado obtido pode não ser o mais preciso em todos os casos.
Use-a com consciência e lembre-se: para identificações mais complexas, é necessário consultar uma chave mais completa.

O que você deseja fazer?
----------------------------------------
1. Estou ciente e quero continuar
2. Gostaria de uma chave mais aprofundada
----------------------------------------
''')

    while True:
        try:
            aprofundamento = int(input("Digite sua resposta: "))
            if aprofundamento == 1:
                print("🌱 Ótimo! Vamos começar o processo de identificação.")
                chave_identificacao()
                break
            else:
                print('''Infelizmente, nosso projeto não traduziu uma chave mais aprofundada ainda.
Entretanto, caso queira, recomendamos checar a seguinte bibliografia:
SOUZA, V.C.; LORENZI, H. Chave de Identificação: Para as principais famílias de Angiospermas e Gimnospermas nativas e cultivadas do Brasil. 4ª ed. Instituto Plantarum: Nova Odessa. 2023.''')
        except ValueError:
            print("⚠️  Entrada inválida! Digite apenas o número 1 ou 2.\n")

#-------------------------------------------------------------------------------------------

elif escolha == 2:
    print('''🌿 Sobre o projeto
========================================
Este script apresenta uma *chave de identificação digital para famílias botânicas*, desenvolvida em **Python** como parte da disciplina *CEN0336 - Introdução à Programação de Computadores Aplicada a Ciências Biológicas*.
A proposta foi criar uma ferramenta interativa que guie você passo a passo na identificação de famílias vegetais, tornando o processo mais intuitivo, acessível e menos sujeito a erros do que as chaves impressas tradicionais. 
Além de facilitar o aprendizado, o projeto busca integrar **biologia e programação**, mostrando como a tecnologia pode apoiar o ensino e a pesquisa científica.
========================================

👩‍🔬 Idealizadores
----------------------------------------
• Adriano Gerolamo do Nascimento  
  Número USP: 11242428

• Lívia Akemi Tahara Amaral  
  Número USP: 5485925

• Jéssica dos Reis de Souza  
  Número USP: 13731942
----------------------------------------
''')

