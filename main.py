from PyPDF2 import PdfReader
import pandas as pd
import re

reader = PdfReader('EM BEATRIZ RODRIGUES.pdf')

totalPaginas = len(reader.pages)
listaCabecalho = ['ESTADO DO TOCANTINS', 'PREFEITURA MUNICIPAL DE PALMAS', 'RELAÇÃO DE ALUNOS POR TURMA']

df = pd.DataFrame(columns=['Turma', 'Idmatricula', 'Nome'])

listPaginas = list()
turma = None
listaAlunos = list()
for index in range(totalPaginas):
    page = reader.pages[index]

    text = page.extract_text()

    listaTexto = text.split('\n')

    del listaTexto[0:4]

    for linha in listaTexto:
        if "Turma:" in linha:
            turma = linha.split(":")[1].replace('Período letivo','')

        elif "Idmatricula" in linha:
            pass

        elif linha.strip():
            partes = linha.split()
            partes = linha.split('/')
            
            partes2 = partes[0].split(' ')
            
            partes2.pop(0)
            partes2.pop(-1)

            
            # regex totalmente insalubre, nao confie
            matricula = partes2[0]
            partes2.pop(0)
            nome = ' '.join(map(str,partes2))
            aluno_dict = {
                'Turma': turma,
                'Idmatricula': matricula,
                'Nome': nome,
            }
            
            # print(aluno_dict)
            
            listaAlunos.append(aluno_dict)
#             df = pd.concat([df, pd.DataFrame([aluno_dict])], ignore_index=True)

# df.to_csv('alunos.csv', index=False)
