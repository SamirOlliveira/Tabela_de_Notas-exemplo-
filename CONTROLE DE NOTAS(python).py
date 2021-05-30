#!/usr/bin/env python
# coding: utf-8
#RODE ELE DE PREFERÊNCIA NO JUPYTER NOTEBOOK
# In[2]:
def traco():ddd
    print('='*30)


import pandas as pd
# importando biblioteca para dataframe

aluno1 = str(input('digite o nome do aluno: '))
#notas e esquemas, celula de variaveis aluno1
notaPT = str(input('digite a nota de português: '))
notaMT = str(input('digite o nome de matemática: '))
notaCI = str(input('digite o nome de Ciências: '))
notaHT = str(input('digite o nome de História: '))
notaGO = str(input('digite o nome de Geografia: '))

traco()

# In[3]:


aluno2 = str(input('digite o nome do aluno: '))
#notas e esquemas, celula de variaveis alun2
notaPT2 = str(input('digite a nota de português: '))
notaMT2 = str(input('digite o nome de matemática: '))
notaCI2= str(input('digite o nome de Ciências: '))
notaHT2 = str(input('digite o nome de História: '))
notaGO2 = str(input('digite o nome de Geografia: '))

traco()
# In[4]:


aluno3 = str(input('digite o nome do aluno: '))
#notas e esquemas, celula de variaveis aluno3
notaPT3 = str(input('digite a nota de português: '))
notaMT3 = str(input('digite o nome de matemática: '))
notaCI3 = str(input('digite o nome de Ciências: '))
notaHT3 = str(input('digite o nome de História: '))
notaGO3 = str(input('digite o nome de Geografia: '))

traco()
# In[24]:


notasDIC = {'Alunos':[aluno1, aluno2, aluno3], 'Português':[notaPT, notaPT2, notaPT3], 'Matemática':[notaMT, notaMT2, notaMT3], 'Ciências':[notaCI, notaCI2, notaCI3],
            'História':[notaHT, notaHT2, notaHT3], 'Geografia':[notaGO, notaGO2, notaGO3]}
#conversão data frame

notaDF = pd.DataFrame(notasDIC)


# In[27]:


notaDF.rename(columns={'Alunos':'Alunos notas alunos'}) #comando para trocar nome de colunas


# In[ ]:





# In[ ]:





# In[ ]:




