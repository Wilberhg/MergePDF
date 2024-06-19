import os
from glob import glob

pdfs = glob("*.pdf")

caminho_arquivo = os.getcwd()
gs = os.path.normpath(os.path.join(caminho_arquivo, "gs", "gs10.03.1", "bin", "gswin64c.exe"))
# os.environ["PATH"] = gs

def compress_pdf_file(input_path, output_path):
    import subprocess

    subprocess.call(
        [
            gs,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/printer",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile=" + output_path,
            input_path,
        ]
    )  # To install Ghostscript, use: apt install ghostscript
    return output_path

for pdf in pdfs:
    nome_arqv = os.path.basename(pdf)
    compress_pdf_file(pdf, nome_arqv)
    ...

# for pdf in pdfs:
#     nome_arqv = os.path.basename(pdf)
#     os.system(f'cd /d "{caminho_arquivo}" & pdf_compressor.py -o {nome_arqv} "{pdf}"')