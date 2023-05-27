import pandas as pd
import math

df = pd.read_csv('Result_22Mar_S1_g1.csv')

for i in range (5, 40):
    total = 0;
    for x in df.iterrows
        total = total + df.iat[x, i]

    Mean = total/26131;
    total = 0

    for x in df.iterrows
        total = total + (df.iat[x, i] - Mean)**2

    SD = math.sqrt(total/26131)
    total = 0

    for x in df.iterrows
        total = total + (df.iat[x, i] - Mean)/SD

    Z = total/26131
    total = 0

    print(Mean, SD, Z)