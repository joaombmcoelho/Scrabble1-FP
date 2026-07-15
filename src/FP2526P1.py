'''
FP2526P1
autor: João Coelho
nº: 117964
'''

MINIMO_LETRAS_1_JOGADA = 2
N_LETRAS_JOGADOR = 7
TAMANHO_TABULEIRO = 15
N_MAX_JOGADORES = 4
letras = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Z')


def cria_conjunto(let, occ):
    
    '''
    Devolve um dicionário com o numero de ocorrências de cada letra

    Recebe dois tuplos de igual tamanho:
    let, com letras únicas do abcedário (let) 
    occ, com int positivos q correspondem ao nº de ocorrencias de cada letra

    Devolve um dicionário a que a cada letra corresponde o nº de occorências
    
    tuple, tuple -> dict
    '''

    #correção dos argumentos

    if type (let) != tuple or type (occ) != tuple:
        raise ValueError('cria_conjunto: argumentos inválidos')
    if len(let) != len (occ):
        raise ValueError('cria_conjunto: argumentos inválidos')
    let_sem_rep=list(let)
    for i in range (len(let)):
        if let[i] not in letras: #Se um elemento de let não for uma letra do abcedário considerado
            raise ValueError('cria_conjunto: argumentos inválidos')
        for j in range (len(let_sem_rep)):
            let_sem_rep[i] = " " #substitui elemento da cópia, para procurar repetições
            if let[i] == let_sem_rep[j]:
                raise ValueError('cria_conjunto: argumentos inválidos')
    for i in range (len(occ)):
        if type (occ [i]) != int or occ[i] < 1: #as ocorrencias têm de ser inteiros positivos
            raise ValueError('cria_conjunto: argumentos inválidos')
        
    #criação do conjunto

    conjunto = {}
    for i in range (len(let)):
        conjunto [let[i]] = occ [i]
    return conjunto


def gera_numero_aleatorio(estado):
    
    '''
    Recebe um inteiro positivo (seed)
    Devolve um número pseudo-aleatório através das operações xorshift

    int -> int
    '''

    estado ^= ( estado << 13) & 0xFFFFFFFF
    estado ^= ( estado >> 17) & 0xFFFFFFFF
    estado ^= ( estado << 5) & 0xFFFFFFFF
    return estado


def permuta_letras(letras, estado):
    
    '''
    Troca a ordem dos elementos da lista letras

    Recebe uma lista de letras e o estado inicial (inteiro positivo, para gerar número pseudo-aleatório
    Devolve uma lista permutada de acordo com o algoritmo de Fisher-Yates

    list, int -> list
    '''

    for i in range (len(letras) -1, 0, -1):
        estado = gera_numero_aleatorio(estado) #atualização do estado p/ a seguinte iteração
        j = estado % (i+1) #o módulo de (i+1) limita o numero gerado ao intervalo 0<=j<=i
        letras [j], letras[i] = letras[i], letras[j]


def baralha_conjunto(conj, estado):
    
    '''
    Baralha o conjunto após o ordenar numa lista

    Recebe um conjunto de letras (dicionário) e o estado inicial (inteiro positivo),
    para a permutação, chama a função 'ordena_letras', para as ordenar numa lista;
    E chama a função 'permuta_letras' para as permutar
    Devolve a lista com as letras permutadas

    dict, int -> list
    '''

    letras_ordenadas = ordena_letras (letras, conj) 
    permuta_letras(letras_ordenadas, estado)
    return letras_ordenadas


def testa_palavra_padrao(palavra, padrao, conj):
    
    '''
    Verifica se um padrão pode ser preenchido por uma palavra

    Recebe uma palavra (string), um padrão (string), formado pelo caracter '.' 
    e por letras, e um conjunto de letras (dicionário).
    Copia o conjunto para não o modificar destrutivamente
    Verifica se é possível formar essa palavra preenchendo nos espaços do padrao 
    com o carater '.', as letras no conjunto de letras.
    Chama a função 'elimina_letra_conjunto', para prosseguir a verificação
    caracater a caracter, dado que as letras verificadas não podem ser verificadas novamente
    Devolve True se for possível fazê-lo
    Devolce False, caso contrário.
    
    string, string, dict -> bool
    '''

    conj2=conj.copy()
    for i in range (len(padrao)):
        if padrao [i] != palavra [i] and padrao [i] != '.': #se a letra no padrao nao constar na mesma pos. na palavra
            return False
        elif len (padrao) != len (palavra):
            return False
        elif padrao [i] == '.':
            letra = palavra[i]
            if not elimina_letra_conjunto(conj2, letra):
                return False
    return True


def cria_tabuleiro():
    
    '''
    Gera a lista correspondente ao tabuleiro

    Quando invocada, gera um tabuleiro, que corresponde a uma lista com 15 listas,
    (cada uma corresponde a uma linha), geradas pela função 'gerador_linhas'
    Devolve essa lista

    {} -> list
    '''

    tab=[]
    for i in range (0,15,1):
        tab += [gerador_linhas(), ]
    return tab


def cria_casa(l,c):
    
    '''
    Recebe uma abcissa e ordenada e devolve a casa correspondente

    Recebe dois inteiros positivos l (linha),c (coluna),
    Valores entre 1 e o tamanho do tabuleiro
    Verifica os seus argumentos
    Devolve um tuplo correspondente à casa do tabuleiro (linha, coluna)

    int, int -> tuple
    '''

    if not (type (l) == int and type (c) == int and l<= TAMANHO_TABULEIRO and l>=1 and c<= TAMANHO_TABULEIRO and c>=1):
            raise ValueError('cria_casa: argumentos inválidos')
    casa=(l, c)
    return casa


def obtem_valor(tab,casa):
    
    '''
    Procura no tabueliro o valor da casa pretendida

    Recebe o tabuleiro (list) e a casa (tuple), e para procurar o valor,
    reduz o índice em 1, pois a contagem das linhas e das colunas é de 1-TAMANHO_TABULEIRO
    Em vez de 0 a TAMANHO_TABULEIRO-1
    casa[0] corresponde a l, linha
    casa[1] corresponde a c, coluna
    Devolve o valor encontrado (string)

    list, tuple -> str
    '''

    valor = tab [casa[0]-1] [casa[1]-1] 
    return valor


def insere_letra(tab, casa, letra):
    
    '''
    Insere uma letra na casa pretendida do tabuleiro

    Recebe o tabuleiro (list), uma casa (tuple) e uma letra (string) 
    e insere-a na casa escolhida do tabuleiro
    Modifica destrutivamente o tabuleiro, por atribuição.

    list, tuple, str -> list
    '''

    tab[casa[0]- 1] [casa[1] -1] = letra
    return tab


def obtem_sequencia(tab, casa, direcao, tamanho):
    
    '''
    Procura, no tabuleiro, os caracteres da posição até ao tamanho pretendidos

    Recebe o tabuleiro (list), uma casa (tuple), 
    a direção (string) ('H' - Horizontal; 'V' - Vertical),
    e o tamanho pretendido da str a procurar (int positivo)
    Recorre à função 'cria_casa' e 'obtem_valor' para aceder ao tabuleiro
    Devolve uma str que parte da casa escolhida para a direita (direção = 'H), 
    ou para baixo (direção = 'V'), com o comprimento dado pelo tamanho
    
    list, tuple, str, int -> str
    '''

    sequencia = ""
    if direcao == 'H': 
        for i in range (0, tamanho, 1):
            casa_h = cria_casa (casa[0], casa[1]+i) #avança uma coluna à direita
            sequencia += obtem_valor(tab,casa_h) #faz a concatenação das letras atingir o tamanho inserido
    elif direcao == 'V':
        for i in range (0, tamanho, 1):
            casa_v = cria_casa (casa[0]+i, casa[1]) #desce uma linha
            sequencia += obtem_valor (tab, casa_v)
    return sequencia


def insere_palavra(tab, casa, direcao, palavra):
    
    '''
    Insere, no tabuleiro, uma palavra, a partir casa e na direção escolhidas

    Recebe o tabuleiro (list), uma casa (tuple),
    a direção (string) ('H' - Horizontal; 'V' - Vertical),
    e a palavra a inserir no tabuleiro (string)
    Recorre à função 'cria_casa' e 'insere_letra' para aceder e modificar o tabuleiro
    Devolve o tabuleiro com a palavra que parte da casa escolhida ,
    para a direita (direção = 'H), ou para baixo (direção = 'V')

    list, tuple, str, str -> list
    '''

    if direcao == 'H':
        for i in range (0, len(palavra), 1):
            casa_h = cria_casa (casa[0], casa[1]+i)
            tab = insere_letra (tab, casa_h, palavra[i]) #insere letras à direita
    elif direcao == 'V':
        for i in range (0, len(palavra), 1):
            casa_v = cria_casa (casa[0]+i, casa[1])
            tab = insere_letra (tab, casa_v, palavra[i]) #insere letras abaixo
    return tab


#3.2.7 tabuleiro para str: tabuleiro → cad. carateres

def tabuleiro_para_str(tab):

    '''
    Constrói a representação visual do tabuleiro

    Recebe um tabuleiro (list)
    Cria uma string que é concatenada sucessivamente até ser obtido o tabuleiro
    Devolve a cadeia de caracteres que o representa

    list -> str
    '''

    tab_str = '                       1 1 1 1 1 1\n'
    tab_str += '     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5\n'
    tab_str += '   +-------------------------------+\n'
    for linha in range (0, len(tab), 1):
        tab_str += f'{linha+1:>2} |' #linha 0 da lista -> linha 1 do tabuleiro
        for coluna in range(0,len(tab),1):
            tab_str += f' {tab[linha][coluna]}' #procura o elemento na posicao [linha][coluna]
        tab_str += " |\n"
    tab_str += '   +-------------------------------+'
    return tab_str
    

def cria_jogador(ordem, pontos, conj_letras):

    '''
    Cria um jogador com a sua ordem, pontos e conj. letras respetivo

    Recebe a ordem do jogador (int positivo, 0<ordem<5) 
    e os seus pontos, (int positivo de até 3 digitos) e um conjunto de letras
    Verifica os seus argumentos

    Devolve um dicionário que representa o jogador do scrabble com as chaves:
    'id', 'pontos' e 'letras' e os seus respetivos valores

    int, int, dict -> dict
    '''

    #Verificação dos argumentos

    if not (type (ordem) == int and ordem>0 and ordem<5 and type(pontos) == int and type(conj_letras) == dict and pontos >=0 and len(str(pontos))<=3):
        raise ValueError('cria_jogador: argumentos inválidos')

    n_letras = 0
    for chave in conj_letras:
        if not type(chave) == str:
            raise ValueError ('cria_jogador: argumentos inválidos')
        n_letras +=  conj_letras[chave]
        if conj_letras[chave] <0 or n_letras>7: 
            raise ValueError('cria_jogador: argumentos inválidos')

    for letra in conj_letras:
        if letra not in letras:
            raise ValueError('cria_jogador: argumentos inválidos')
    
    return {'id':ordem, 'pontos':pontos, 'letras':conj_letras}


def jogador_para_str(jog):

    '''
    Recebe um jogador (dicionário) e devolve uma representação visual do mesmo (string)
    
    Recorre à função 'ordena_letras' para as ordenar

    dict -> str
    '''

    id = jog['id']
    pontos = jog ['pontos']
    conj_letras = jog ['letras']
    str_letras = ""
    letras_ordenadas = ordena_letras(letras, conj_letras) #cria uma lista nova
    for letra in letras_ordenadas: 
        str_letras += f' {letra}' #converte os elementos dessa lista numa string para o output
    res = f'#{id} ({pontos:>3}):{str_letras}'
    return res


def distribui_letra(letras, jogador):
    
    '''
    Retira ultima letra da lista e adiciona-a ao conjunto do jogador

    Recebe uma lista de letras e o dicionário que representa o jogador
    Devolve False se a lista for vazia
    Caso contrário:
        Modifica destrutivamente a lista e o jogador:
        Retira a ultima letra da lista, adicionando-a ao conjunto de letras do jogador
        Devolve True

    list, dict -> bool
    '''

    if letras == []:
        return False
    else:
        ultima_letra = letras[len(letras)-1]
        if ultima_letra in jogador['letras']:
            jogador['letras'][ultima_letra] += 1 #adiciona um valor à chave
        else:
            jogador['letras'].update({ultima_letra: 1}) #se não pertencer, adiciona o par letra:valor
        del(letras[len(letras)-1]) #apaga o ultima elemento da lista
        return True


def joga_palavra(tab, palavra, casa, direcao, conj_letras, primeira):

    '''
    Permite jogar uma palavra no tabuleiro

    Recebe o tabuleiro(list), a palavra a inserir (string), a casa de partida (tuple),
    a direcao (string), 'H' ou 'V', o dicionário que representa o conjunto de letras
    e um booleano que identifica se é ou não a primeira jogada
    Consoante as regras do jogo, a função tem um comportamento diferente se se trata
    da primeira jogada ou não. Recorre às funções 'testa_palavra_padrao', 'cria_casa',
    'insere_palavra', 'elimina_str' e 'ordena_letras_para_tuplo'
    Devolve um tuplo vazio se a jogada não for válida, mas, se o for, devolve o tuplo
    com as letras jogadas pelo jogador

    list, str, tuple, str, dict, bool -> tuple
    '''

    res = ()
    #testar se a palavra cabe no tabuleiro
    if direcao == 'H':
        len_horz = TAMANHO_TABULEIRO - casa[1] + 1 #'H': Tamanho disponivel = total - posição inicial na linha (col) + 1
        if len(palavra) > len_horz:
            return res
    elif direcao == 'V':
        len_vert = TAMANHO_TABULEIRO - casa [0] + 1 
        if len(palavra) > len_vert:
            return res
    
    padrao_tabuleiro=obtem_sequencia(tab, casa, direcao, len(palavra))

    #o conjunto tem de conter todas as letras necessária para formar a palavra
    if not testa_palavra_padrao(palavra, padrao_tabuleiro, conj_letras):
        return res
    if primeira == True: 
        if len(palavra) < MINIMO_LETRAS_1_JOGADA:
            return res
        meio = len(tab) // 2 + 1  #len(tab) sempre impar
        casa_central = cria_casa(meio,meio)
        cobre_casa_c = False
        for i in range (0, len(palavra), 1): #Ver se cobre a casa central
            if direcao == 'H':
                casa_h = cria_casa (casa[0], casa[1]+i) #avança uma coluna à direita 
                if casa_h == casa_central:
                    cobre_casa_c = True
                    break
            elif direcao == 'V':
                casa_v = cria_casa (casa[0]+i, casa[1]) #desce uma linha
                if casa_v == casa_central:
                    cobre_casa_c = True
                    break
        if not cobre_casa_c:
            return res
    
    else: #primeira == False:

        # a palavra tem de conter uma letra do padrao
        contem_peca_tab = False
        for letra in palavra:
            if letra in padrao_tabuleiro: #se houver uma letra da palavra no padrão, está na posiçao certa
                contem_peca_tab = True 
                break
        if contem_peca_tab != True: 
            return res
        # o jogador deve utilizar pelo menos uma letra do seu conjunto, tem de preencher pelo menos uma casa
        if '.' not in padrao_tabuleiro: 
            return res
        
    # Se a jogada é válida
    insere_palavra(tab, casa, direcao, palavra)
    #Tem de se retirar as letras que já estão no padrão, pois não fazem parte do conjunto

    palavra_final = elimina_str(palavra, padrao_tabuleiro)
    res += ordena_letras_para_tuplo(palavra_final, letras)
    return res

    
def processa_jogada(tab, jog, pilha, pontos, primeira):

    '''
    Consoante o input, permite passar, trocar ou jogar no Scrabble

    Recebe o tabuleiro (list), jog (dict), a pilha (list), um dicionário
    com os pontos de cada letra e um booleano que identifica se é ou não a primeira jogada.
    Até a jogada ser válida, pede ao jogador um input 'P', 'T' <seq_letras> ou 'J' <linha> <coluna> <dir> <palavra>
    Se o input for 'P' (passar), a função devolve False e termina o ciclo
    Se o input começar por 'T' (trocar), a função vai analisar se a jogada é válida e se o for,
    troca as letras da palavra por letras da pilha, caso contrário pede um novo input
    Se o input começar por 'J' (jogar), a função analisa se a jogada é válida e se o for,
    joga as letras da palavra no tabuleiro e substitui-as por letras da pilha, 
    caso contrário pede um noov input
    Devolve False para a jogada 'passar' e True para as outras jogadas válidas

    list, dict, list, dict, bool -> bool
    '''

    while True:
        jogada_jogador=input(f"Jogada J{jog['id']}: ").split() #transforma numa lista com os elementos sem os espaços
        conj_letras = jog ['letras']
        if len (jogada_jogador) == 0:
            continue
        if jogada_jogador[0] == 'P' and len(jogada_jogador) == 1: 
            return False
        
        #T - Trocar
        elif jogada_jogador[0] == 'T': 
            palavra = ""
            for i in range (1,len(jogada_jogador),1): #concatena as letras a trocar numa palavra
                if jogada_jogador[i] in letras: 
                    palavra += jogada_jogador[i]
            if len (palavra) == 0 and len(jogada_jogador) > 1:
                continue
            if len(palavra) > N_LETRAS_JOGADOR: #não trocar mais letras que as que se tem
                continue 
            if len(pilha) < len(palavra): #não trocar se ja nao houverem letras na pilha
                continue
            conj_teste={'id': jog['id'], 'pontos': jog['pontos'], 'letras': jog['letras'].copy()} 
            #copia apenas as letras, pq senao nao funciona, para testar em baixo para nao modificar destrutivamente
            pilha_teste=pilha.copy()
            if not elimina_let_substitui_conj(pilha_teste, conj_teste, palavra): #Assim, permite que não se troquem letras que não se tem
                continue
            elimina_let_substitui_conj(pilha, jog, palavra) #Só se modifica destrutivamente, depois de garantir que é válida
            return True
        
        #J - Jogar
        elif jogada_jogador[0] == 'J': 
            if len (jogada_jogador) != 5: #no caso de input inválido
                continue
            direcao = jogada_jogador[3]
            palavra = jogada_jogador[4]
            try:
                casa=cria_casa(int(jogada_jogador[1]),int(jogada_jogador[2]))
            except ValueError: #para nao parar o ciclo
                continue
            jogada = joga_palavra(tab, palavra, casa, direcao, conj_letras, primeira)
            if jogada == (): #se inválida, pede input outra vez
                continue        
            for pos_letra in range(0,len(palavra),1): #Contagem dos pontos
                letra = palavra[pos_letra]
                jog['pontos'] += pontos[letra]
            if not elimina_let_substitui_conj(pilha, jog, jogada): #Dá-se novas letras ao jogador, pq já sabemos que é válida
                continue
            return True


def scrabble(jogadores, saco, pontos, seed):

    '''
    Permite jogar o jogo 'Scrabble'

    Recebe o nº de jogadores (int) entre 1 e N_MAX_JOGADORES, o saco (dict) com todas as letras a distribuir,
    os pontos (dict) com a pontuação de cada letra e a seed (int positivo) para gerar um número pseudo-aleatório.
    Valida os seus argumentos, e se forem válidos, entra num ciclo que só termina quando já não houverem letras
    na pilha ou nos conjuntos dos jogadores ou quando todos os jogadore spassarem a jogada.
    Recorre à função 'processa_jogada', para o concretizar, à baralha_conjunto' para baralhar as letras do saco,
    à 'distribui_letra', para distribuir as letras do saco pelos jogadores, à 'cria_jogador', para os criar 
    e à função 'tabuleiro_para_str' e'jogador_para_str' para a representação visual do jogo.
    Devolve um tuplo com as pontuações dos jogadores no fim do jogo

    int, dict, dict, int -> tuple
    '''
    #Correção de argumentos
    if (jogadores<2 or jogadores>N_MAX_JOGADORES) or type(jogadores) != int:
        raise ValueError('scrabble: argumentos inválidos')
    if type (saco) != dict or type (pontos) != dict or type(seed) != int or seed<1:
        raise ValueError('scrabble: argumentos inválidos')
    for letra in saco:
        if letra not in pontos:
            raise ValueError('scrabble: argumentos inválidos')
    
    for chave in pontos:
        if chave not in letras:
            raise ValueError('scrabble: argumentos inválidos')
        elif type (pontos[chave]) != int or pontos[chave] <1:
            raise ValueError('scrabble: argumentos inválidos')
    
    #Verificar se letras no saco são suficientes para o nº de jogadores:

    soma_valores = 0
    for chave in saco:
        if chave not in letras:
            raise ValueError('scrabble: argumentos inválidos')
        elif type (saco[chave]) != int or saco[chave] <1:
            raise ValueError('scrabble: argumentos inválidos')
        soma_valores += saco[chave]
    if soma_valores < 7 * jogadores:
        raise ValueError ('scrabble: argumentos inválidos')

    #baralhar o saco de letras e dist. o conjunto de 7 letras pelos pelos jogadores em ordem
    pilha = baralha_conjunto(saco, seed)
    
    #lista dos jogadores e dos seus conjuntos
    lista_jogadores = []
    primeira = True
    gerar_jogo = True #Quando o início do jogo for gerado, passa a False
    pontuacao=0
    passou=0
    tab = cria_tabuleiro()
    print('Bem-vindo ao SCRABBLE.')
    print(tabuleiro_para_str(tab))

    while True:
        if gerar_jogo==True:
            for i in range(0,jogadores):
                #criar o jogador
                novo_jogador = cria_jogador (i+1, pontuacao, {})
                #dist as letras
                for j in range (0, N_LETRAS_JOGADOR):
                    distribui_letra (pilha, novo_jogador)
                lista_jogadores.append(novo_jogador) #cria uma lista de dicionários, cada um representará um jogador
               
        for k in range(0, jogadores): #Ciclo para cada jogada de cada jogador
            for l in range(0,jogadores):
                if pilha == [] and lista_jogadores[l]['letras'] == {}: #se pilha vazia e jogador sem letras
                    return resultado
                print(jogador_para_str(lista_jogadores[l]))
            if processa_jogada(tab, lista_jogadores[k], pilha, pontos, primeira) == False: 
                passou+=1 #conta as jogadas passadas
            else:
                passou = 0 #reincia o contador de jogadas passadas
                if primeira:
                    primeira = False
            resultado = ()
            for i in range (0, jogadores):
                resultado += (lista_jogadores[i]['pontos'], ) #atualiza o tuplo dos pontos
            if passou == jogadores:
                return resultado #se todos os jogadores passarem, termina
            if pilha == []:
                return resultado
            print(tabuleiro_para_str(tab))
        gerar_jogo = False #início do jogo já foi gerado


#FUNÇÕES AUXILIARES

def ordena_letras(letras, conj):

    '''
    Ordena as letras de um conjunto numa lista

    Recebe um tuplo com o alfabeto considerado
    E um dicionário que representa conjunto de letras
    Percorre o alfabeto e, ao encontrar uma dessas letras como chave do dicionário,
    acrescenta-a, valor vezes, à nova lista, garantindo ordenação correta
    Devolve a lista com os elementos do conjunto de letras ordenados

    tuple, dict -> list
    '''

    letras_ordenadas = [] 
    for chave in letras: 
        if chave in conj:  
            letras_ordenadas += [chave, ] * conj[chave]
    return letras_ordenadas


def elimina_letra_conjunto(conj, letra):

    '''
    Elimina 1x a letra pretendida do conjunto

    Recebe um conjunto (dicionário) e uma letra (string);
    Elimina uma ocorrência dessa letra, -1 valor a cada chave
    Se o valor não for positivo, elimina o par chave: valor
    Devolve False se a letra não estivar no conjunto
    Devole True após eliminá-la do conjunto

    dict, str -> bool
    '''

    if letra not in conj:
        return False
    conj[letra] = conj[letra] - 1 #Remove um valor à chave correspondente
    if conj[letra] <= 0: 
        del conj[letra] #se o valor não for positivo, a letra é removida
    return True


def gerador_linhas():
    
    '''
    Gera uma lista que corresponde a uma linha do tabuleiro

    Quando chamada, gera uma lista correspondente a uma linha do tabuleiro, 
    com 15 elementos (colunas) , em que cada elemento é o carater '.'
    Devolve essa lista

    {} -> list
    '''

    linha=[]
    for i in range (0,TAMANHO_TABULEIRO,1):
        linha += ['.', ]
    return linha


def elimina_str(palavra,padrao): 
    
    '''
    Elimina da palavra as letras já presentes no padrão do tabuleiro

    Recebe uma palavra (string) e um padrão (string)
    Copia-os para listas mutáveis
    Percorre a lista da palavra e se alguma letra já estiver na lista do padrão,
    percorre-a e elimina a primeira ocorrência dessa letra da lista do padrão,
    para as próximas iterações e da lista da palavra, como pretendido.
    Assim, Devolve a lista com as letras que o jogador usou
    
    str, str -> list
    '''
    
    palavra_lista=list(palavra) #converter em lista para poder eliminar ocorrencias
    padrao_lista=list(padrao)
    i=0
    while i < len(palavra_lista): #percorre a palavra
        j = 0
        if palavra_lista[i] in padrao_lista: 
            while j < len (padrao_lista):
                if padrao_lista[j] == palavra_lista[i]: #elimina p/ prox. iterações sem repetições
                    del(padrao_lista[j]) 
                    break                #Qnd elimina letra, avança p/ prox. iteração
                else:j+=1   
            del(palavra_lista[i]) #elimina a primeira ocorrencia da letra, na palavra
        else:
            i+=1
    return palavra_lista 


def ordena_letras_para_tuplo(palavra, letras):

    '''
    Ordena letras de uma palavra num tuplo

    Pode receber uma palavra (string) ou uma lista com letras de uma palavra
    e o tuplo com as letras do abcedário considerado.
    Percorre as letras de letras, para ordenação e conta quantas vezes essa letra se repete
    Devolve o tuplo com as letras, no nº de vezes que se repetem, ordenadas.

    palavra, tuple -> tuple
    '''

    t = ()
    for letra in letras: 
        occ = 0 #reinicia o contador para cada letra
        for letra_palavra in palavra: #para cada letra de letras, percorre as letras da palavra
            if letra_palavra == letra:  
                occ +=1 #Conta o nº de repetições de certa letra na palavra, occ=0 se não ocorrer
        t += (letra, ) * occ
    return t
        

def elimina_let_substitui_conj(pilha, jog, palavra):

    '''
    Elimina do conjunto as letras jogadas, substituindo-as pelas últimas letras da pilha

    Recebe a pilha (list), o jogador (dict) e uma palavra (str) e recorre à função
    'elimina_let_conj' para eliminar as letras jogadas do conjunto do jogador e, para
    acrescentar novas letras ao conjunto, recorre à função 'distribui_letra' que as
    retirará da pilha.
    Devolve False se as letras a jogar não estiverem no conjunto e True caso contrário.

    list, dict, str -> bool
    '''

    for letra in palavra:
        if not elimina_letra_conjunto(jog['letras'], letra):
            return False
        distribui_letra(pilha, jog)
    else:
        return True
        
