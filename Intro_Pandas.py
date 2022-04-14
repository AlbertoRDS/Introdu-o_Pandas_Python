import pandas as pd
import numpy as np


# Criando séries vazias
ser = pd.Series()

print(ser)

# matriz simples
data = np.array(['g', 'e', 'e', 'k', 's'])

ser = pd.Series(data)
print(ser)
