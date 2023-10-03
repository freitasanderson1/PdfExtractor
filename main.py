from PyPDF2 import PdfReader
  
reader = PdfReader('EM BEATRIZ RODRIGUES.pdf')
  
totalPaginas = len(reader.pages)
listaCabecalho = ['ESTADO DO TOCANTINS','PREFEITURA MUNICIPAL DE PALMAS','RELAÇÃO DE ALUNOS POR TURMA']

listPaginas = list()

for index in range(totalPaginas):
    page = reader.pages[index]

    text = page.extract_text()

    listaTexto = text.split('\n')

    del listaTexto[0:3]

    print(type(listaTexto))

    print(listaTexto)

    print('\n\n\n\n')


# [print(item) for item in text]