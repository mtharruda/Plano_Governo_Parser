# -*- coding: utf-8 -*-
"""analise_planogoverno_Sorocaba.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f-uirwduWg4IXzz6QIEDi1PaUl6u6ViA

#Preparando o ambiente
Para ler e extrair o arquivo pdf, precisaremos da biblioteca **pyMuPDF**. Leia a documentação [aqui](https://pymupdf.readthedocs.io/en/latest/).
<br>
Também precisaremos da biblioteca **re**, que trabalha com expressões regulares em Python. Com ela, conseguiremos encontrar as palavras dentro do pdf.
<br>
Com a biblioteca **fitz** abriremos nosso pdf.
<br>
Também chamaremos o Pandas, pois foi o melhor (até então) modo que encontrei para dividir o pdf

##Leitura dos dados
"""

!pip install pymupdf
!pip install --force-reinstall pymupdf # Forçar a o kernel reinstalar a biblioteca para termos a versão mais atualizada. Em algumas sessões, tive problemas com a antiga versão.
import pandas as pd
import re
import fitz

pd.set_option('max_colwidth', None)

"""#Leitura dos pdfs"""

#Primeiro vamos ler nosso pdf e passar uma variável para armezená-lo
doc_manga = fitz.open('/content/PLANODEGOVERNOcoligaoSorocabanocorao.pdf')
doc_balas = fitz.open('/content/PlanodeGovernoDaniloBalas20252028vfinal06ago2024envioTSE.pdf')
doc_paulo = fitz.open('/content/5_1722973574181.pdf')
doc_calebe = fitz.open('/content/ProgramaparaasEleicoes2024.pdf')

"""##Loop condicional para armezanar o documento em um dataframe
**Nota:** Importante lembrar que a melhor forma encontrada para analisar o arquivo foi transformando ele em um *dataframe*.

##Rodrigo Manga (Republicanos)
"""

#Passemos, inicialmente, uma lista aberta que receberá os dados extraídos pela biblioteca.
texto = []
for page in doc_manga:
    text = page.get_text()
    print(text)
    texto.append(text)
#Para cada página extraída, iremos "jogar" dentro da lista TEXTO, usando o append.

#Após o loop, criaremos um dataframe com a lista e passaremos o nome da coluna "PLANO".
bd_manga = pd.DataFrame(texto, columns = ["Plano"])

bd_manga

"""##Danilo Balas (PL)"""

#Passemos, inicialmente, uma lista aberta que receberá os dados extraídos pela biblioteca.
texto = []
for page in doc_balas:
    text = page.get_text()
    print(text)
    texto.append(text)
#Para cada página extraída, iremos "jogar" dentro da lista TEXTO, usando o append.

#Após o loop, criaremos um dataframe com a lista e passaremos o nome da coluna "PLANO".
bd_balas = pd.DataFrame(texto, columns = ["Plano"])

"""##Paulinho do Transporte (PT)"""

#Passemos, inicialmente, uma lista aberta que receberá os dados extraídos pela biblioteca.
texto = []
for page in doc_paulo:
    text = page.get_text()
    print(text)
    texto.append(text)
#Para cada página extraída, iremos "jogar" dentro da lista TEXTO, usando o append.

#Após o loop, criaremos um dataframe com a lista e passaremos o nome da coluna "PLANO".
bd_paulo = pd.DataFrame(texto, columns = ["Plano"])

"""##Calebe (PCO)"""

#Passemos, inicialmente, uma lista aberta que receberá os dados extraídos pela biblioteca.
texto = []
for page in doc_calebe:
    text = page.get_text()
    print(text)
    texto.append(text)
#Para cada página extraída, iremos "jogar" dentro da lista TEXTO, usando o append.

#Após o loop, criaremos um dataframe com a lista e passaremos o nome da coluna "PLANO".
bd_calebe = pd.DataFrame(texto, columns = ["Plano"])

"""#Limpeza e ajustes no DataFrame"""

#Podemos notar que o python interpreta a quebra de linha com \n. No entanto, na hora de analisarmos cada string, ele identifica como palavra, não como quebra de linha.
#Para resolver esse problema, precisamos usar o str.replace para remover todos as quebras de linha.
bd_manga['Plano'] = bd_manga['Plano'].str.replace('\n', ' ')
bd_balas['Plano'] = bd_balas['Plano'].str.replace('\n', ' ')
bd_paulo['Plano'] = bd_paulo['Plano'].str.replace('\n', ' ')
bd_calebe['Plano'] = bd_calebe['Plano'].str.replace('\n', ' ')

#x soso

"""#Pesquisa

##Enchentes

###Rodrigo Manga
"""

keywords = input()
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
  print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Enchente|Enchentes"
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_manga['search'] = bd_manga['Plano'].str.contains(keywords, case = False)
bd_manga['Plano'].loc[bd_manga['search'] == True]

"""###Danilo Balas"""

keywords = "Enchente|Enchentes"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
  print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""###Paulinho do Transporte"""

keywords = "Enchente|Enchentes"
for i in bd_paulo:
  contagem = bd_paulo['Plano'].str.count(keywords, re.IGNORECASE)
  print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""###Calebe"""

keywords = "Enchente|Enchentes"
for i in bd_calebe:
  contagem = bd_calebe['Plano'].str.count(keywords, re.IGNORECASE)
  print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""##Queimadas"""

keywords = "Queimada|Queimadas"
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Queimada|Queimadas"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Queimada|Queimadas"
for i in bd_paulo:
  contagem = bd_paulo['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Queimada|Queimadas"
for i in bd_calebe:
  contagem = bd_calebe['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""##Deslizamentos"""

keywords = "Deslizamento"
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Deslizamento"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Deslizamento"
for i in bd_paulo:
  contagem = bd_paulo['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Deslizamento"
for i in bd_calebe:
  contagem = bd_calebe['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""##Crise climática"""

keywords = "Climática"
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_manga['search'] = bd_manga['Plano'].str.contains(keywords, case = False)
bd_manga['Plano'].loc[bd_manga['search'] == True]

keywords = "Climática"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Climática"
for i in bd_paulo:
  contagem = bd_paulo['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_paulo['search'] = bd_paulo['Plano'].str.contains(keywords, case = False)
bd_paulo['Plano'].loc[bd_paulo['search'] == True]

keywords = "Climática"
for i in bd_calebe:
  contagem = bd_calebe['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""##Seca"""

keywords = "Seca|Secas|Estiagem"
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Seca|Secas|Estiagem"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Seca|Secas|Estiagem"
for i in bd_paulo:
  contagem = bd_paulo['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

keywords = "Seca|Secas|Estiagem"
for i in bd_calebe:
  contagem = bd_calebe['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""##Meio ambiente"""

keywords = "meio ambiente"
for i in bd_manga:
  contagem = bd_manga['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_manga['search'] = bd_manga['Plano'].str.contains(keywords, case = False)
bd_manga['Plano'].loc[bd_manga['search'] == True]

keywords = "meio ambiente"
for i in bd_paulo:
  contagem = bd_paulo['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_paulo['search'] = bd_paulo['Plano'].str.contains(keywords, case = False)
bd_paulo['Plano'].loc[bd_paulo['search'] == True]

keywords = "meio ambiente"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_balas['search'] = bd_balas['Plano'].str.contains(keywords, case = False)
bd_balas['Plano'].loc[bd_balas['search'] == True]

keywords = "meio ambiente"
for i in bd_calebe:
  contagem = bd_calebe['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

"""##Guarda Civil Ambiental - plano de governo Balas"""

keywords = "guarda"
for i in bd_balas:
  contagem = bd_balas['Plano'].str.count(keywords, re.IGNORECASE)
print(f"A palavra", keywords, "aparece", contagem.sum(), "vezes no plano de governo")

bd_balas['search'] = bd_balas['Plano'].str.contains(keywords, case = False)
bd_balas['Plano'].loc[bd_balas['search'] == True]