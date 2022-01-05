import pandas as pd
vascudao = pd.read_excel('vascudo.xlsx')
for line in vascudao:
    for colum in line:
        print(colum)
