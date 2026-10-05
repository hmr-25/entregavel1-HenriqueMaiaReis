bateria = int(input("Porcentagem atual da bateria (0 a 100): "))
duracao = int(input("Qual a duração da missão (em minutos)? "))
consumo = float(input("Qual o consumo por minuto dos pontos percentuais da bateria: "))

if bateria < 0 or bateria > 100 or duracao <= 0 or consumo <= 0:
    print("Valor inválido")
else:
    consumoPmissao = duracao * consumo

    if consumoPmissao <= bateria:
        batRestante = bateria - consumoPmissao

        print(f"Bateria de {bateria}%, duração de {duracao} minutos e consumo de {consumo} pontos percentuais por minuto resultam em consumo total de {consumoPmissao} pontos percentuais e bateria restante de {batRestante}%.")
    else:
        faltante = consumoPmissao - bateria

        print(f"A missão não pode ser concluída. Faltam {faltante} pontos percentuais de bateria.")