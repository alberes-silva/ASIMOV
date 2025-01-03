#Coleta de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#Dados necessários
contagem_nome = len(nome)
futura_idade = 5

#Processamento dos dados
print("Olá, ", nome,"!")
print("Seu nome possui ",  contagem_nome, " letras")
print ("Você terá ", idade + futura_idade, " anos daqui a ", futura_idade, " anos")

