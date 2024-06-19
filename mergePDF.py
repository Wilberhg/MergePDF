from PyPDF2 import PdfMerger
from glob import glob
from os import getcwd, path, makedirs
from shutil import move
from traceback import format_exc
from time import sleep

try:
    print("\nInicializando o programa...")
    varDir = getcwd()
    pdfs = glob(path.normpath(path.join(varDir, "*.pdf")))
    if pdfs:
        print("\nColetando o nome das pastas e dos arquivos...")
        with PdfMerger(strict=False) as merger:
            for pdf in pdfs:
                merger.append(pdf)
            print("\nJuntando os arquivos PDFs...")
            merger.write(path.normpath(path.join(varDir, "RENOMEAR.pdf")))
        diretorio_backup = path.normpath(path.join(varDir, "arquivos_iniciais"))
        makedirs(diretorio_backup)
        for pdf in pdfs:
            move(pdf, diretorio_backup)
    print("\nPrograma concluído com êxito!")
    sleep(2.5)
except:
    print("\nO programa apresentou erro e está sendo registrado...")
    sleep(5)
    with open(path.normpath(path.join(varDir, "ErrorLog.txt")), "a+") as file:
        file.write(format_exc())
