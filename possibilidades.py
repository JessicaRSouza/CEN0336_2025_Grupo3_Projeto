#!/usr/bin/env python3

def chave_identificacao():

    # 1. Nosso "Banco de Dados" de características
    familias_db = {

        # === Monocotiledôneas ===
        "Arecaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [1]},

        "Orchidaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [2]},

        "Bromeliaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [3]},

        "Iridaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [4],
            "flor_visto": ["sim"],
            "n_estame": [3]},

        "Amaryllidaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [4],
            "flor_visto": ["sim"],
            "n_estame": [6]},

        "Cyperaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [4],
            "flor_visto": ["nao"],
            "monocot_naovisto": [1]},

        "Poaceae": {
            "classe": ["monocot"],
            "tipo_morfo": [4],
            "flor_visto": ["nao"],
            "monocot_naovisto": [2]},

        # === Eudicotiledôneas - Limbo Composto ===
        "Bignoniaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["composto"],
            "filotaxia": ["oposta"]},

        "Fabaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["composto"],
            "filotaxia": ["alterna"],
            "estipulas": ["sim"],
            "gavinhas": ["nao"]},

        "Sapindaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["composto"],
            "filotaxia": ["alterna"],
            "estipulas": ["sim", "nao"],
            "gavinhas": ["sim", "nao"],
            "pontuacoes_translucidas": ["nao"],
            "aromatica": ["nao"]},

        "Rutaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["composto"],
            "filotaxia": ["alterna"],
            "estipulas": ["nao"],
            "pontuacoes_translucidas": ["sim"],
            "aromatica": ["sim"]},

        "Anacardiaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["composto"],
            "filotaxia": ["alterna"],
            "estipulas": ["nao"],
            "pontuacoes_translucidas": ["nao"],
            "aromatica": ["sim"]},

        "Meliaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["composto"],
            "filotaxia": ["alterna"],
            "estipulas": ["nao"],
            "pontuacoes_translucidas": ["nao"],
            "aromatica": ["nao"]},

        # === Eudicotiledôneas - Limbo Simples ===
        "Piperaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["sim"]},

        "Annonaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna"],
            "disposicao_folhas": ["distica"]},

        "Euphorbiaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna"],
            "disposicao_folhas": ["espiralada"],
            "latex": ["sim", "nao"],
            "estipulas": ["sim"],
            "estipulas_tipo": ["lateral"],
            "nectarios_extraflorais": ["sim"]},

        "Moraceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna"],
            "disposicao_folhas": ["espiralada"],
            "latex": ["sim"],
            "estipulas_tipo": ["terminal"]},

        "Malvaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna"],
            "disposicao_folhas": ["espiralada"],
            "latex": ["nao"],
            "estipulas": ["sim"],
            "nectarios_extraflorais": ["nao"]},

        "Solanaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna"],
            "disposicao_folhas": ["espiralada"],
            "latex": ["nao"],
            "estipulas": ["nao"],
            "aroma_foliar_simples": ["desagradavel"]},

        "Lauraceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna"],
            "disposicao_folhas": ["espiralada"],
            "latex": ["nao"],
            "estipulas": ["nao"],
            "aroma_foliar_simples": ["casca_fruta"]},

        "Asteraceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["alterna", "oposta"],
            "disposicao_folhas": ["espiralada"],
            "latex": ["nao"],
            "estipulas": ["nao"],
            "aroma_foliar_simples": ["outro"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["serreada"],
            "aromatica": ["nao"],
            "habito_capitulo": ["sim"]},

        "Melastomataceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["curvinervea"]},

        "Lamiaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["serreada"],
            "aromatica": ["sim"]},

        "Verbenaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["serreada"],
            "aromatica": ["nao"],
            "habito_capitulo": ["nao"]},

        "Myrtaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["lisa"],
            "latex": ["nao"],
            "caract_especifica": ["pont_transluc"]},

        "Rubiaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["lisa"],
            "latex": ["nao"],
            "caract_especifica": ["estipula_interpeciolar"]},

        "Malpighiaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["lisa"],
            "latex": ["nao"],
            "caract_especifica": ["elaioforos"]},

        "Apocynaceae": {
            "classe": ["eudicot"],
            "limbo_foliar": ["simples"],
            "nos_geniculados": ["nao"],
            "filotaxia": ["oposta"],
            "nervacao_foliar": ["nao_curvinervea"],
            "margem_foliar": ["lisa"],
            "latex": ["sim"]}
    }

    # 2. Listas de possibilidades
    possibilidades = list(familias_db.keys())
    backup_possibilidades = []

    # 3. Funções auxiliares de filtragem
    def filtrar_lista(chave_caracteristica, valor_resposta):
        nonlocal possibilidades, backup_possibilidades
        backup_possibilidades = list(possibilidades)
        novas_possibilidades = []
        for familia in possibilidades:
            caracteristicas_familia = familias_db[familia].get(chave_caracteristica, [])
            if valor_resposta in caracteristicas_familia:
                novas_possibilidades.append(familia)
        possibilidades = novas_possibilidades
        return checar_resultado(f"'{chave_caracteristica} = {valor_resposta}'")

    def checar_resultado(pergunta_feita=""):

        # Verifica o estado da lista de possibilidades após um filtro.

        if not possibilidades:
            print(f"\n❌ Nenhuma família corresponde à sua última resposta.")
            print(f"   As famílias possíveis ANTES dessa resposta eram: {backup_possibilidades}")
            return False

        if len(possibilidades) == 1:
            print(f"\n✅ Identificação concluída! A família provável é: **{possibilidades[0]}**")
            return False

        return True

    # --- Início da Chave Interativa ---
    print("\n--- Iniciando a chave ---")

    # Pergunta 1: Classe
    valor_filtro = None
    while True:
        class_veg = input("\nSua planta é monocotiledônea ou eudicotiledônea?: ").rstrip().lower()
        if class_veg in ["monocotiledonea", "monocotiledônea"]:
            valor_filtro = "monocot"
            break

        elif class_veg in ["eudicotiledonea", "eudicotiledônea"]:
            valor_filtro = "eudicot"
            break

        else: print("Opção inválida. Digite 'monocotiledônea' ou 'eudicotiledônea'.")

    if not filtrar_lista("classe", valor_filtro): 
        return

    # -----------------------------------------------------------------
    # Ramo MONOCOTILEDÔNEA
    # -----------------------------------------------------------------
    if valor_filtro == "monocot":
        while True:
            try:
                tipo_morfo = int(input('''\nQual a aparência da sua planta?\n1. Palmeira\n2. Orquídea\n3. Bromélia\n4. Outro\nDigite sua resposta: '''))
                if tipo_morfo in [1, 2, 3, 4]: break

                else: print("Opção inválida. Por favor, digite um número de 1 a 4.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um NÚMERO de 1 a 4.")

        if not filtrar_lista("tipo_morfo", tipo_morfo):
            return

        if tipo_morfo == 4:
            valor_flor_visto = None
            while True:
                flor_visto = input("\nSua planta possui flores vistosas (sim/não)?: ").lower().rstrip()
                if flor_visto == "sim":
                    valor_flor_visto = "sim"
                    break

                elif flor_visto in ["não", "nao"]:
                    valor_flor_visto = "nao"
                    break

                else:
                    print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

            if not filtrar_lista("flor_visto", valor_flor_visto):
                return

            if valor_flor_visto == "sim":
                while True:
                    try:
                        n_estame = int(input("\nA flor da sua planta possui 3 ou 6 estames? (Digite o número): "))
                        if not filtrar_lista("n_estame", n_estame):
                            return

                        if n_estame in [3, 6]:
                            break

                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")

            elif valor_flor_visto == "nao":
                while True:
                    try:
                        monocot_naovisto = int(input('''\nQual descrição abaixo melhor representa sua planta?: \n1. Bainha fechada, caule triangular e folhas alternas espiraladas\n2. Bainha aberta, caule achatado ou circular e folhas alternas dísticas\nDigite sua resposta: '''))
                        if monocot_naovisto in [1, 2]:
                            if not filtrar_lista("monocot_naovisto", monocot_naovisto):
                                return
                            break

                        else:
                            print("Opção inválida. Por favor, digite 1 ou 2.")

                    except ValueError:
                        print("Entrada inválida. Por favor, digite o NÚMERO 1 ou 2.")

    # -----------------------------------------------------------------
    # Ramo EUDICOTILEDÔNEA
    # -----------------------------------------------------------------
    elif valor_filtro == "eudicot":

        # Pergunta E1: Limbo Foliar (Simples vs Composto)
        tipo_limbo = None
        while True:
            tipo_limbo = input("\nA planta tem folhas simples ou compostas?: ").lower().rstrip()
            if tipo_limbo in ["simples", "compostas"]:
                break

            else:
                print("Entrada inválida. Por favor, digite 'simples' ou 'compostas'.")

        valor_filtro_db = tipo_limbo
        if tipo_limbo == "compostas":
            valor_filtro_db = "composto"

        if not filtrar_lista("limbo_foliar", valor_filtro_db):
            return

        # -----------------------------------------------------------------
        # Ramo E1.1: Folhas Compostas (tipo_limbo == "compostas")
        # -----------------------------------------------------------------
        if tipo_limbo == "compostas":
            valor_filo = None
            while True:
                filo = input("\nA filotaxia é oposta ou alterna?: ").lower().rstrip()
                if filo in ['oposta', 'alterna']:
                    valor_filo = filo
                    break

                else:
                    print("Entrada inválida. Digite 'oposta' ou 'alterna'.")

            if not filtrar_lista("filotaxia", valor_filo):
                return

            if valor_filo == 'alterna':
                valor_estipulas = None
                while True:
                    estipulas = input("\nPossui estípulas? (sim/não): ").lower().rstrip()
                    if estipulas == 'sim':
                        valor_estipulas = "sim"
                        break

                    elif estipulas in ['nao', 'não']:
                        valor_estipulas = "nao"
                        break

                    else:
                        print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                if not filtrar_lista("estipulas", valor_estipulas):
                    return

                if valor_estipulas == 'sim':
                    valor_gavinhas = None
                    while True:
                        gavinhas = input("\nÉ uma trepadeira com gavinhas? (sim/nao): ").lower().rstrip()
                        if gavinhas == 'sim':
                            valor_gavinhas = "sim"
                            break

                        elif gavinhas in ['nao', 'não']:
                            valor_gavinhas = "nao"
                            break

                        else:
                            print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                    if not filtrar_lista("gavinhas", valor_gavinhas):
                        return

                elif valor_estipulas == 'nao':
                    valor_pontuacoes = None
                    while True:
                        pontuacoes = input("\nAs folhas possuem pontuações translúcidas? (sim/não): ").lower().rstrip()
                        if pontuacoes == 'sim':
                            valor_pontuacoes = "sim"
                            break

                        elif pontuacoes in ['nao', 'não']:
                            valor_pontuacoes = "nao"
                            break

                        else:
                            print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                    if not filtrar_lista("pontuacoes_translucidas", valor_pontuacoes): return

                    if valor_pontuacoes == 'nao':
                        valor_aromatica = None
                        while True:
                            aromatica = input("\nA planta é aromática ao ser macerada? (sim/não): ").lower().rstrip()
                            if aromatica == 'sim':
                                valor_aromatica = "sim"
                                break

                            elif aromatica in ['nao', 'não']:
                                valor_aromatica = "nao"
                                break

                            else:
                                print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                        if not filtrar_lista("aromatica", valor_aromatica):
                            return

        # -----------------------------------------------------------------
        # Ramo E1.2: Folhas Simples (tipo_limbo == "simples")
        # -----------------------------------------------------------------
        elif tipo_limbo == "simples":
            valor_nos_gen = None
            while True:
                nos_gen = input("\nA planta possui nós geniculados (articulados/inchados)? (sim/não): ").lower().rstrip()
                if nos_gen == 'sim':
                    valor_nos_gen = "sim"
                    break

                elif nos_gen in ['nao', 'não']:
                    valor_nos_gen = "nao"
                    break

                else:
                    print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

            if not filtrar_lista("nos_geniculados", valor_nos_gen):
                return

            if valor_nos_gen == "nao":
                valor_filo_simples = None
                while True:
                    filo_simples = input("\nA filotaxia é oposta ou alterna?: ").lower().rstrip()
                    if filo_simples in ['oposta', 'alterna']:
                        valor_filo_simples = filo_simples
                        break

                    else:
                        print("Entrada inválida. Digite 'oposta' ou 'alterna'.")

                if not filtrar_lista("filotaxia", valor_filo_simples):
                    return

                # --- Ramo S2.1: Folhas Alternas (Simples) ---
                if valor_filo_simples == "alterna":
                    valor_disposicao = None
                    while True:
                        disposicao = input("\nAs folhas são dísticas (em 2 fileiras) ou espiraladas?: ").lower().rstrip()
                        if disposicao == 'disticas' or disposicao == 'dísticas':
                            valor_disposicao = "distica"
                            break

                        elif disposicao == 'espiraladas':
                            valor_disposicao = "espiralada"
                            break

                        else:
                            print("Entrada inválida. Digite 'disticas' ou 'espiraladas'.")

                    if not filtrar_lista("disposicao_folhas", valor_disposicao):
                        return

                    if valor_disposicao == "espiralada":
                        valor_latex = None
                        while True:
                            latex = input("\nA planta possui látex? (sim/não): ").lower().rstrip()
                            if latex == 'sim':
                                valor_latex = "sim"
                                break

                            elif latex in ['nao', 'não']:
                                valor_latex = "nao"
                                break

                            else:
                                print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                        if not filtrar_lista("latex", valor_latex):
                            return

                        if valor_latex == "sim":
                            valor_estipula_tipo = None
                            while True:
                                estipula_tipo = input("\nA estípula é terminal (deixa cicatriz circular) ou lateral?: ").lower().rstrip()
                                if estipula_tipo in ['terminal', 'lateral']:
                                    valor_estipula_tipo = estipula_tipo
                                    break

                                else:
                                    print("Entrada inválida. Digite 'terminal' ou 'lateral'.")

                            if not filtrar_lista("estipulas_tipo", valor_estipula_tipo):
                                return

                        elif valor_latex == "nao":
                            valor_estipulas = None
                            while True:
                                estipulas = input("\nA planta possui estípulas? (sim/não): ").lower().rstrip()
                                if estipulas == 'sim':
                                    valor_estipulas = "sim"
                                    break

                                elif estipulas in ['nao', 'não']:
                                    valor_estipulas = "nao"
                                    break

                                else:
                                    print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                            if not filtrar_lista("estipulas", valor_estipulas):
                                return

                            if valor_estipulas == "sim":
                                valor_nectarios = None
                                while True:
                                    nectarios = input("\nPossui nectários extraflorais (glândulas na folha/pecíolo)? (sim/não): ").lower().rstrip()
                                    if nectarios == 'sim':
                                        valor_nectarios = "sim"
                                        break

                                    elif nectarios in ['nao', 'não']:
                                        valor_nectarios = "nao"
                                        break

                                    else:
                                        print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                                if not filtrar_lista("nectarios_extraflorais", valor_nectarios):
                                    return

                            elif valor_estipulas == "nao":
                                valor_aroma = None
                                while True:
                                    print("\nQual o aroma da planta ao macerar (amassar) a folha?")
                                    aroma = input("1. Aroma desagradável (batata, pimentão)\n2. Aroma de 'casca de fruta' (cítrico, canela)\n3. Outro / Sem aroma especial\nDigite 1, 2 ou 3: ").lower().rstrip()
                                    if aroma == '1':
                                        valor_aroma = "desagradavel"
                                        break

                                    elif aroma == '2':
                                        valor_aroma = "casca_fruta"
                                        break

                                    elif aroma == '3':
                                        valor_aroma = "outro"
                                        break

                                    else:
                                        print("Opção inválida. Digite 1, 2 ou 3.")

                                if not filtrar_lista("aroma_foliar_simples", valor_aroma):
                                    return

                # --- Ramo S2.2: Folhas Opostas (Simples) ---
                elif valor_filo_simples == "oposta":
                    valor_nervacao = None
                    while True:
                        nervacao = input("\nA nervação é curvinérvea (nervuras saem da base e fazem curva até o ápice)? (sim/não): ").lower().rstrip()
                        if nervacao == 'sim':
                            valor_nervacao = "curvinervea"
                            break

                        elif nervacao in ['nao', 'não']:
                            valor_nervacao = "nao_curvinervea"
                            break

                        else:
                            print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                    if not filtrar_lista("nervacao_foliar", valor_nervacao):
                        return

                    if valor_nervacao == "nao_curvinervea":
                        valor_margem = None
                        while True:
                            margem = input("\nA margem foliar é serreada ou lisa?: ").lower().rstrip()
                            if margem in ['serreada', 'lisa']:
                                valor_margem = margem
                                break

                            else:
                                print("Entrada inválida. Digite 'serreada' ou 'lisa'.")

                        if not filtrar_lista("margem_foliar", valor_margem):
                            return

                        if valor_margem == "serreada":
                            valor_aroma_serreada = None
                            while True:
                                aroma_s = input("\nA planta é aromática ao macerar? (sim/não): ").lower().rstrip()
                                if aroma_s == 'sim':
                                    valor_aroma_serreada = "sim"
                                    break

                                elif aroma_s in ['nao', 'não']:
                                    valor_aroma_serreada = "nao"
                                    break

                                else:
                                    print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                            if not filtrar_lista("aromatica", valor_aroma_serreada):
                                return

                            if valor_aroma_serreada == 'nao':
                                valor_habito_aster = None
                                while True:
                                    habito_a = input("\nA planta é uma erva com flores em capítulo (como margarida)? (sim/não): ").lower().rstrip()
                                    if habito_a == 'sim':
                                        valor_habito_aster = "sim"
                                        break

                                    elif habito_a in ['nao', 'não']:
                                        valor_habito_aster = "nao"
                                        break

                                    else:
                                        print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                                if not filtrar_lista("habito_capitulo", valor_habito_aster):
                                    return

                        elif valor_margem == "lisa":
                            valor_latex_lisa = None
                            while True:
                                latex_l = input("\nA planta possui látex? (sim/não): ").lower().rstrip()
                                if latex_l == 'sim':
                                    valor_latex_lisa = "sim"
                                    break

                                elif latex_l in ['nao', 'não']:
                                    valor_latex_lisa = "nao"
                                    break

                                else:
                                    print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

                            if not filtrar_lista("latex", valor_latex_lisa):
                                return

                            if valor_latex_lisa == 'nao':
                                valor_especifico = None
                                while True:
                                    print("\nQual destas características melhor descreve a planta?")
                                    especifico = input(
                                        "1. Pontuações translúcidas (folha contra a luz)\n"
                                        "2. Estípulas interpeciolares (entre os pecíolos)\n"
                                        "3. Glândulas no cálice das flores (elaióforos)\n"
                                        "4. Nenhuma das anteriores\n"
                                        "Digite 1, 2, 3 ou 4: ").lower().rstrip()

                                    if especifico == '1':
                                        valor_especifico = "pont_transluc"
                                        break

                                    elif especifico == '2':
                                        valor_especifico = "estipula_interpeciolar"
                                        break

                                    elif especifico == '3':
                                        valor_especifico = "elaioforos"
                                        break

                                    elif especifico == '4':
                                        valor_especifico = "nenhuma"
                                        break

                                    else:
                                        print("Opção inválida. Digite 1, 2, 3 ou 4.")

                                if not filtrar_lista("caract_especifica", valor_especifico):
                                    return

    # Fim da função
    if len(possibilidades) > 1:
        print("\nℹ️ Não foi possível reduzir a uma única família com as perguntas disponíveis.")
        print(f"As famílias mais prováveis são: {possibilidades}")

#-------------------------------------------------------------------------------------------
# MENU PRINCIPAL
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
    print('''\nAntes de começarmos, é importante lembrar que esta chave é um **resumo** — ou seja, não contempla todas as famílias botânicas existentes.

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
                print("\n🌱 Ótimo! Vamos começar o processo de identificação.")
                chave_identificacao() 
                break
            elif aprofundamento == 2: 
                print('''\nInfelizmente, nosso projeto não traduziu uma chave mais aprofundada ainda.
Entretanto, caso queira, recomendamos checar a seguinte bibliografia:
SOUZA, V.C.; LORENZI, H. Chave de Identificação: Para as principais famílias de Angiospermas e Gimnospermas nativas e cultivadas do Brasil. 4ª ed. Instituto Plantarum: Nova Odessa. 2023.''')
                break 
            else:
                print("⚠️  Opção inválida! Por favor, digite 1 ou 2.\n")
        except ValueError:
            print("⚠️  Entrada inválida! Digite apenas o número 1 ou 2.\n")

#-------------------------------------------------------------------------------------------

elif escolha == 2:
    print('''\n🌿 Sobre o projeto
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
