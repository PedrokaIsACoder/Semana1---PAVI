import math

# Função para calcular integral
def CalcularIntegral(F, a, b):
    return F(b) - F(a)                  # Teorema Fundamental do Calculo
    
# f(x) = x^2
def F1(x):
    return (x**3)/3                     # Retornar para o valor da integral
    
# f(x) = sen(x)
def F2(x):
    return -math.cos(x)
  
# f(x) = e^x  
def F3(x):
    return math.exp(x)

# Exibir o valor já com o resultado da integral definida no devido intervalo
print("Integral de x^2 no intervalo [0,1]: ", CalcularIntegral(F1, 0, 1))
print("Integral de sen(x) no intervalo [0,1]: ", CalcularIntegral(F2, 0, math.pi))
print("Integral de e^x no intervalo [0,1]: ", CalcularIntegral(F3, 0, 1))
