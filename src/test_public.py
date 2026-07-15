import pytest 
import sys
import FP2526P1 as fp  # <--- Change the name FP2526P1 to the file name with your project

class TestPublicSaco:
    def test_1(self):
        saco = {'A': 14, 'B':3}
        assert fp.cria_conjunto(('A','B'), (14, 3)) == saco

    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B'), (14, -3))
        assert "cria_conjunto: argumentos inválidos" == str(excinfo.value)

    def test_3(self):
        assert (fp.gera_numero_aleatorio(1), fp.gera_numero_aleatorio(25)) == \
            (270369, 6759192)

    def test_4(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        assert fp.permuta_letras(letras, 1) ==  None and letras == ['D', 'B', 'A', 'C', 'G', 'H', 'I', 'F', 'E', 'J']

    def test_5(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        assert fp.permuta_letras(letras, 2) ==  None and letras ==   ['H', 'A', 'J', 'F', 'G', 'E', 'B', 'C', 'D', 'I']
    
    
    def test_6(self):
        saco = fp.cria_conjunto(('A','B','C','D'), (4,2,3,3))
        assert fp.baralha_conjunto(saco, 1) == ['C', 'A', 'A', 'C', 'A', 'B', 'B', 'D', 'C', 'D', 'A', 'D']
        
    def test_7(self):
        saco = fp.cria_conjunto(('A','B','C','D'), (4,2,3,3))
        assert fp.baralha_conjunto(saco, 3) == ['A', 'B', 'A', 'D', 'B', 'C', 'A', 'C', 'D', 'C', 'D', 'A']
        
    def test_8(self):
        conjunto = fp.cria_conjunto(('A','C','S','V'), (1,2,1,1))
        assert not fp.testa_palavra_padrao('VACA', '....', conjunto)
        
    def test_9(self):
        conjunto = fp.cria_conjunto(('A','C','S','V'), (1,2,1,1))
        assert not fp.testa_palavra_padrao('VACA', '.A.', conjunto)
        
    def test_10(self):
        conjunto = fp.cria_conjunto(('A','C','S','V'), (1,2,1,1))
        assert fp.testa_palavra_padrao('VACA', '.A..', conjunto)
        


class TestPublicTabuleiro:
    def test_1(self):
        tab =  [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
        assert fp.cria_tabuleiro() == tab
        
    def test_2(self):
        assert fp.cria_casa(8,8) == (8, 8)
    
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(1,20)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)

    def test_4(self):
        tab = fp.cria_tabuleiro()
        c1, c2 = fp.cria_casa(8,6), fp.cria_casa(6,8)
        tab = fp.insere_letra(tab, c1, 'A')
        tab = fp.insere_letra(tab, c2, 'B')
        
        assert (fp.obtem_valor(tab, c1),  fp.obtem_valor(tab, c2)) == ('A', 'B')
        
    def test_5(self):
        tab = fp.cria_tabuleiro()
        tab = fp.insere_palavra(tab, fp.cria_casa(8,3), 'H', 'COMPUTADOR')
        
        assert fp.obtem_sequencia(tab, fp.cria_casa(8,10), 'H', 3) == 'DOR'
        
    def test_6(self):
        tab = fp.cria_tabuleiro()
        tab = fp.insere_palavra(tab, fp.cria_casa(8,3), 'H', 'COMPUTADOR')
        
        assert fp.obtem_sequencia(tab, fp.cria_casa(7,5), 'V', 4) == '.M..'
        
        
    def test_7(self):
        tab = fp.cria_tabuleiro()
        stab = \
            '''                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+'''
        assert fp.tabuleiro_para_str(tab) == stab
       
    def test_8(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, fp.cria_casa(8,1), 'H', 'FUNDAMENTOS')
        fp.insere_palavra(tab, fp.cria_casa(8,4), 'V', 'DA')
        fp.insere_palavra(tab, fp.cria_casa(2,6), 'V', 'PROGRAMAÇAO')
        stab = \
            '''                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . P . . . . . . . . . |
 3 | . . . . . R . . . . . . . . . |
 4 | . . . . . O . . . . . . . . . |
 5 | . . . . . G . . . . . . . . . |
 6 | . . . . . R . . . . . . . . . |
 7 | . . . . . A . . . . . . . . . |
 8 | F U N D A M E N T O S . . . . |
 9 | . . . A . A . . . . . . . . . |
10 | . . . . . Ç . . . . . . . . . |
11 | . . . . . A . . . . . . . . . |
12 | . . . . . O . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+'''
        assert fp.tabuleiro_para_str(tab) == stab 
        

class TestPublicJogador:
    def test_1(self):
        assert fp.cria_jogador(2, 0, fp.cria_conjunto((),())) == {'id':2, 'pontos':0, 'letras':{}}
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(5, 0, fp.cria_conjunto((),()))
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
      
    def test_3(self):
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1)))
        assert fp.jogador_para_str(jog1) == '#1 (  0): A C C N O O O'

    def test_4(self):
        jog2 = fp.cria_jogador(2, 13, fp.cria_conjunto(('A', 'B', 'E', 'J'),(2,1,3,1)))
        assert fp.jogador_para_str(jog2) == '#2 ( 13): A A B E E E J'
  
    def test_5(self):
        jog = fp.cria_jogador(1, 0, fp.cria_conjunto((),()))
        letras = ['A', 'B', 'C', 'A']
        assert fp.distribui_letra(letras, jog)
        
    def test_6(self):
        jog = fp.cria_jogador(1, 0, fp.cria_conjunto((),()))
        letras = ['A', 'B', 'C', 'A']
        _ = fp.distribui_letra(letras, jog)
        assert (letras, jog) == (['A', 'B', 'C'], {'id': 1, 'pontos': 0, 'letras': {'A': 1}})
        
    def test_7(self):
        jog = fp.cria_jogador(1, 0, fp.cria_conjunto((),()))
        letras = ['A', 'B', 'C', 'A']
        while letras: fp.distribui_letra(letras, jog)
        assert (letras, jog) == ([], {'id': 1, 'pontos': 0, 'letras': {'A': 2, 'C': 1, 'B': 1}}) and \
            not fp.distribui_letra(letras, jog) 
        
class TestPublicJogo:
    def test_1(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        #('C', 'C', 'A', 'O', 'O', 'O', 'N')
        assert fp.joga_palavra(tab, 'VACA', fp.cria_casa(8,8), 'H', conj_letras1, True) == ()

    def test_2(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'CAO', fp.cria_casa(7,8), 'H', conj_letras1, True) == ()
        
    def test_3(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'CAO', fp.cria_casa(8,8), 'H', conj_letras1, False) == ()
            
    def test_4(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'CAO', fp.cria_casa(8,8), 'H', conj_letras1, True) == ('A', 'C', 'O')
            
    def test_5(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('P', 'E', 'O', 'R'),(2,1,3,1))
        fp.joga_palavra(tab, 'CAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        assert fp.joga_palavra(tab, 'PERO', fp.cria_casa(2,2), 'V', conj_letras2, False) == ()
        
    def test_6(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('P', 'E', 'O', 'R'),(2,1,3,1))
        fp.joga_palavra(tab, 'CAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        assert fp.joga_palavra(tab, 'PERO', fp.cria_casa(5,10), 'V', conj_letras2, False) == ('E', 'P', 'R')

    def test_7(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('P', 'E', 'O', 'R'),(2,1,3,1))
        fp.joga_palavra(tab, 'CAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        fp.joga_palavra(tab, 'PERO', fp.cria_casa(5,10), 'V', conj_letras2, False)
        
        stab = """                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . P . . . . . |
 6 | . . . . . . . . . E . . . . . |
 7 | . . . . . . . . . R . . . . . |
 8 | . . . . . . . C A O . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+"""
        
        assert fp.tabuleiro_para_str(tab) ==  stab
    
    def test_8(self):
        
        LETRAS_PONTOS = {
            "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
            "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
            "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8 }

        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS, True, "olà\nP\n") == (res, text)

    def test_9(self):
        
        LETRAS_PONTOS = {
            "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
            "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
            "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8 }

        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        
        
        res, text = True, 'Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS, True, "T X A\n") == (res, text) and \
            fp.jogador_para_str(jog1) == '#1 (  0): A D F I O T U' and \
                saco == ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J'] 

    def test_10(self):
        
        LETRAS_PONTOS = {
            "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
            "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
            "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8 }


        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J']
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'D', 'U','O','T','I','F'),(1,1,1,1,1,1,1)))
        
        
        res, text = True, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS, True, "J 7 8 V LUTA\nJ 7 8 V TOFU\n") == (res, text) and \
            fp.jogador_para_str(jog1) == '#1 (  7): A D E E I J S' and \
                saco == ['S', 'B', 'P', 'E', 'C']
      
    def test_11(self):
        
        LETRAS_PONTOS = {
            "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
            "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
            "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8 }

        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J']
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'D', 'U','O','T','I','F'),(1,1,1,1,1,1,1)))
        
    
        tab_str = """                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . T . . . . . . . |
 8 | . . . . . . . O . . . . . . . |
 9 | . . . . . . . F . . . . . . . |
10 | . . . . . . . U . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+"""
        
        res, text = True, 'Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS, True, "J 7 8 V TOFU\n") == (res, text) and \
            fp.tabuleiro_para_str(tab) == tab_str
          
        
    
    def test_12(self):
        pontos = {
        "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
        "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
        "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8 }


        saco = {
        "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
        "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
        "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
        
        res = (11, 19)
        assert scrabble_offline(2, saco, pontos,  32, JOGADA_PUBLIC_1) == (res, OUTPUT_PUBLIC_1) 

        
    def test_13(self):
        pontos = {"A": 1}

        saco = {
        "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
        "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
        "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
        
        
        with pytest.raises(ValueError) as excinfo:
            scrabble_offline(2, saco, pontos,  33, JOGADA_PUBLIC_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
        

### AUXILIAR CODE NECESSARY TO REPLACE STANDARD INPUT 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def processa_jogada_offline(tabuleiro, jogador, saco, letras_pontos, first, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.processa_jogada(tabuleiro, jogador, saco, letras_pontos, first)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout
        

def scrabble_offline(num_jogadores, letras_contagem, letras_pontos, seed, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.scrabble(num_jogadores, letras_contagem, letras_pontos, seed)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

# JOGOS AUTOMATICOS
JOGADA_PUBLIC_1 = 'J 6 8 V DEMO\nJ 9 4 H NOIVO\nJ 6 8 H DEITA\nJ 6 12 V ACABOU\nP\nP\n'
OUTPUT_PUBLIC_1 = """Bem-vindo ao SCRABBLE.
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  0): B Ç D E M O U
#2 (  0): A B I N O O V
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . D . . . . . . . |
 7 | . . . . . . . E . . . . . . . |
 8 | . . . . . . . M . . . . . . . |
 9 | . . . . . . . O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  5): A B Ç E I T U
#2 (  0): A B I N O O V
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . D . . . . . . . |
 7 | . . . . . . . E . . . . . . . |
 8 | . . . . . . . M . . . . . . . |
 9 | . . . N O I V O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  5): A B Ç E I T U
#2 ( 10): A A B B C O U
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . D E I T A . . . |
 7 | . . . . . . . E . . . . . . . |
 8 | . . . . . . . M . . . . . . . |
 9 | . . . N O I V O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 11): A B Ç O R S U
#2 ( 10): A A B B C O U
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . D E I T A . . . |
 7 | . . . . . . . E . . . C . . . |
 8 | . . . . . . . M . . . A . . . |
 9 | . . . N O I V O . . . B . . . |
10 | . . . . . . . . . . . O . . . |
11 | . . . . . . . . . . . U . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 11): A B Ç O R S U
#2 ( 19): A A A B E M O
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . D E I T A . . . |
 7 | . . . . . . . E . . . C . . . |
 8 | . . . . . . . M . . . A . . . |
 9 | . . . N O I V O . . . B . . . |
10 | . . . . . . . . . . . O . . . |
11 | . . . . . . . . . . . U . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 11): A B Ç O R S U
#2 ( 19): A A A B E M O
Jogada J2: """
