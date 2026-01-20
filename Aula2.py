import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

notas=np.array([7,5,10,8.5,9.5,9])
media_notas=np.mean(notas)
maior_nota=np.max(notas)

print(media_notas)
print(maior_nota)

dados={'nome':['Ana','Beatriz','Carla','Diego'],'idade':[16,17,18,20],'salario':[1000,2000,1515,5000]}
df=pd.DataFrame(dados)
sns.barplot(x='nome',y='salario',data=df)
plt.show()

dados={'idade':[16,17,18,20],'salario':[1000,2000,1515,5000]}
df=pd.DataFrame(dados)
sns.barplot(x='idade',y='salario',data=df)
plt.show()

#comparações

maior_de_idade=df['idade'][3]>=18
bom_salario=df['salario'][3]>=3000

#lógica combinada

adulto_independente=maior_de_idade and bom_salario
joven_dependente=(not maior_de_idade) and (not bom_salario)

#classificações

if adulto_independente:
    print('adulto bem de vida')
elif joven_dependente:
    print('joven sem dinheiro')
else:
    print('nenhuma das opções')
