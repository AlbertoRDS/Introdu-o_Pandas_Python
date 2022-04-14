import pandas as pd

# Chamando o construtor DataFrame
df = pd.DataFrame()
print(df)

# lista de cordas
lst = ['Geeks', 'For', 'Geeks', 'is',
			'portal', 'for', 'Geeks']

# Chamando o construtor DataFrame na lista
df = pd.DataFrame(lst)
print(df)
