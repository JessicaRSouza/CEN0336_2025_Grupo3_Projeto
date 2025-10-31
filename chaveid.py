#!/usr/bin/env python3
print('''🌿 Bem-vindo(a) à chave interativa de identificação das principais famílias de monocotiledôneas e eudicotiledôneas!

O que você gostaria de fazer?
----------------------------------------
1. Iniciar a chave de identificação
2. Conhecer melhor o projeto
----------------------------------------
''')

escolha = input("Digite sua resposta: ")

#-------------------------------------------------------------------------------------------

if int(escolha) == 1:
	print('''Antes de começarmos, é importante lembrar que esta chave é um **resumo** — ou seja, não contempla todas as famílias botânicas existentes.

Ela reúne as principais famílias de uso didático e prático, mas o resultado obtido pode não ser o mais preciso em todos os casos.
Use-a com consciência e lembre-se: para identificações mais complexas, é necessário consultar uma chave mais completa.

O que você deseja fazer?
----------------------------------------
1. Estou ciente e quero continuar
2. Gostaria de uma chave mais aprofundada
----------------------------------------
''')

	aprofundamento = input("Digite sua resposta: ")

	if int(aprofundamento) == 1:
		print("Ótimo! Vamos começar o processo de identificação.")

	else:
		print('''Infelizmente, nosso projeto não traduziu uma chave mais aprofundada ainda.
Entretanto, caso queira, recomendamos checar a seguinte bibliografia:
SOUZA, V.C.; LORENZI, H. Chave de Identificação: Para as principais famílias de Angiospermas e Gimnospermas nativas e cultivadas do Brasil. 4ª ed. Instituto Plantarum: Nova Odessa. 2023.''')

#-------------------------------------------------------------------------------------------

else:
	print('''🌿 Sobre o projeto
========================================
Este script apresenta uma *chave de identificação digital para famílias botânicas*, 
desenvolvida em **Python** como parte da disciplina 
*CEN0336 - Introdução à Programação de Computadores Aplicada a Ciências Biológicas*.

A proposta foi criar uma ferramenta interativa que guie você passo a passo 
na identificação de famílias vegetais, tornando o processo mais intuitivo, 
acessível e menos sujeito a erros do que as chaves impressas tradicionais. 

Além de facilitar o aprendizado, o projeto busca integrar **biologia e programação**, 
mostrando como a tecnologia pode apoiar o ensino e a pesquisa científica.
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

