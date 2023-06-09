""" 
Nome: Camila do Prado Padalino 
RM: 98316
"""

def calculo_delta(a,b,c):
    delta = b ** 2 - 4 * a * c
    equacaoXv = -b / (2 * a)
    equacaoYv = - delta / (4 * a)
    print(f"O X do vértice é {equacaoXv: .2f} \n e o Y do vértice é {equacaoYv: .2f}.") 

    if delta > 0:
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        soma_raizes = x1 + x2
        produto_raizes = x1 * x2
        print(f"A primeira raiz vale: {x1: .2f} e a segunda raiz vale: {x2: .2f}.")
        print(f" A soma das raízes é: {soma_raizes}")
        print(f"O produto das raízes é {produto_raizes}")
    
    elif delta < 0:
        print("Não há raízes, pois o delta é negativo.")
    
    elif delta == 0:
        x = -b / (2 * a)
        print(f'As raízes são iguais, valem: {x}')

    
def grafico_funcao_segundo_grau(a,b,c):
    i = -100
    x = []
    y = []
    while i < 10:
        x.append(i)
        f = a * i ** 2 + b * i + c
        y.append(f)
        i += 1

    print (x)
    print(y)

a = int(input("Insira um valor: "))
b = int(input("Insira um outro valor: "))
c = int(input("Insira um último valor: "))
calculo_delta(a,b,c)
grafico_funcao_segundo_grau(a,b,c)

