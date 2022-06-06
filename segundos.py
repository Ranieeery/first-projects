Valor = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos_inicio = int(Valor)

dias = segundos_inicio // 86400
resto1 = segundos_inicio % 86400
horas = resto1 // 3600
resto2 = resto1 % 3600
minutos = resto2 // 60
segundos = resto2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")
