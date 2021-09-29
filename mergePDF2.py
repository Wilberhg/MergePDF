from PyPDF2 import PdfFileMerger
from glob import glob
from os import getcwd
from traceback import format_exc
from time import sleep

try:
    print('\nInicializando o programa...')
    varDir = getcwd()
    pdfs = glob(rf'{varDir}\*.pdf')
    print('\nColetando o nome das pastas e dos arquivos...')
    merger = PdfFileMerger(strict=False)
    for pdf in pdfs:
        merger.append(pdf)
    print('\nJuntando os arquivos PDFs...')
    merger.write(rf'{varDir}\RENOMEAR.pdf')
    merger.close()
    print('\nPrograma concluído com êxito!')
    sleep(2.5)
except:
    print('\nO programa apresentou erro e está sendo registrado...')
    sleep(5)
    file = open(rf'{varDir}\ErrorLog.txt', 'a+')
    file.write(format_exc)
    file.close()
