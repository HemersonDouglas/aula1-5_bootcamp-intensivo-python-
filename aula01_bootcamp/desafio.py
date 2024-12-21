
constante_bonus = 1000

# 1) Solicite ao usuário que digite seu nome

nome_usuario = "Digite seu nome: "
input(nome_usuario)

# 2) Solicite ao usuário que digite o valor do seu saário 

salario = float(input("Digite o valor do seu salário: "))


# 3) Solicite ao usuário que digite o valor do bônus recebido

bonus_recebido = float(input("Digite o seu bônus: "))


# 4) Calcule o valor do bônus final 

valor_bonus = constante_bonus + salario * bonus_recebido


# 5) Imprima cálculo do KPI para o usuário

print(f"O usuário {nome_usuario} possui o bonus de {valor_bonus}")