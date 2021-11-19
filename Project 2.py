# Beatriz Gavilan 102463
# 17/11/2021
# beatrizgavilan@tecnico.ulisboa.pt

# Fundamentos da Programação
# Projeto 2 - simular geracoes num prado com animais e obstaculos



    # TAD Posicao:

# Representação interna: lista

# Operacoes basicas:

# cria_posicao: int x int -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_x: posicao -> int
# obter_pos_y: posicao -> int
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str

# Funcoes de Alto Nivel:

# obter_posicoes_adjacentes: posicao -> tuplo
# ordenar_posicoes: tuplo -> tuplo
# Funcao auxiliar: posicoes_iguais_reduzida: posicao x posicao -> booleano


def cria_posicao(x, y):
    """
    cria_posicao: int x int -> posicao
    Construtor
    Cria uma posicao com as coordenadas dadas.
    """

    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')

    return [x, y]


def cria_copia_posicao(posicao):
    """
    cria_copia_posicao: posicao -> posicao
    Construtor
    Cria uma copia nova da posicao.
    """
    if not eh_posicao(posicao):
        raise ValueError('cria_copia_posicao: argumentos invalidos')
    return posicao[:]


def obter_pos_x(posicao):
    """
    obter_pos_x: posicao -> int
    Seletor
    Devolve a componente x da posicao.
    """
    return posicao[0]


def obter_pos_y(posicao):
    """
    obter_pos_y: posicao -> int
    Seletor
    Devolve a componente y da posicao.
    """
    return posicao[1]


def eh_posicao(arg):
    """
    eh_posicao: universal -> booleano
    Reconhecedor
    Devolve True se arg eh uma posicao.
    """
    return type(arg) == list and len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int and arg[0] >= 0 and \
           arg[1] >= 0


def posicoes_iguais(posicao1, posicao2):
    """
    posicoes_iguais: posicao x posicao -> booleano
    Teste
    Devolve True se a posicao1 e posicao2 sao posicoes e iguais.
    """
    return eh_posicao(posicao1) and eh_posicao(posicao2) and posicao1 == posicao2


def posicoes_iguais_reduzida(posicao1, posicao2):
    """
    posicoes_iguais_reduzida: posicao x posicao -> booleano
    Funcao auxiliar que devolve True se a posicao1 e posicao2 sao iguais, quando ja se sabe que sao posicoes,
    para maior eficiencia.
    """
    return obter_pos_x(posicao1) == obter_pos_x(posicao2) and obter_pos_y(posicao1) == obter_pos_y(posicao2)


def posicao_para_str(posicao):
    """
    posicao_para_str: posicao -> str
    Transformador
    Escreve a cadeia de carateres que representa a posicao.
    """
    return str(tuple(posicao))


def obter_posicoes_adjacentes(posicao):
    """
    obter_posicoes_adjacentes: posicao -> tuplo
    Devolve um tuplo com as posicoes adjacentes ah posicao dada, ordenadas segundo o sentido horario.
    """

    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)
    if x == 0:      # nao tem posicoes ah esquerda
        if y == 0:
            return cria_posicao(1, 0), cria_posicao(0, 1)
        return cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1)

    if y == 0:      # nao tem posicoes acima
        return cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y)

    return cria_posicao(x, y - 1), cria_posicao(x + 1, y), cria_posicao(x, y + 1), cria_posicao(x - 1, y)


def ordenar_posicoes(tuplo_posicoes):
    """
    ordenar_posicoes: tuplo -> tuplo
    Devolve um tuplo com as mesmas posicoes do argumento, ordenadas segundo a ordem de leitura do prado.
    """
    lista_posicoes = []

    for p in tuplo_posicoes:
        lista_posicoes += [(obter_pos_y(p), obter_pos_x(p), p)]  # eh lido de baixo para cima, do y menor para o maior,
    lista_posicoes = sorted(lista_posicoes)                                 # e, na mesma linha, le o menor x primeiro

    for i in range(len(lista_posicoes)):
        lista_posicoes[i] = lista_posicoes[i][2]   # substitui as coordenadas
                                                                                                # pelas posicoes
    return tuple(lista_posicoes)


        # TAD Animal:

# Representação interna: dicionário

# Operacoes basicas:

# cria_animal: str × int × int → animal
# cria_copia_animal: animal → animal
# obter_especie: animal → str
# obter_freq_reproducao: animal → int
# obter_freq_alimentacao: animal → int
# obter_idade: animal → int
# obter_fome: animal → int
# aumenta_idade: animal → animal
# reset_idade: animal → animal
# aumenta_fome: animal → animal
# reset_fome: animal → animal
# eh_animal: universal → booleano
# eh_predador: universal → booleano
# eh_presa: universal → booleano
# animais_iguais: animal × animal → booleano
# animal_para_char: animal → str
# animal_para_str: animal → str

# Funcoes de Alto Nivel:

# eh_animal_fertil: animal -> booleano
# eh_animal_faminto: animal -> booleano
# reproduz_animal: animal -> animal


def cria_animal(especie, f_reproducao, f_alimentacao):  # usando dicionarios
    """
    cria_animal: str x int x int -> animal
    Construtor
    Devolve o animal com a  especie, frequencia de reproducao e frequencia de alimentacao dadas.
    (Quando a frequencia de alimentacao eh 0, eh uma presa).
    """

    animal = {'especie': especie, 'f_reproducao': f_reproducao, 'f_alimentacao': f_alimentacao, 'idade': 0, 'fome': 0}

    if not eh_animal(animal):
        raise ValueError('cria_animal: argumentos invalidos')

    return animal


def cria_copia_animal(animal):
    """
    cria_copia_animal: animal -> animal
    Construtor
    Devolve uma nova copia do animal.
    """
    if not eh_animal(animal):
        raise ValueError('cria_copia_animal: argumentos invalidos')

    return animal.copy()


def obter_especie(animal):
    """
    obter especie: animal -> str
    Seletor
    Devolve a especie do animal.
    """
    return animal['especie']


def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal -> int
    Seletor
    Devolve a frequencia de reproducao do animal.
    """
    return animal['f_reproducao']


def obter_freq_alimentacao(animal):
    """
    obter_freq_alimentacao: animal -> int
    Seletor
    Devolve a frequencia de alimentacao do animal (sempre 0 nas presas).
    """
    return animal['f_alimentacao']


def obter_idade(animal):
    """
    obter_idade: animal -> int
    Seletor
    Devolve a idade do animal.
    """
    return animal['idade']


def obter_fome(animal):
    """
    obter_fome: animal -> int
    Seletor
    Devolve a fome do animal (sempre 0 nas presas).
    """
    return animal['fome']


def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal
    Modificador (destrutivo)
    Devolve o animal apos aumentar a sua idade em 1 unidade.
    """
    animal['idade'] += 1
    return animal


def reset_idade(animal):
    """
    reset_idade: animal -> animal
    Modificador (destrutivo)
    Devolve o animal apos redefinir a sua idade como 0.
    """
    animal['idade'] = 0
    return animal


def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal
    Modificador (destrutivo)
    Devolve o animal apos aumentar a sua fome em 1 unidade, se este for predador.
    """
    if eh_predador(animal):
        animal['fome'] += 1
    return animal


def reset_fome(animal):
    """
    reset_fome: animal -> animal
    Modificador (destrutivo)
    Devolve o animal apos redefinir a sua fome como 0, se este for predador.
    """
    if eh_predador(animal):
        animal['fome'] = 0
    return animal


def eh_animal(arg):
    """
    eh_animal: universal -> booleano
    Reconhecedor
    Devolve True se o seu argumento é um TAD animal.
    """
    if not isinstance(arg, dict) or len(arg) != 5:
        return False

    if 'especie' not in arg or 'f_reproducao' not in arg or 'f_alimentacao' not in arg or 'idade' not in arg or\
            'fome' not in arg:
        return False

    if not isinstance(arg['especie'], str) or len(arg['especie']) == 0 or not isinstance(arg['f_reproducao'], int):
        return False

    if not isinstance(arg['idade'], int) or not isinstance(arg['f_alimentacao'], int) or \
            not isinstance(arg['fome'], int):
        return False

    if arg['idade'] < 0 or arg['fome'] < 0 or arg['f_reproducao'] <= 0 or arg['f_alimentacao'] < 0:
        return False

    return True


def eh_predador(arg):
    """
    eh_predador: universal -> booleano
    Reconhecedor
    Devolve True se o seu argumento é um TAD animal do tipo predador.
    """
    return eh_animal(arg) and arg['f_alimentacao'] > 0  # predador tem freq alimentacao positiva


def eh_presa(arg):
    """
    eh_presa: universal -> booleano
    Reconhecedor
    Devolve True se o seu argumento é um TAD animal do tipo presa.
    """
    return eh_animal(arg) and arg['f_alimentacao'] == 0 and arg['fome'] == 0  # predador tem freq alimentacao positiva


def animais_iguais(animal_1, animal_2):
    """
    animais_iguais: animal x animal -> booleano
    Teste
    Devolve True se animal_1 e animal_2 sao animais e iguais.
    """
    return eh_animal(animal_1) and eh_animal(animal_2) and animal_1 == animal_2


def animal_para_char(animal):
    """
    animal_para_char: animal -> str
    Transformador
    Devolve a cad. de caracteres do primeiro caracter da especie do animal, em maiuscula para predadores e minuscula
    para presas.
    """
    return obter_especie(animal)[0].upper() if eh_predador(animal) else obter_especie(animal)[0].lower()


def animal_para_str(animal):
    """
    animal_para_str: animal -> str
    Transformador
    Devolve a cadeia de caracteres que representa o animal da forma: especie[idade/freq. reprod.;fome/freq. aliment.]
    """
    if eh_predador(animal):
        return obter_especie(animal) + ' [' + str(obter_idade(animal)) + '/' + str(obter_freq_reproducao(animal))\
               + ';' + str(obter_fome(animal)) + '/' + str(obter_freq_alimentacao(animal)) + ']'

    else:
        return obter_especie(animal) + ' [' + str(obter_idade(animal)) + '/' + str(obter_freq_reproducao(animal)) + ']'


def eh_animal_fertil(animal):
    """
    eh_animal_fertil: animal -> booleano
    Devolve True se o animal atingiu a idade de reproducao.
    """
    return obter_idade(animal) == obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    """
    eh_animal_faminto: animal -> booleano
    Devolve True se o animal eh predador e se atingiu um valor de fome igual ou superior ah freq. de alimentacao.
    """
    return eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal)


def reproduz_animal(animal):
    """
    reproduz_animal: animal -> animal
    Devolve um novo animal da mesma especie, com idade e fome igual a 0, e alterando (destrutivamente) a idade
    do animal original para 0.
    """
    return reset_fome(cria_copia_animal(reset_idade(animal)))


        # TAD Prado:

# Representação interna: dicionário

# Operacoes basicas:

# cria_prado: posicao × tuplo × tuplo × tuplo → prado
# cria_copia_prado: prado → prado
# obter_tamanho_x: prado → int
# obter_tamanho_y: prado → int
# obter_numero_predadores: prado → int
# obter_numero_presas: prado → int
# obter_posicao_animais: prado → tuplo posicoes
# obter_animal: prado × posicao → animal
# eliminar_animal: prado × posicao → prado
# mover_animal: prado × posicao × posicao → prado
# inserir_animal: prado × animal × posicao → prado
# eh_prado: universal 􏰀→ booleano
# eh_posicao_animal: prado × posicao → booleano
# eh_posicao_obstaculo: prado × posicao → booleano
# eh_posicao_livre: prado × posicao → booleano
# prados_iguais: prado × prado → booleano
# prado_para_str: prado → str

# Funcao de Alto Nivel:

# obter_valor_numerico: prado x posicao -> int
# obter_movimento: prado x posicao -> posicao
# Funcao auxiliar: validar_caracteristicas_prado: posicao x tuplo x tuplo/lista x tuplo/lista -> booleano


def cria_prado(pos_limite, rochedos, animais, pos_animais):
    """
    cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    Construtor
    Apos valida-lo, devolve o prado com a posicao limite, rochedos, animais e respetivas posicoes no argumento.
    """
    if not eh_posicao(pos_limite) or type(rochedos) != tuple or type(animais) != tuple or type(pos_animais) != tuple:
        raise ValueError('cria_prado: argumentos invalidos')

    if not validar_caracteristicas_prado(pos_limite, rochedos, animais, pos_animais):
        raise ValueError('cria_prado: argumentos invalidos')

    return {'limite': pos_limite, 'rochedos': rochedos, 'animais': list(animais), 'pos_animais': list(pos_animais)}


def validar_caracteristicas_prado(arg_limite, arg_rochedos, arg_animais, arg_pos_animais):
    '''
    validar_caracteristicas_prado: posicao x tuplo x tuplo/lista x tuplo/lista -> booleano
    Funcao auxiliar que devolve True se os elementos do argumento puderem ser, respetivamente, um limite,
    rochedos, animais e respetivas posicoes num prado.
    '''
    numero_animais = len(arg_pos_animais)
    numero_rochedos = len(arg_rochedos)

    if numero_animais < 1 or numero_animais != len(arg_animais):
        return False

    for i in range(numero_animais):
        # se animal esta fora dos limites do prado ou numa montanha
        if not eh_posicao(arg_pos_animais[i]) or \
                not (0 < obter_pos_x(arg_pos_animais[i]) < obter_pos_x(arg_limite)) or \
                not (0 < obter_pos_y(arg_pos_animais[i]) < obter_pos_y(arg_limite)):

            return False

        if not eh_animal(arg_animais[i]):  # se nao for animal
            return False

        if i < numero_animais - 1:
            for e in range(i + 1, numero_animais):
                if posicoes_iguais(arg_pos_animais[i], arg_pos_animais[e]):  # se ha 2 ou + animais numa posicao
                    return False

    for i in range(numero_rochedos):
        # se rochedo esta fora dos limites do prado ou numa montanha
        if not eh_posicao(arg_rochedos[i]) or \
                not (0 < obter_pos_x(arg_rochedos[i]) < obter_pos_x(arg_limite)) or \
                not (0 < obter_pos_y(arg_rochedos[i]) < obter_pos_y(arg_limite)):

            return False

        if i < numero_rochedos - 1:
            for e in range(i + 1, numero_rochedos):
                if posicoes_iguais(arg_rochedos[i], arg_rochedos[e]):  # se ha 2 ou + rochedos na mesma posicao
                    return False

        for indice_animal in range(numero_animais):  # se a mesma pos tiver rochedo e animal
            if posicoes_iguais_reduzida(arg_rochedos[i], arg_pos_animais[indice_animal]):
                return False
    return True


def cria_copia_prado(prado):
    """
    cria_copia_prado: prado -> prado
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
    obter_tamanho_x: prado -> int
    Seletor
    Devolve o valor inteiro que corresponde ah dimensao Nx do prado, ou seja, ao seu numero de colunas.
    """
    return obter_pos_x(prado['limite']) + 1


def obter_tamanho_y(prado):
    """
    obter_tamanho_y: prado -> int
    Seletor
    Devolve o valor inteiro que corresponde ah dimensao Ny do prado, ou seja, ao seu numero de linhas.
    """
    return obter_pos_y(prado['limite']) + 1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado -> int
    Seletor
    Devolve o numero de animais predadores no prado.
    """
    return len(list(filter(eh_predador, prado['animais'])))


def obter_numero_presas(prado):
    """
    obter_numero_presas: prado -> int
    Seletor
    Devolve o numero de presas no prado.
    """
    return len(list(filter(eh_presa, prado['animais'])))


def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado -> tuplo posicoes
    Seletor
    Devolve um tuplo com as posicoes do prado ocupadas por animais, por ordem de leitura do prado.
    """
    return ordenar_posicoes(tuple(prado['pos_animais']))


def obter_animal(prado, posicao):
    """
    obter_animal: prado x posicao -> animal
    Seletor
    Devolve o animal do prado que se encontra na posicao dada.
    """
    for i in range(len(prado['pos_animais'])):
        if posicoes_iguais_reduzida(prado['pos_animais'][i], posicao):
            return prado['animais'][i]      # animais e posicoes correspondentes estao na mesma ordem


def eliminar_animal(prado, posicao):
    """
    eliminar_animal: prado x posicao -> prado
    Modificador (destrutivo)
    Devolve o prado apos eliminar o animal da posicao, deixando-a livre.
    """
    numero_animais = len(prado['pos_animais'])

    for i in range(numero_animais):
        if posicoes_iguais(prado['pos_animais'][i], posicao):

            prado['animais'].pop(i)
            prado['pos_animais'].pop(i)
            return prado


def mover_animal(prado, posicao_1, posicao_2):
    """
    mover_animal: prado x posicao x posicao -> prado
    Modificador (destrutivo)
    Devolve o prado apos movimentar o animal da posicao1 para a posicao2, libertando a posicao onde se encontrava.
    """
    numero_animais = len(prado['pos_animais'])

    for i in range(numero_animais):
        if posicoes_iguais(prado['pos_animais'][i], posicao_1):
            prado['pos_animais'][i] = posicao_2

    return prado


def inserir_animal(prado, animal, posicao):
    """
    inserir_animal: prado x animal x posicao -> prado
    Modificador (destrutivo)
    Devolve o prado apos acrescentar o animal na posicao dada.
    """
    prado['animais'] += [animal]
    prado['pos_animais'] += [posicao]
    return prado


def eh_prado(arg):
    """
    eh_prado: universal -> booleano
    Reconhecedor
    Devolve True se o argumento é um TAD prado.
    """
    if type(arg) != dict or len(arg) != 4:
        return False

    if 'limite' not in arg or 'rochedos' not in arg or 'animais' not in arg or 'pos_animais' not in arg:
        return False

    if not eh_posicao(arg['limite']) or type(arg['rochedos']) != tuple or type(arg['animais']) != list or\
            type(arg['pos_animais']) != list:
        return False

    if not validar_caracteristicas_prado(arg['limite'], arg['rochedos'], arg['animais'], arg['pos_animais']):
        return False

    return True


def eh_posicao_animal(prado, posicao):
    """
    eh_posicao_animal: prado x posicao -> booleano
    Reconhecedor
    Devolve True apenas se a posicao do prado esta ocupada por um animal.
    """
    n_animais = len(prado['pos_animais'])

    for i in range(n_animais):
        if posicoes_iguais_reduzida(prado['pos_animais'][i], posicao):
            return True

    return False


def eh_posicao_obstaculo(prado, posicao):
    """
    eh_posicao_obstaculo: prado x posicao -> booleano
    Reconhecedor
    Devolve True se a posicao corresponde a uma montanha ou rochedo.
    """
    if obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == obter_pos_x(prado['limite']):
        return True                           # se posicao eh uma montanha

    if obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == obter_pos_y(prado['limite']):
        return True                           # se posicao eh uma montanha

    for ind_rochedo in range(len(prado['rochedos'])):
        if posicoes_iguais_reduzida(posicao, prado['rochedos'][ind_rochedo]):  # se posicao eh um rochedo
            return True

    return False


def eh_posicao_livre(prado, posicao):
    """
    eh_posicao_obstaculo: prado x posicao -> booleano
    Reconhecedor
    Devolve True se a posicao corresponde a um espaco livre (sem animais ou obstaculos).
    """
    return not eh_posicao_obstaculo(prado, posicao) and not eh_posicao_animal(prado, posicao)


def prados_iguais(prado1, prado2):
    """
    prados_iguais: prado x prado -> booleano
    Teste
    Devolve True se prado1 e prado2 sao prados e iguais.
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
    prado_para_str: prado -> str
    Transformador
    Devolve uma cad. de caracteres que representa o prado.
    """
    Nx = obter_tamanho_x(prado) - 1  # numero de colunas exceto a coluna 0
    Ny = obter_tamanho_y(prado) - 1  # numero de linhas exceto a linha 0
    linhas_meio = ()
    linha_limite = '+' + '-' * (Nx - 1) + '+'

    animais_prado = list(obter_posicao_animais(prado))  # por ordem de leitura do prado

    for y in range(1, Ny):  # so percorre as linhas entre a primeira e a ultima
        linhas_meio += ('|',)  # representacao da coluna 0

        for x in range(1, Nx):  # so percorre as colunas entre a primeira e a ultima

            if animais_prado:   # ha animais por escrever
                if y == obter_pos_y(animais_prado[0]) and x == obter_pos_x(animais_prado[0]):
                    animal = obter_animal(prado, animais_prado[0])
                    linhas_meio += (animal_para_char(animal),)
                    animais_prado = animais_prado[1:]

                elif eh_posicao_obstaculo(prado, cria_posicao(x, y)):
                    linhas_meio += ('@',)

                else:  # posicoes livres
                    linhas_meio += ('.',)

            else:
                if eh_posicao_obstaculo(prado, cria_posicao(x, y)):  # rochedos
                    linhas_meio += ('@',)

                else:  # posicoes livres
                    linhas_meio += ('.',)

        linhas_meio += ('|\n',)  # representacao da ultima coluna

    return linha_limite + '\n' + ''.join(linhas_meio) + linha_limite


def obter_valor_numerico(prado, posicao):
    """
    obter_valor_numerico: prado x posicao -> int
    Devolve o valor numerico da posicao, correspondente ah ordem de leitura no prado.
    """
    return obter_tamanho_x(prado) * obter_pos_y(posicao) + obter_pos_x(posicao)


def obter_movimento(prado, posicao):
    """
    obter_movimento: prado x posicao -> posicao
    Devolve a posicao seguinte do animal no prado, segundo as regras de movimento dos animais.
    """
    # lista de pos adjacentes livres e sem montanhas
    pos_adjacentes = list(obter_posicoes_adjacentes(posicao))

    if eh_predador(obter_animal(prado, posicao)):
        pos_presas = []

        for pos in pos_adjacentes:
            if eh_posicao_animal(prado, pos) and eh_presa(obter_animal(prado, pos)):
                pos_presas += [pos]  # o predador come as presas, ocupando as suas posicoes

        if pos_presas:
            return pos_presas[obter_valor_numerico(prado, posicao) % len(pos_presas)]

    pos_livres = list(filter(lambda x: eh_posicao_livre(prado, x), pos_adjacentes))  # nao sao montanhas ou rochedos
    if pos_livres:
        return pos_livres[obter_valor_numerico(prado, posicao) % len(pos_livres)]  # resto do valor de pos atual // num
                                                                                                # de posicoes livres
    return posicao      # quando nao ha posicoes livres, nao se move


def geracao(prado):
    """
    geracao: prado -> prado
    Funcao auxiliar que devolve o prado, modificado de acordo com a evolucao correspondente a uma geracao completa.
    """
    presas_comidas_frente = []

    for pos_animal in obter_posicao_animais(prado):

        continua = True
        # para so percorrer os animais comidos das linhas que interessam (atual e seguinte)
        presas_comidas_frente = list(filter(lambda p: obter_pos_y(p) >= obter_pos_y(pos_animal), presas_comidas_frente))

        for presa_comida_frente in presas_comidas_frente:
            if posicoes_iguais_reduzida(pos_animal, presa_comida_frente):
                continua = False

        if continua:
            animal = obter_animal(prado, pos_animal)
            fertil = eh_animal_fertil(animal)

            if eh_predador(animal):     # a fome so aumenta nos predadores
                aumenta_fome(animal)
            if not fertil:      # quando eh fertil, a idade so voltará a aumentar apos reproduzir-se
                aumenta_idade(animal)
                fertil = eh_animal_fertil(animal)

            pos_f = obter_movimento(prado, pos_animal)

            if not posicoes_iguais_reduzida(pos_f, pos_animal):
                # quando o animal se vai mover (pos sao !=)
                if eh_posicao_animal(prado, pos_f):  # predador come a presa e ocupa a sua pos
                    eliminar_animal(prado, pos_f)   # a presa morre
                    reset_fome(animal)      # a fome passa a 0
                    presas_comidas_frente += [pos_f]

                if eh_animal_faminto(animal):
                    eliminar_animal(prado, pos_animal)   # morre ah fome
                else:
                    mover_animal(prado, pos_animal, pos_f)   # eh igual mover ou nao o animal se ele for morrer depois

                if fertil:  # so se reproduz qd se moveu e eh fertil
                    inserir_animal(prado, reproduz_animal(animal), pos_animal)  # animal-filho ocupa pos anterior do pai

            else:   # nao se moveu
                if eh_animal_faminto(animal):
                    eliminar_animal(prado, pos_f)  # morre ah fome

    return prado


def simula_ecossistema(ficheiro, num_geracoes, modo):
    """
    simula_ecossistema: str x int x booleano -> tuplo
    Funcao que escreve o prado, o numero de presas e predadores dependendo do modo (quiet, se for False, ou verboso,
    se for True) e devolve um tuplo com o numero de predadores e presas no prado, no fim da simulacao.
    """

    def escreve_geracao(prado, geracao, numero_predadores, numero_presas):  #pred presas
        """
        escreve_geracao: prado x int -> str
        Funcao auxiliar que escreve o prado pela saida standard, o numero de presas e predadores, e o numero da geracao.
        """
        return f'Predadores: {numero_predadores} vs Presas: {numero_presas} \
(Gen. {geracao})\n' + prado_para_str(prado)

    with open(ficheiro, 'r') as fich_config:
        tuplo_linha1 = eval(fich_config.readline())  # tira \n da linha
        limite = cria_posicao(tuplo_linha1[0], tuplo_linha1[1])

        tuplo_linha2 = eval(fich_config.readline())
        rochedos = ()
        for rochedo_em_tuplo in tuplo_linha2:
            rochedos += (cria_posicao(rochedo_em_tuplo[0], rochedo_em_tuplo[1]),)   # tuplo com posicoes dos rochedos

        linhas_animais = fich_config.readlines()
        animais = ()
        pos_animais = ()

    for linha_animal in linhas_animais:
        tuplo_linha_animal = eval(linha_animal)
        animais += (cria_animal(tuplo_linha_animal[0], tuplo_linha_animal[1], tuplo_linha_animal[2]),)
        pos_animais += (cria_posicao(tuplo_linha_animal[3][0], tuplo_linha_animal[3][1]),)
                                                                # tuplo com animais e tuplo com suas posicoes

    prado = cria_prado(limite, rochedos, animais, pos_animais)
    print(escreve_geracao(prado, 0, obter_numero_predadores(prado), obter_numero_presas(prado)))

    if modo:    # modo verboso
        for num_da_geracao in range(1, num_geracoes + 1):

            n_predadores_inicio = obter_numero_predadores(prado)
            n_presas_inicio = obter_numero_presas(prado)

            prado = geracao(prado)      # avanca 1 geracao

            n_predadores_fim = obter_numero_predadores(prado)
            n_presas_fim = obter_numero_presas(prado)

            if n_predadores_inicio != n_predadores_fim or n_presas_inicio != n_presas_fim:
                print(escreve_geracao(prado, num_da_geracao, n_predadores_fim, n_presas_fim))

    else:      # modo quiet

        for num_da_geracao in range(1, num_geracoes + 1):   # avanca todas as geracoes sem as escrever
            prado = geracao(prado)

        print(escreve_geracao(prado, num_geracoes, obter_numero_predadores(prado), obter_numero_presas(prado)))

    return obter_numero_predadores(prado), obter_numero_presas(prado)       # tuplo com num de predadores e presas

