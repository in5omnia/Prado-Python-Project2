# Beatriz Gavilan
# 17/11/2021
# beatrizgavilan@tecnico.ulisboa.pt
# Projeto 2 - simular geracoes num prado com animais e obstaculos


def cria_posicao(x, y):  # usando listas
    """
    cria_posicao: int × int → posicao
    Construtor
    Cria uma posicao com as coordenadas dadas.
    """
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return [x, y]


def cria_copia_posicao(posicao):
    """
    cria_copia_posicao: posicao → posicao
    Construtor
    Cria uma copia nova da posicao.
    """
    if not eh_posicao(posicao):
        raise ValueError('cria_copia_posicao: argumentos invalidos')
    return posicao[:]  # OU cria_posicao(p[0], p[1])


def obter_pos_x(posicao):
    """
    obter_pos_x: posicao → int
    Seletor
    Devolve a componente x da posicao p.
    """
    return posicao[0]


def obter_pos_y(posicao):
    """
    obter_pos_y: posicao → int
    Seletor
    Devolve a componente y da posicao p.
    """
    return posicao[1]


def eh_posicao(arg):
    """
    eh_posicao: universal → booleano
    Reconhecedor
    Devolve True se arg eh uma posicao.
    """
    return type(arg) == list and len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int and arg[0] >= 0 and \
           arg[1] >= 0


def posicoes_iguais(posicao1, posicao2):
    """
    posicoes_iguais: posicao × posicao → booleano
    Teste
    Devolve True se as posicoes p1 e p2 sao posicoes e iguais.
    """
    return eh_posicao(posicao1) and eh_posicao(posicao2) and obter_pos_x(posicao1) == obter_pos_x(posicao2)\
           and obter_pos_y(posicao1) == obter_pos_y(posicao2)


def posicao_para_str(posicao):
    """
    posicao_para_str: posicao → str
    Transformador
    Escreve a cadeia de carateres que representa a posicao p.
    """
    return str(tuple(posicao))


def obter_posicoes_adjacentes(posicao):
    """
    obter_posicoes_adjacentes: posicao → tuplo
    Devolve um tuplo com as posicoes adjacentes a p, ordenadas segundo o sentido horario.
    """
    if posicao == [0, 0]:
        return cria_posicao(1, 0), cria_posicao(0, 1)

    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)
    if x == 0:      # nao tem posicoes ah esquerda
        return cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1)

    if y == 0:      # nao tem posicoes acima
        return cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y)

    return cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y)


def ordenar_posicoes(tuplo_posicoes):
    """
    ordenar_posicoes: tuplo → tuplo
    Devolve um tuplo com as mesmas posicoes do argumento, ordenadas segundo a ordem de leitura do prado.
    """
    lista_posicoes = []

    for p in tuplo_posicoes:
        lista_posicoes += [(obter_pos_y(p), obter_pos_x(p))]  # eh lido de baixo para cima, do y menor para o maior, e,
    lista_posicoes = sorted(lista_posicoes)                                   # na mesma linha, le o menor x primeiro

    for i in range(len(lista_posicoes)):
        lista_posicoes[i] = cria_posicao(lista_posicoes[i][1], lista_posicoes[i][0])   # substitui as coordenadas pelas posicoes

    return tuple(lista_posicoes)


def cria_animal(especie, f_reproducao, f_alimentacao):  # usando dicionarios
    """
    cria_animal: str × int × int → animal
    Construtor
    Devolve o animal de especie s, frequencia de reproducao r e frequencia de alimentacao a (quando a=0, eh uma presa).
    """
    animal = {'especie': especie, 'f_reproducao': f_reproducao, 'f_alimentacao': f_alimentacao, 'idade': 0, 'fome': 0}

    if not eh_animal(animal):
        raise ValueError('cria_animal: argumentos invalidos')

    return animal


def cria_copia_animal(animal):
    """
    cria_copia_animal: animal → animal
    Construtor
    Devolve uma nova copia do animal.
    """
    if not eh_animal(animal):
        raise ValueError('cria_copia_animal: argumentos invalidos')

    return animal.copy()


def obter_especie(animal):
    """
    obter especie: animal → str
    Seletor
    Devolve a especie do animal a.
    """
    return animal['especie']


def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal → int
    Seletor
    Devolve a frequencia de reproducao do animal a.
    """
    return animal['f_reproducao']


def obter_freq_alimentacao(animal):
    """
    obter_freq_alimentacao: animal → int
    Seletor
    Devolve a frequencia de alimentacao do animal a (sempre 0 nas presas).
    """
    return animal['f_alimentacao']


def obter_idade(animal):
    """
    obter_idade: animal → int
    Seletor
    Devolve a idade do animal a.
    """
    return animal['idade']


def obter_fome(animal):
    """
    obter_fome: animal → int
    Seletor
    Devolve a fome do animal a (sempre 0 nas presas).
    """
    return animal['fome']


def aumenta_idade(animal):
    """
    aumenta_idade: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos aumentar a sua idade em 1 unidade.
    """
    animal['idade'] += 1
    return animal


def reset_idade(animal):
    """
    reset_idade: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos redefinir a sua idade como 0.
    """
    animal['idade'] = 0
    return animal


def aumenta_fome(animal):
    """
    aumenta_fome: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos aumentar a sua fome em 1 unidade, se este for predador.
    """
    if eh_predador(animal):
        animal['fome'] += 1
    return animal


def reset_fome(animal):
    """
    reset_fome: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos redefinir a sua fome como 0, se este for predador.
    """
    if eh_predador(animal):
        animal['fome'] = 0
    return animal


def eh_animal(arg):
    """
    eh_animal: universal → booleano
    Reconhecedor
    Devolve True se o seu argumento é um TAD animal.
    """
    if type(arg) != dict or len(arg) != 5:
        return False

    if ('especie' and 'f_reproducao' and 'f_alimentacao' and 'idade' and 'fome') not in arg:
        return False

    if type(arg['especie']) != str or len(arg['especie']) == 0 or type(arg['f_reproducao']) != int:
        return False

    if type(arg['idade']) != int or type(arg['f_alimentacao']) != int or type(arg['fome']) != int:
        return False

    if arg['idade'] < 0 or arg['fome'] < 0 or arg['f_reproducao'] <= 0 or arg['f_alimentacao'] < 0:
        return False

    return True


def eh_predador(arg):
    """
    eh_predador: universal → booleano
    Reconhecedor
    Devolve True se o seu argumento é um TAD animal do tipo predador.
    """
    return eh_animal(arg) and arg['f_alimentacao'] > 0  # predador tem freq alimentacao positiva


def eh_presa(arg):
    """
    eh_presa: universal → booleano
    Reconhecedor
    Devolve True se o seu argumento é um TAD animal do tipo presa.
    """
    return eh_animal(arg) and arg['f_alimentacao'] == 0 and arg['fome'] == 0  # predador tem freq alimentacao positiva


def animais_iguais(animal_1, animal_2):
    """
    animais_iguais: animal × animal → booleano
    Teste
    Devolve True se a1 e a2 sao animais e iguais.
    """
    return eh_animal(animal_1) and eh_animal(animal_2) and animal_1 == animal_2


def animal_para_char(animal):
    """
    animal_para_char: animal → str
    Transformador
    Devolve a cad. de caracteres do primeiro caracter da especie do animal, em maiuscula para predadores e minuscula
    para presas.
    """
    return obter_especie(animal)[0].upper() if eh_predador(animal) else obter_especie(animal)[0].lower()


def animal_para_str(animal):
    """
    animal_para_str: animal → str
    Transformador
    Devolve a cadeia de caracteres que representa o animal da forma especie[idade/freq. reprod.;fome/freq. aliment.]
    """
    if eh_predador(animal):
        return obter_especie(animal) + ' [' + str(obter_idade(animal)) + '/' + str(obter_freq_reproducao(animal))\
               + ';' + str(obter_fome(animal)) + '/' + str(obter_freq_alimentacao(animal)) + ']'

    else:
        return obter_especie(animal) + ' [' + str(obter_idade(animal)) + '/' + str(obter_freq_reproducao(animal)) + ']'


def eh_animal_fertil(animal):
    """
    eh_animal_fertil: animal → booleano
    Devolve True se o animal atingiu a idade de reproducao.
    """
    return obter_idade(animal) == obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    """
    eh_animal_faminto: animal → booleano
    Devolve True se o animal eh predador e atingiu um valor de fome igual ou superior ah freq. de alimentacao.
    """
    return eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal)


def reproduz_animal(animal):
    """
    reproduz_animal: animal → animal
    Devolve um novo animal da mesma especie de a, com idade e fome igual a 0, e alterando (destrutivamente) a idade
    do animal a para 0.
    """
    return reset_fome(cria_copia_animal(reset_idade(animal)))


def cria_prado(pos_limite, rochedos, animais, pos_animais):
    """
    cria_prado: posicao × tuplo × tuplo × tuplo → prado
    Construtor
    Apos valida-lo, devolve o prado com a posicao limite, rochedos, animais e respetivas posicoes no argumento.
    """
    prado = {'limite': pos_limite, 'rochedos': rochedos, 'animais': list(animais), 'pos_animais': list(pos_animais)}

    if not eh_prado(prado):
        raise ValueError('cria_prado: argumentos invalidos')

    return prado


def cria_copia_prado(prado):
    """
    cria_copia_prado: prado → prado
    Construtor
    Devolve uma nova copia do prado.
    """
    if not eh_prado(prado):
        raise ValueError('cria_copia_prado: argumentos invalidos')

    rochedos = ()
    for rochedo in prado['rochedos']:
        rochedos += (cria_copia_posicao(rochedo),)

    animais = []
    for animal in prado['animais']:
        animais += [cria_copia_animal(animal)]

    pos_animais = []
    for pos in prado['pos_animais']:
        pos_animais += [cria_copia_posicao(pos)]

    return {
        'limite': cria_copia_posicao(prado['limite']),
        'rochedos': rochedos,
        'animais': animais,
        'pos_animais': pos_animais
    }


def obter_tamanho_x(prado):
    """
    obter_tamanho_x: prado → int
    Seletor
    Devolve o valor inteiro que corresponde ah dimensao Nx do prado.
    """
    return obter_pos_x(prado['limite']) + 1


def obter_tamanho_y(prado):
    """
    obter_tamanho_y: prado → int
    Seletor
    Devolve o valor inteiro que corresponde ah dimensao Ny do prado.
    """
    return obter_pos_y(prado['limite']) + 1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado → int
    Seletor
    Devolve o numero de animais predadores no prado.
    """
    return len(list(filter(eh_predador, prado['animais'])))


def obter_numero_presas(prado):
    """
    obter_numero_presas: prado → int
    Seletor
    Devolve o numero de presas no prado.
    """
    return len(list(filter(eh_presa, prado['animais'])))


def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado → tuplo posicoes
    Seletor
    Devolve um tuplo com as posicoes do prado ocupadas por animais, por ordem de leitura do prado.
    """
    return ordenar_posicoes(tuple(prado['pos_animais']))


def obter_animal(prado, posicao):
    """
    obter_animal: prado × posicao → animal
    Seletor
    Devolve o animal do prado que se encontra na posicao p.
    """
    numero_animais = len(prado['pos_animais'])
    for i in range(numero_animais):
        if posicoes_iguais(prado['pos_animais'][i], posicao):
            return prado['animais'][i]      # animais e posicoes correspondentes estao na mesma ordem


def eliminar_animal(prado, posicao):
    """
    eliminar_animal: prado × posicao → prado
    Modificador (destrutivo)
    Devolve o prado apos eliminar o animal da posicao p, deixando-a livre.
    """
    numero_animais = len(prado['pos_animais'])

    for i in range(numero_animais):
        if posicoes_iguais(prado['pos_animais'][i], posicao):

            prado['animais'].pop(i)
            prado['pos_animais'].pop(i)
            break

    return prado


def mover_animal(prado, posicao_1, posicao_2):
    """
    mover_animal: prado × posicao × posicao → prado
    Modificador (destrutivo)
    Devolve o prado apos movimentar o animal da posicao p1 para p2, libertando a posicao onde se encontrava.
    """
    numero_animais = len(prado['pos_animais'])

    for i in range(numero_animais):
        if posicoes_iguais(prado['pos_animais'][i], posicao_1):
            prado['pos_animais'][i] = posicao_2

    return prado


def inserir_animal(prado, animal, posicao):
    """
    inserir_animal: prado × animal × posicao → prado
    Modificador (destrutivo)
    Devolve o prado apos acrescentar, na posicao p do prado, o animal a.
    """
    prado['animais'] += [animal]
    prado['pos_animais'] += [posicao]
    return prado


def eh_prado(arg):
    """
    eh_prado: universal → booleano
    Reconhecedor
    Devolve True se o argumento é um TAD prado.
    """
    if type(arg) != dict and len(arg) != 4 and (('limite' and 'rochedos' and 'animais' and 'pos_animais') not in arg):
        return False

    if not eh_posicao(arg['limite']) or type(arg['rochedos']) != tuple or type(arg['animais']) != list:
        return False

    if len(arg['animais']) < 1 or type(arg['pos_animais']) != list or len(arg['pos_animais']) != len(arg['animais']):
        return False

    for rochedo in arg['rochedos']:         # se o rochedo nao esta dentro dos limites do prado
        if not eh_posicao(rochedo) or not (0 < obter_pos_x(rochedo) < obter_pos_x(arg['limite'])) or \
                not (0 < obter_pos_y(rochedo) < obter_pos_y(arg['limite'])):
            return False

    for ind_rochedo in range(len(arg['rochedos'])):       # se a mesma pos tiver rochedo e animal
        for ind_pos_animal in range(len(arg['pos_animais'])):
            if posicoes_iguais(arg['rochedos'][ind_rochedo], arg['pos_animais'][ind_pos_animal]):
                return False

    for animal in arg['animais']:
        if not eh_animal(animal):      # se nao for animal
            return False

    for pos_animal in arg['pos_animais']:           # se o animal nao esta dentro dos limites do prado
        if not eh_posicao(pos_animal) or not (0 < obter_pos_x(pos_animal) < obter_pos_x(arg['limite'])) or \
                not (0 < obter_pos_y(pos_animal) < obter_pos_y(arg['limite'])):
            return False

    for i in range(len(arg['pos_animais']) - 1):
        for e in range(i + 1, len(arg['pos_animais'])):
            if posicoes_iguais(arg['pos_animais'][i], arg['pos_animais'][e]):  # se ha 2 ou + animais na mesma posicao
                return False

    return True


def eh_posicao_animal(prado, posicao):
    """
    eh_posicao_animal: prado × posicao → booleano
    Reconhecedor
    Devolve True apenas se a posicao p do prado esta ocupada por um animal.
    """
    n_animais = len(prado['pos_animais'])

    for i in range(n_animais):
        if posicoes_iguais(prado['pos_animais'][i], posicao):
            return True

    return False


def eh_posicao_obstaculo(prado, posicao):
    """
    eh_posicao_obstaculo: prado × posicao → booleano
    Reconhecedor
    Devolve True se a posicao p corresponde a uma montanha ou rochedo.
    """
    if obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == obter_pos_x(prado['limite']):
        return True                           # se posicao eh uma montanha

    if obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == obter_pos_y(prado['limite']):
        return True                           # se posicao eh uma montanha

    for ind_rochedo in range(len(prado['rochedos'])):
        if posicoes_iguais(posicao, prado['rochedos'][ind_rochedo]):  # se posicao eh um rochedo
            return True

    return False


def eh_posicao_livre(prado, posicao):
    """
    eh_posicao_obstaculo: prado × posicao → booleano
    Reconhecedor
    Devolve True se a posicao p corresponde a um espaco livre (sem animais ou obstaculos).
    """
    return not eh_posicao_obstaculo(prado, posicao) and not eh_posicao_animal(prado, posicao)


def prados_iguais(prado1, prado2):
    """
    prados_iguais: prado × prado → booleano
    Teste
    Devolve True se p1 e p2 sao prados e iguais.
    """
    if not eh_prado(prado1) or not eh_prado(prado2):
        return False

    if not posicoes_iguais(prado1['limite'], prado2['limite']):     # posicoes limite sao iguais
        return False

    rochedos_prado1 = ordenar_posicoes(prado1['rochedos'])
    rochedos_prado2 = ordenar_posicoes(prado2['rochedos'])

    if len(rochedos_prado1) != len(rochedos_prado2) or len(prado1['animais']) != len(prado2['animais']):
        return False

    for i in range(len(rochedos_prado1)):               # rochedos na mesma posicao
        if not posicoes_iguais(rochedos_prado1[i], rochedos_prado2[i]):
            return False

    pos_animais_prado1 = obter_posicao_animais(prado1)   # ja ordenados segundo a  leitura do prado
    pos_animais_prado2 = obter_posicao_animais(prado2)

    if len(pos_animais_prado1) != len(pos_animais_prado2):
        return False

    for i in range(len(pos_animais_prado1)):
        pos_prado_1 = pos_animais_prado1[i]
        pos_prado_2 = pos_animais_prado2[i]

        if not posicoes_iguais(pos_prado_1, pos_prado_2):
            return False

        if not animais_iguais(obter_animal(prado1, pos_prado_1), obter_animal(prado2, pos_prado_2)):
            return False

    return True


def prado_para_str(prado):
    """
    prado_para_str: prado → str
    Transformador
    Devolve uma cad. de caracteres que representa o prado.
    """
    Nx = obter_tamanho_x(prado) - 1     # numero de colunas exceto a coluna 0
    Ny = obter_tamanho_y(prado) - 1     # numero de linhas exceto a linha 0
    l = ()

    for y in range(1, Ny):              # so percorre as linhas entre a primeira e a ultima
        l += ('|',)               # representacao da coluna 0

        for x in range(1, Nx):              # so percorre as colunas entre a primeira e a ultima
            p = cria_posicao(x, y)

            if eh_posicao_animal(prado, p):
                a = obter_animal(prado, p)

                if eh_presa(a):
                    l += (animal_para_char(a),)  # letra minuscula

                else:
                    l += (animal_para_char(a),)  # letra maiuscula

            elif eh_posicao_obstaculo(prado, p):
                l += ('@',)

            else:  # posicoes livres
                l += ('.',)

        l += ('|\n',)           # representacao da ultima coluna

    return '+' + '-' * (Nx - 1) + '+\n' + ''.join(l) + '+' + '-' * (Nx - 1) + '+'


def obter_valor_numerico(prado, posicao):
    """
    obter_valor_numerico: prado × posicao → int
    Devolve o valor numerico da posicao p correspondente ah ordem de leitura no prado m.
    """
    return obter_tamanho_x(prado) * obter_pos_y(posicao) + obter_pos_x(posicao)


def obter_movimento(prado, posicao):
    """
    obter_movimento: prado × posicao → posicao
    Devolve a posicao seguinte do animal na posicao p no prado m, segundo as regras de movimento dos animais.
    """
    # lista de pos adjacentes livres e sem montanhas
    pos_adjacentes = list(filter(lambda pos: (0 < obter_pos_x(pos) < obter_tamanho_x(prado) - 1 and
                            0 < obter_pos_y(pos) < obter_tamanho_y(prado) - 1), obter_posicoes_adjacentes(posicao)))

    if eh_predador(obter_animal(prado, posicao)):
        pos_presas = []

        for pos in pos_adjacentes:
            if eh_posicao_animal(prado, pos) and eh_presa(obter_animal(prado, pos)):
                pos_presas += [pos]  # o predador come as presas, ocupando as suas posicoes

        if pos_presas:
            return pos_presas[obter_valor_numerico(prado, posicao) % len(pos_presas)]

    pos_livres = list(filter(lambda x: eh_posicao_livre(prado, x), pos_adjacentes))
    if pos_livres:
        return pos_livres[obter_valor_numerico(prado, posicao) % len(pos_livres)]  # resto de valor de pos atual//num pos livres

    return posicao      # quando nao ha posicoes livres, nao se move


def geracao(prado):
    """
    geracao: prado → prado
    Funcao auxiliar que devolve o prado m, modificado de acordo com a evolucao correspondente a uma geracao completa.
    """
    pred_q_comeram_frente = []


    for pos_a in obter_posicao_animais(prado):
        continua = True
        for pred_q_comeu_frente in pred_q_comeram_frente:
            if posicoes_iguais(pos_a, pred_q_comeu_frente):
                continua = False

        if continua:
            a = obter_animal(prado, pos_a)

            if eh_predador(a):  # a fome so aumenta nos predadores
                aumenta_fome(a)
            if not eh_animal_fertil(a):  # qd eh fertil, a idade so voltará a aumentar apos reproduzir-se
                aumenta_idade(a)

            pos_f = obter_movimento(prado, pos_a)
            if pos_f != pos_a:  # move se quando as pos sao !=

                if eh_predador(a) and eh_posicao_animal(prado, pos_f):  # quando o predador come a presa e ocupa a sua pos
                    eliminar_animal(prado, pos_f)  # a presa morre
                    reset_fome(a)  # a fome passa a 0

                    if posicoes_iguais(ordenar_posicoes((pos_a, pos_f))[1], pos_f):
                        pred_q_comeram_frente += [pos_f]

                mover_animal(prado, pos_a, pos_f)

                if eh_animal_fertil(a):  # so se reproduz qd se moveu e eh fertil
                    inserir_animal(prado, reproduz_animal(a), pos_a)  # o animal-filho ocupa a pos anterior do pai

            if eh_animal_faminto(a):
                eliminar_animal(prado, pos_f)  # morre ah fome

    return prado


def simula_ecossistema(ficheiro, num_geracoes, modo):
    """
    simula_ecossistema: str x int x booleano → tuplo
    Funcao que escreve o prado, o numero de presas e predadores dependendo do modo,
    e devolve um tuplo com o numero de predadores e presas no prado, no fim da simulacao.
    """
    def tuplo_para_posicao(tuplo):
        """
        str_para_posicao: tuplo -> posicao
        Funcao auxiliar que devolve a posicao correspondente ao tuplo dado.
        """
        return cria_posicao(tuplo[0], tuplo[1])


    def escreve_geracao(prado, geracao):
        """
        escreve_geracao: prado x int -> str
        Funcao auxiliar que escreve o prado pela saida standard, o numero de presas e predadores, e o numero da geracao.
        """
        return f'Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} \
(Gen. {geracao})\n' + prado_para_str(prado)


    with open(ficheiro, 'r') as fich_config:
        linha1 = eval(fich_config.readline())  # tira \n da linha
        limite = tuplo_para_posicao(linha1)

        linha2 = eval(fich_config.readline())
        rochedos = ()
        for rochedo_em_str in linha2:
            rochedos += (tuplo_para_posicao(rochedo_em_str),)   # tuplo com posicoes dos rochedos

        linhas_animais = fich_config.readlines()
        animais = ()
        pos_animais = ()

        for linha_animal in linhas_animais:
            animais += (cria_animal(eval(linha_animal)[0], eval(linha_animal)[1], eval(linha_animal)[2]),)
            pos_animais += (tuplo_para_posicao(eval(linha_animal)[3]),)
                                                                    # tuplo com animais e tuplo com suas posicoes
    prado = cria_prado(limite, rochedos, animais, pos_animais)
    print(escreve_geracao(prado, 0))

    if modo:    # modo verboso
        for num_da_geracao in range(1, num_geracoes + 1):

            n_predadores_inicio = obter_numero_predadores(prado)
            n_presas_inicio = obter_numero_presas(prado)

            prado = geracao(prado)      # avanca 1 geracao

            n_predadores_fim = obter_numero_predadores(prado)
            n_presas_fim = obter_numero_presas(prado)

            if n_predadores_inicio != n_predadores_fim or n_presas_inicio != n_presas_fim:
                print(escreve_geracao(prado, num_da_geracao))

    else:      # modo quiet

        for num_da_geracao in range(1, num_geracoes + 1):   # avanca todas as geracoes sem as escrever
            prado = geracao(prado)

        print(escreve_geracao(prado, num_geracoes))

    return obter_numero_predadores(prado), obter_numero_presas(prado)       # tuplo com num de predadores e presas


print(simula_ecossistema('opop.txt', 100, True))

