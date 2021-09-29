from PyPDF2 import PdfFileMerger
import glob
pdfs = glob.glob(r'D:\PDF\*.pdf')
merger = PdfFileMerger(strict=False)
for pdf in pdfs:
    merger.append(pdf)
merger.write(r'D:\PDF\PranchaFinal.pdf')
merger.close()
