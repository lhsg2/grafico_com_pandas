import pandas as pd
data = {
    'nome' : ['grylo','bob','wanderson','jô Soares'],
    'idade' : [55,10,70,70],
    'cidade' : ['Brazilandia', 'Valinhos', 'Barão Geraldo', 'São Paulo']
}

df = pd.DataFrame(data)
print(df)