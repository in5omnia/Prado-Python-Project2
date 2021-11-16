def cria_posicao(x, y):  # usando listas
    """
    cria_posicao: int × int → posicao
    Construtor
    Cria uma posicao com as coordenadas dadas.
    """
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return [x, y]


def cria_copia_posicao(p):
    """
    cria_copia_posicao: posicao → posicao
    Construtor
    Cria uma copia nova da posicao.
    """
    if not eh_posicao(p):
        raise ValueError('cria_copia_posicao: argumentos invalidos')
    return p[:]  # OU cria_posicao(p[0], p[1])


def obter_pos_x(p):
    """
    obter_pos_x: posicao → int
    Seletor
    Devolve a componente x da posicao p.
    """
    return p[0]


def obter_pos_y(p):
    """
    obter_pos_y: posicao → int
    Seletor
    Devolve a componente y da posicao p.
    """
    return p[1]


def eh_posicao(arg):
    """
    eh_posicao: universal → booleano
    Reconhecedor
    Devolve True se arg eh uma posicao.
    """
    return type(arg) == list and len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int and arg[0] >= 0 and \
           arg[1] >= 0


def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao × posicao → booleano
    Teste
    Devolve True se as posicoes p1 e p2 sao posicoes e iguais.
    """
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == \
           obter_pos_y(p2)


def posicao_para_str(p):
    """
    posicao_para_str: posicao → str
    Transformador
    Escreve a cadeia de carateres que representa a posicao p.
    """
    return str(tuple(p))


def obter_posicoes_adjacentes(p):  # SHOULD I CHECK IF ALL THE POSITIONS EXIST? CUZ (0,0) DOESNT HAVE 1 LEFT OR ABOVE
    """
    obter_posicoes_adjacentes: posicao → tuplo
    Devolve um tuplo com as posicoes adjacentes a p, ordenadas segundo o sentido horario.
    """
    if p == [0, 0]:
        return cria_posicao(1, 0), cria_posicao(0, 1)
    x = obter_pos_x(p)
    y = obter_pos_y(p)
    if x == 0:  # nao tem posicoes ah esquerda
        return cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1)
    if y == 0:  # nao tem posicoes acima
        return cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y)
    return cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y)


def ordenar_posicoes(t):
    """
    ordenar_posicoes: tuplo → tuplo
    Devolve um tuplo com as mesmas posicoes do argumento, ordenadas segundo a ordem de leitura do prado.
    """
    lst_p = []
    for p in t:
        lst_p += [(obter_pos_y(p), obter_pos_x(p))]  # eh lido de baixo para cima, do y menor para o maior, e
    lst_p = sorted(lst_p)  # na mesma linha, le primeiro o menor x
    for i in range(len(lst_p)):
        lst_p[i] = cria_posicao(lst_p[i][1], lst_p[i][0])  # substituir as coordenadas pelas posicoes

    return tuple(lst_p)


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


def cria_copia_animal(a):
    """
    cria_copia_animal: animal → animal
    Construtor
    Devolve uma nova copia do animal.
    """
    if not eh_animal(a):
        raise ValueError('cria_copia_animal: argumentos invalidos')
    return a.copy()


def obter_especie(a):
    """
    obter especie: animal → str
    Seletor
    Devolve a especie do animal a.
    """
    return a['especie']


def obter_freq_reproducao(a):
    """
    obter_freq_reproducao: animal → int
    Seletor
    Devolve a frequencia de reproducao do animal a.
    """
    return a['f_reproducao']


def obter_freq_alimentacao(a):
    """
    obter_freq_alimentacao: animal → int
    Seletor
    Devolve a frequencia de alimentacao do animal a (sempre 0 nas presas).
    """
    return a['f_alimentacao']


def obter_idade(a):
    """
    obter_idade: animal → int
    Seletor
    Devolve a idade do animal a.
    """
    return a['idade']


def obter_fome(a):
    """
    obter_fome: animal → int
    Seletor
    Devolve a fome do animal a (sempre 0 nas presas).
    """
    return a['fome']


def aumenta_idade(a):
    """
    aumenta_idade: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos aumentar a sua idade em 1 unidade.
    """
    a['idade'] += 1
    return a


def reset_idade(a):
    """
    reset_idade: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos redefinir a sua idade como 0.
    """
    a['idade'] = 0
    return a


def aumenta_fome(a):
    """
    aumenta_fome: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos aumentar a sua fome em 1 unidade, se este for predador.
    """
    if eh_predador(a):
        a['fome'] += 1
    return a


def reset_fome(a):
    """
    reset_fome: animal → animal
    Modificador (destrutivo)
    Devolve o animal apos redefinir a sua fome como 0, se este for predador.
    """
    if eh_predador(a):
        a['fome'] = 0
    return a


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


def animais_iguais(a1, a2):
    """
    animais_iguais: animal × animal → booleano
    Teste
    Devolve True se a1 e a2 sao animais e iguais.
    """
    return eh_animal(a1) and eh_animal(a2) and a1 == a2


def animal_para_char(a):
    """
    animal_para_char: animal → str
    Transformador
    Devolve a cad. de caracteres do primeiro caracter da especie do animal, em maiuscula para predadores e minuscula
    para presas.
    """
    return obter_especie(a)[0].upper() if eh_predador(a) else obter_especie(a)[0].lower()


def animal_para_str(a):
    """
    animal_para_str: animal → str
    Transformador
    Devolve a cadeia de caracteres que representa o animal da forma especie[idade/freq. reprod.;fome/freq. aliment.]
    """
    if eh_predador(a):
        return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ';' + \
               str(obter_fome(a)) + '/' + str(obter_freq_alimentacao(a)) + ']'
    else:
        return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ']'


def eh_animal_fertil(a):
    """
    eh_animal_fertil: animal → booleano
    Devolve True se o animal atingiu a idade de reproducao.
    """
    return obter_idade(a) == obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """
    eh_animal_faminto: animal → booleano
    Devolve True se o animal eh predador e atingiu um valor de fome igual ou superior ah freq. de alimentacao.
    """
    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """
    reproduz_animal: animal → animal
    Devolve um novo animal da mesma especie de a, com idade e fome igual a 0, e alterando (destrutivamente) a idade
    do animal a para 0.
    """
    return reset_fome(cria_copia_animal(reset_idade(a)))


def cria_prado(d, r, a, p):
    prado = {'mapa': d, 'rochedos': r, 'animais': list(a), 'pos_animais': list(p)}
    if not eh_prado(prado):
        raise ValueError('cria_prado: argumentos invalidos')
    return prado  # animais e suas posicoes em listas


def cria_copia_prado(m):
    """
    cria_copia_prado: prado → prado
    Construtor
    Devolve uma nova copia do prado.
    """
    if not eh_prado(m):
        raise ValueError('cria_copia_prado: argumentos invalidos')
    rochedos = ()
    for rochedo in m['rochedos']:
        rochedos += (cria_copia_posicao(rochedo),)
    animais = []
    for animal in m['animais']:
        animais += [cria_copia_animal(animal)]
    pos_animais = []
    for pos in m['pos_animais']:
        pos_animais += [cria_copia_posicao(pos)]

    return {
        'mapa': cria_copia_posicao(m['mapa']),
        'rochedos': rochedos,
        'animais': animais,
        'pos_animais': pos_animais
    }


def obter_tamanho_x(m):
    """
    obter_tamanho_x: prado → int
    Seletor
    Devolve o valor inteiro que corresponde ah dimensao Nx do prado.
    """
    return obter_pos_x(m['mapa']) + 1


def obter_tamanho_y(m):
    """
    obter_tamanho_y: prado → int
    Seletor
    Devolve o valor inteiro que corresponde ah dimensao Ny do prado.
    """
    return obter_pos_y(m['mapa']) + 1


def obter_numero_predadores(m):
    """
    obter_numero_predadores: prado → int
    Seletor
    Devolve o numero de animais predadores no prado.
    """
    return len(list(filter(eh_predador, m['animais'])))


def obter_numero_presas(m):
    """
    obter_numero_presas: prado → int
    Seletor
    Devolve o numero de presas no prado.
    """
    return len(list(filter(eh_presa, m['animais'])))


def obter_posicao_animais(m):
    """
    obter_posicao_animais: prado → tuplo posicoes
    Seletor
    Devolve um tuplo com as posicoes do prado ocupadas por animais, por ordem de leitura do prado.
    """
    return ordenar_posicoes(tuple(m['pos_animais']))


def obter_animal(m, p):
    """
    obter_animal: prado × posicao → animal
    Seletor
    Devolve o animal do prado que se encontra na posicao p.
    """
    n_animais = len(m['pos_animais'])
    for i in range(n_animais):
        if posicoes_iguais(m['pos_animais'][i], p):
            return m['animais'][i]  # animais e posicoes correspondentes estao na mesma ordem


def eliminar_animal(m, p):
    """
    eliminar_animal: prado × posicao → prado
    Modificador (destrutivo)
    Devolve o prado apos eliminar o animal da posicao p, deixando-a livre.
    """
    n_animais = len(m['pos_animais'])
    for i in range(n_animais):
        if posicoes_iguais(m['pos_animais'][i], p):
            m['animais'].pop(i)
            m['pos_animais'].pop(i)
            break
    return m


def mover_animal(m, p1, p2):
    """
    mover_animal: prado × posicao × posicao → prado
    Modificador (destrutivo)
    Devolve o prado apos movimentar o animal da posicao p1 para p2, libertando a posicao onde se encontrava.
    """
    n_animais = len(m['pos_animais'])
    for i in range(n_animais):
        if posicoes_iguais(m['pos_animais'][i], p1):
            m['pos_animais'][i] = p2
    return m


def inserir_animal(m, a, p):
    """
    inserir_animal: prado × animal × posicao → prado
    Modificador (destrutivo)
    Devolve o prado apos acrescentar, na posicao p do prado, o animal a.
    """
    m['animais'] += [a]
    m['pos_animais'] += [p]
    return m


def eh_prado(arg):
    """
    eh_prado: universal → booleano
    Reconhecedor
    Devolve True se o argumento é um TAD prado.
    """
    if type(arg) != dict and len(arg) != 4 and (('mapa' and 'rochedos' and 'animais' and 'pos_animais') not in arg):
        return False
    if not eh_posicao(arg['mapa']) or type(arg['rochedos']) != tuple or type(arg['animais']) != list or \
            len(arg['animais']) < 1 or type(arg['pos_animais']) != list or \
            len(arg['pos_animais']) != len(arg['animais']):
        return False
    for rochedo in arg['rochedos']:
        if not eh_posicao(rochedo) or not (0 < obter_pos_x(rochedo) < obter_pos_x(arg['mapa'])) or \
                not (0 < obter_pos_y(rochedo) < obter_pos_y(arg['mapa'])):
            return False
    for ind_r in range(len(arg['rochedos'])):  # se a mesma pos tiver rochedo e animal
        for ind_pos_a in range(len(arg['pos_animais'])):
            if posicoes_iguais(arg['rochedos'][ind_r], arg['pos_animais'][ind_pos_a]):
                return False
    for animal in arg['animais']:
        if not eh_animal(animal):
            return False
    for pos in arg['pos_animais']:
        if not eh_posicao(pos) or not (0 < obter_pos_x(pos) < obter_pos_x(arg['mapa'])) or \
                not (0 < obter_pos_y(pos) < obter_pos_y(arg['mapa'])):
            return False
    for i in range(len(arg['pos_animais']) - 1):
        for e in range(i + 1, len(arg['pos_animais'])):
            if posicoes_iguais(arg['pos_animais'][i],
                               arg['pos_animais'][e]):  # se houverem 2 ou + animais na mesma posicao
                return False
    return True


def eh_posicao_animal(m, p):
    """
    eh_posicao_animal: prado × posicao → booleano
    Reconhecedor
    Devolve True apenas se a posicao p do prado esta ocupada por um animal.
    """
    n_animais = len(m['pos_animais'])
    for i in range(n_animais):
        if posicoes_iguais(m['pos_animais'][i], p):
            return True
    return False


def eh_posicao_obstaculo(m, p):
    """
    eh_posicao_obstaculo: prado × posicao → booleano
    Reconhecedor
    Devolve True se a posicao p corresponde a uma montanha ou rochedo.
    """
    if obter_pos_x(p) == 0 or obter_pos_y(p) == 0 or obter_pos_x(p) == obter_pos_x(m['mapa']) or \
            obter_pos_y(p) == obter_pos_y(m['mapa']):  # p eh a pos de uma montanha
        return True
    for ind_r in range(len(m['rochedos'])):
        if posicoes_iguais(p, m['rochedos'][ind_r]):  # p eh a pos de um rochedo
            return True
    return False


def eh_posicao_livre(m, p):
    """
    eh_posicao_obstaculo: prado × posicao → booleano
    Reconhecedor
    Devolve True se a posicao p corresponde a um espaco livre (sem animais ou obstaculos).
    """
    return not eh_posicao_obstaculo(m, p) and not eh_posicao_animal(m, p)


def prados_iguais(p1, p2):
    """
    prados_iguais: prado × prado → booleano
    Teste
    Devolve True se p1 e p2 sao prados e iguais.
    """
    return eh_prado(p1) and eh_prado(p2) and p1 == p2


def prado_para_str(m):
    """
    prado_para_str: prado → str
    Transformador
    Devolve uma cad. de caracteres que representa o prado.
    """
    Nx = obter_tamanho_x(m) - 1
    Ny = obter_tamanho_y(m) - 1
    l = ()
    for y in range(1, Ny):
        l += ('|',)
        for x in range(1, Nx):
            p = cria_posicao(x, y)
            if eh_posicao_animal(m, p):
                a = obter_animal(m, p)
                if eh_presa(a):
                    l += (animal_para_char(a),)  # letra minuscula
                else:
                    l += (animal_para_char(a),)  # letra maiuscula
            elif eh_posicao_obstaculo(m, p):
                l += ('@',)
            else:  # posicoes livres
                l += ('.',)
        l += ('|\n',)
    return '+' + '-' * (Nx - 1) + '+\n' + ''.join(l) + '+' + '-' * (Nx - 1) + '+'


def obter_valor_numerico(m, p):
    """
    obter_valor_numerico: prado × posicao → int
    Devolve o valor numerico da posicao p correspondente ah ordem de leitura no prado m.
    """
    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)


def obter_movimento(m, p):
    """
    obter_movimento: prado × posicao → posicao
    Devolve a posicao seguinte do animal na posicao p no prado m, segundo as regras de movimento dos animais.
    """  # lista de pos adjacentes livres e sem montanhas
    pos_adj = list(filter(lambda pos: (0 < obter_pos_x(pos) < obter_tamanho_x(m) - 1 and 0 < obter_pos_y(pos) <
                                       obter_tamanho_y(m) - 1), obter_posicoes_adjacentes(p)))
    if eh_predador(obter_animal(m, p)):
        pos_presas = []
        for pos in pos_adj:
            if eh_posicao_animal(m, pos) and eh_presa(obter_animal(m, pos)):
                pos_presas += [pos]  # o predador come as presas, ocupando as suas pos
        if pos_presas:
            return pos_presas[obter_valor_numerico(m, p) % len(pos_presas)]  # ponho um ELSE?
    pos_livres = list(filter(lambda x: eh_posicao_livre(m, x), pos_adj))
    if pos_livres:
        return pos_livres[obter_valor_numerico(m, p) % len(pos_livres)]  # resto de valor de pos atual//num pos livres
    return p  # quando nao ha posicoes livres, nao se move


# VERIFICAR SE POSSO CONSIDERAR Q O ANIMAL N MOVE EM OBTER MOVS


def geracao(m):
    """
    geracao: prado → prado
    Funcao auxiliar que devolve o prado m, modificado de acordo com a evolucao correspondente a uma geracao completa.
    """
    for pos_a in obter_posicao_animais(m):
        a = obter_animal(m, pos_a)
        if eh_predador(a):  # a fome so aumenta nos predadores
            aumenta_fome(a)
        if not eh_animal_fertil(a):  # qd eh fertil, a idade so voltará a aumentar apos reproduzir-se
            aumenta_idade(a)

        pos_f = obter_movimento(m, pos_a)
        if pos_f != pos_a:  # move se quando as pos sao !=
            if eh_predador(a) and eh_posicao_animal(m, pos_f):  # quando o predador come a presa e ocupa a sua pos
                eliminar_animal(m, pos_f)  # a presa morre
                reset_fome(a)  # a fome passa a 0

            mover_animal(m, pos_a, pos_f)
            if eh_animal_fertil(a):  # so se reproduz qd se moveu e eh fertil
                inserir_animal(m, reproduz_animal(a), pos_a)  # o animal-filho ocupa a pos anterior do pai
        if eh_animal_faminto(a):
            eliminar_animal(m, pos_f)  # morre ah fome
    return m


def simula_ecossistema(f, g, v):
    """
    simula_ecossistema: str x int x booleano → tuplo
    Funcao que escreve o prado, o numero de presas devolve um tuplo com o numero de predadores e presas no prado no fim da simulacao.
    """
    def tuplo_para_posicao(tuplo):
        """
        str_para_posicao: tuplo -> posicao
        Funcao auxiliar que devolve a posicao correspondente ao tuplo.
        """
        return cria_posicao(tuplo[0], tuplo[1])

    def escreve_geracao(prado, geracao):
        """
        escreve_geracao: prado x int -> str
        Funcao auxiliar que escreve o prado pela saida standard, o numero de presas e predadores, e o numero da geracao.
        """
        return f'Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} \
(Gen. {geracao})\n' + prado_para_str(prado)

    with open(f, 'r') as fich_config:
        linha1 = eval(fich_config.readline())  # tira \n da linha
        limite = tuplo_para_posicao(linha1)

        linha2 = eval(fich_config.readline())
        rochedos = ()
        for rochedo_em_str in linha2:
            rochedos += (tuplo_para_posicao(rochedo_em_str),)

        linhas_animais = fich_config.readlines()
        animais = ()
        pos_animais = ()
        for linha_animal in linhas_animais:
            animais += (cria_animal(eval(linha_animal)[0], eval(linha_animal)[1], eval(linha_animal)[2]),)
            pos_animais += (tuplo_para_posicao(eval(linha_animal)[3]),)

    prado = cria_prado(limite, rochedos, animais, pos_animais)
    print(escreve_geracao(prado, 0))

    if v:
        for n_geracao in range(1, g + 1):
            n_predadores_inicio = obter_numero_predadores(prado)
            n_presas_inicio = obter_numero_presas(prado)

            prado = geracao(prado)

            n_predadores_fim = obter_numero_predadores(prado)
            n_presas_fim = obter_numero_presas(prado)

            if n_predadores_inicio != n_predadores_fim or n_presas_inicio != n_presas_fim:
                print(escreve_geracao(prado, n_geracao))
    else:
        for n_geracao in range(1, g + 1):
            prado = geracao(prado)
        print(escreve_geracao(prado, g))

    return obter_numero_predadores(prado), obter_numero_presas(prado)


print(simula_ecossistema('opop.txt', 200, True))


