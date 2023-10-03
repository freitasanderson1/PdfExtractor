from PyPDF2 import PdfReader
import pandas as pd
import re

reader = PdfReader('EM BEATRIZ RODRIGUES.pdf')

totalPaginas = len(reader.pages)
listaCabecalho = ['ESTADO DO TOCANTINS', 'PREFEITURA MUNICIPAL DE PALMAS', 'RELAÇÃO DE ALUNOS POR TURMA']

df = pd.DataFrame(columns=['Turma', 'Ord.', 'Idmatricula', 'Nome', 'Data de Nascimento', 'Idade', 'Situação Matrícula'])

listPaginas = list()
turma = None

for index in range(totalPaginas):
    page = reader.pages[index]

    text = page.extract_text()

    listaTexto = text.split('\n')

    del listaTexto[0:3]

    for linha in listaTexto:
        if "Turma:" in linha:
            turma = linha.split(":")[1].strip()
        elif linha.strip():
            partes = linha.split()
            ordem = partes[0]
            matricula = partes[1]
            situacao = partes[-1] 
            partes.pop()
            
            if situacao == "REPROVADO" or situacao == "CURSANDO":
                nome_data_idade = ' '.join(partes[2:-1])
            else:
                nome_data_idade = ' '.join(partes[2:])
            
            # regex totalmente insalubre, nao confie
            match = re.search(r'(\d{2}/\d{2}/\d{4}) (\d+ Anos, \d+ Meses e \d+ Dias)', nome_data_idade)
            if match:
                dataNascimento = match.group(1)
                idade = match.group(2)
                nome = nome_data_idade.replace(match.group(0), '').strip()
            else:
                dataNascimento = ''
                idade = ''
                nome = nome_data_idade
            
            aluno_dict = {
                'Turma': turma,
                'Ord.': ordem,
                'Idmatricula': matricula,
                'Nome': nome,
                'Data de Nascimento': dataNascimento,
                'Idade': idade,
                'Situação Matrícula': situacao
            }
            
            df = pd.concat([df, pd.DataFrame([aluno_dict])], ignore_index=True)

df.to_csv('alunos.csv', index=False)
