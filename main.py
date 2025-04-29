import tkinter as tk #Importando a biblioteca gráfica usada

expressao = "" #Cria uma string para armazenar a expressão que o usuario digitar

def add_numero(num): #Define a função que adiciona um numero a expressão conforme o usuario aperta o botão do valor desejado
    global expressao #Declarando a variavel global dentro da função para que ela possa ser modificada dentro dessa função

    #Adiciona uma validação de parenteses onde impede que seja adicionado um ')' sem um '(' correspondente
    if num == ')' and expressao.count('(') <= expressao.count(')'):
        return  # Bloqueia ")" sem "(" correspondente

    # Validação especial para ponto decimal
    elif num == '.':
        # Verifica se já existe um ponto no número atual
        if '.' in expressao.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]:#Utilizando split para verificar se o numero apos os operadores ja possui um '.',se ja possuir,não permique que seja adicionado outro
            return  # Não adiciona outro ponto

    expressao += str(num) #Adiciona o numero digitado a expressão como uma string
    display.delete(0,tk.END) #Limpa todo o conteudo na tela
    display.insert(0, expressao) #Insere a expressão atualizada



def addOperacao(op): #Define a função que vai adicionar o sinal que o usuario escolher ao apertar o botão na expressão
    global expressao #Declarando a variavel global dentro da função para que ela possa ser modificada dentro dessa função


    # Verifica se o último caractere já é um operador
    if expressao and expressao[-1] in '+-*/':
        return  # Não adiciona outro operador

    expressao += op #Adiciona o operador digitado na expressão
    display.delete(0, tk.END) #Limpa todo o conteúdo na tela
    display.insert(0, expressao) #Insere a expressão atualizada



def calcular(): #Define a função que irá calcular a expressão final após o usuario apertar o botão de igualdade
    global expressao #Declarando a variavel global dentro da função para que ela possa ser modificada dentro dessa função

    try: #Utilizando um "Try except" para tratamento de erros,caso não ocorra nenhum erro a expressão sera realizada

        #Adicionando uma validação de parenteses para tratamento de erros
        if expressao.count('(') != expressao.count(')'):#Verifica se o numero de '(' é igual ao de ')'
            display.delete(0, tk.END)#Caso sejam diferentes apaga o que esta na tela
            display.insert(0, "ERRO: ( )")#E exibe uma mensagem de erro especifica
            return#Impede que a função continue

        # Verifica se termina com operador
        elif expressao and expressao[-1] in '+-*/':
            display.delete(0, tk.END) #Apaga o que esta na tela
            display.insert(0, "ERRO") #Insere uma mensagem de erro
            return #Não permite com que a função continue

        resultado = str(eval(expressao))  # eval calcula a expressão matemática,essa função executa uma string como um codigo Python
        display.delete(0, tk.END)  # Limpa o display
        display.insert(0, resultado) #Exibe o resultado da expressão
        expressao = resultado  # Mantém o resultado para continuar calculando

    except:#Caso ocorra algum erro como o usuario digitar uma letra no display o programa exxibirá a mensagem de "ERRO" na tela
        display.delete(0, tk.END) # Limpa o display
        display.insert(0, "Erro") # Mostra mensagem de erro
        expressao = "" # Reseta a expressão

def limpar():#Definindo a função que vai limpar a tela caso o botão "C" seja pressionado
    global expressao #Declarando a variavel global dentro da função para que ela possa ser modificada dentro dessa função
    expressao = "" #Limpa a string que estava armazenando a expressão numerica que iria ser calculada
    display.delete(0, tk.END) # Limpa o display
    display.insert(0, "0") #Insere um zero no display(recomeçando o calculo)

def apagar_ultimo():#Definindo a função que vai limpar a célula a esquerda caso o botão "⌫" seja pressionado
    global expressao #Declarando a variável global dentra da função para que ela possa ser modificada dentro dessa função
    expressao = expressao[:-1]  # Remove o último caractere da expressão
    display.delete(0, tk.END)  # Limpa o display
    display.insert(0, expressao if expressao else "0")  # Mostra o restante ou 0 se estiver vazio


root = tk.Tk() #Criando a variavel que vai referenciar a janela principal do programa com o nome rot
root.title("Calculadora Básica") #Criando o titulo da janela
root.geometry("300x500") #Definindo as dimensões da janela

#Criando 6 linhas na grade para posicionar os botões
for i in range(6):
    root.grid_rowconfigure(i, weight=1, minsize=60)  #Definindo o peso e a altura mínima das linhas
#Criando 4 colunas na grade para posicionar os botões
for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=60)  #Definindo o peso e a largura mínima das coluna


#Criando  o display de entrada da calculadora
display = tk.Entry(
    root,
    font=('Arial', 36),
    justify='right', #Alinha números à direita (padrão em calculadoras)
    bd=10)#Cria um "relevo" visual ao redor do display,dando uma impressão de profundidade e sombra

display.insert(0, "0")#Inserindo o numero 0 no display,que seria o ponto inicial da calculadora

#Posicionando e definindo o display digital na janela root
display.grid(
    row=0, #Definindo que ele ficará na linha zero
    column=0, #Definindo que ele ficará na coluna zero
    columnspan=4, #Definindo que ele ocupará 4 colunas(equivalente a todas as colunas dos botões)
    sticky="nsew",#Expande em todas direções (Norte/Sul/Leste/Oeste)
    padx=10,pady=10)# Espaçamento externo: 10px horizontal/vertical

#Criando os botões da calculadora:

#Adicionando o botão com o numero 7 na calculadora
botao7 = tk.Button(
    root, #Definindo em qual janela ele vai aparecer
    text="7", #Definindo o texto que vai aparecer no botão,nesse caso o numero 7
    command=lambda:add_numero(7), #Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 7 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao7.grid(row = 2, column=0) #Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 8 na calculadora
botao8 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="8",#Definindo o texto que vai aparecer no botão,nesse caso o numero 8
    command=lambda:add_numero(8),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 8 como parametro
    height=4,#Definindo a altura do botão
    width=8 #Definindo a largura do botão
)
botao8.grid(row = 2, column = 1)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 9 na calculadora
botao9 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="9",#Definindo o texto que vai aparecer no botão,nesse caso o numero 9
    command=lambda:add_numero(9),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 9 como parametro
    height = 4,#Definindo a altura do botão
    width = 8#Definindo a largura do botão
)
botao9.grid(row=2,column = 2)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de multiplicação na calculadora
botaoMult = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="*",#Definindo o texto que vai aparecer no botão,nesse caso o operador de multiplicação
    command=lambda: addOperacao('*'),#Chamando a função que vai adicionar um operador para a expressão,nesse caso o operador de multiplicação
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoMult.grid(row=2,column = 3)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 4 na calculadora
botao4 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="4",#Definindo o texto que vai aparecer no botão,nesse caso o numero 4
    command=lambda:add_numero(4),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 4 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao4.grid(row=3,column = 0)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 5 na calculadora
botao5 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="5",#Definindo o texto que vai aparecer no botão,nesse caso o numero 5
    command=lambda:add_numero(5),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 5 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao5.grid(row=3,column = 1)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 6 na calculadora
botao6 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="6",#Definindo o texto que vai aparecer no botão,nesse caso o numero 6
    command=lambda:add_numero(6),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 6 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao6.grid(row=3,column = 2)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de subtração da calculadora
botaoSub = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="-",#Definindo o texto que vai aparecer no botão,nesse caso o operador de subtração
    command=lambda: addOperacao('-'),#Chamando a função que vai adicionar um operador para a expressão,nesse caso o operador de subtração
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoSub.grid(row=3,column = 3)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 1 na calculadora
botao1 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="1",#Definindo o texto que vai aparecer no botão,nesse caso o numero 1
    command=lambda:add_numero(1),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 1 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao1.grid(row=4,column = 0)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 2 na calculadora
botao2 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="2",#Definindo o texto que vai aparecer no botão,nesse caso o numero 2
    command=lambda:add_numero(2),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 2 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao2.grid(row=4,column = 1)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 3 na calculadora
botao3 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="3",#Definindo o texto que vai aparecer no botão,nesse caso o numero 3
    command=lambda:add_numero(3),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 3 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao3.grid(row=4,column = 2)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de soma da calculadora
botaoSoma = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="+",#Definindo o texto que vai aparecer no botão,nesse caso o operador de adição
    height = 4,#Definindo a altura do botão
    width = 8,#Definindo a largura do botão
    command=lambda: addOperacao('+')#Chamando a função que vai adicionar um operador para a expressão,nesse caso o operador de adição
)
botaoSoma.grid(row=4,column = 3)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de abrir parenteses na calculadora
botaoAbrirP = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text = "(",#Definindo o texto que vai aparecer no botão,nesse caso o simpolo de abrir parenteses
    command=lambda:add_numero('('),#Chamando a função de adicionar operadores para que o parenteses seja incuido na expressão
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoAbrirP.grid(row=1,column=0)#Definindo a posição do botão no grid criado anteriormente

#Adicionando o botão de fechar parenteses na calculadora
botaoFecharP = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text = ")",#Definindo o texto que vai aparecer no botão,nesse caso o simbolo de fechar parenteses
    command=lambda:add_numero(')'),#Chamando a função de adicionar operadores para que o parenteses seja incuido na expressão
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoFecharP.grid(row=1,column=1)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de limpar a célula á esquerda na calculadora
botaoBackspace = tk.Button(
    root,#Defininido em qual janela ele vai aparecer
    text = "⌫",#Definindo o texto que vai aparecer no botão, nesse caso o simbolo de backspace
    command= apagar_ultimo,#Chamando a função de apagar o último para que seja limpo o campo
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoBackspace.grid(row=1,column=2)#Definindo a posição do botão no grid criado anteriormente

#Adicionando o botão de divisão na calculadora
botaoDiv = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="/",#Definindo o texto que vai aparecer no botão,nesse caso o operador de divisão
    command=lambda: addOperacao('/'),#Chamando a função que vai adicionar um operador para a expressão,nesse caso o operador de divisão
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoDiv.grid(row=1,column = 3)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de cancelar a operação na calculadora
botaoCancel = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="C",#Definindo o texto que vai aparecer no botão,nesse caso a letra C(para cancelar a operação)
    command = limpar,#Chamando a função de limpar a expressão para recomeçar,o cálculo
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoCancel.grid(row=5,column = 0)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão com o número 0 na calculadora
botao0 = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="0",#Definindo o texto que vai aparecer no botão,nesse caso o numero 0
    command=lambda:add_numero(0),#Chamando a função de adicionar um numero na expressão numerica quando esse botão for apertado,passando 0 como parametro
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botao0.grid(row=5,column = 1)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de ponto para numeros decimais na calculadora
botaoPonto = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text=".",#Definindo o texto que vai aparecer no botão,nesse caso o ponto(para numeros quebrados)
    command=lambda:add_numero("."),#Chamando a função de adicionar um ponto na expressão numerica quando esse botão for apertado,para numeros não inteiros
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoPonto.grid(row=5,column = 2)#Definindo aa posição do botão no grid criado anteriormente

#Adicionando o botão de resultado na calculadora
botaoResult = tk.Button(
    root,#Definindo em qual janela ele vai aparecer
    text="=",#Definindo o texto que vai aparecer no botão,nesse caso o simbolo de igualdade(para dar fim ao calculo e exibir  resultado)
    command=calcular,#Chamando a função que vai calcular a expressão final
    height = 4,#Definindo a altura do botão
    width = 8 #Definindo a largura do botão
)
botaoResult.grid(row=5,column = 3)#Definindo aa posição do botão no grid criado anteriormente

root.mainloop() #Criando o loop que mantém a janela aberta