media = int(input("digite sua media: "))
Taxa_de_presenca = int(input("sua taxa de presença: "))

if media >= 6 and Taxa_de_presenca >=75:
    print("voce foi aprovado")
elif Taxa_de_presenca <75:
    print("reprovado")
elif media >=4:
    print('recuperaçao')
else:
    print("voce foi reprovado")
    
