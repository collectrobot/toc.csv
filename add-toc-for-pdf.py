import fitz
import pprint
import os
import csv

def set_toc(toc):
    pdf=fitz.open('./b.pdf')
    pdf.set_toc(toc)
    # pdf.saveIncr()
    pdf.save('./b2.pdf')
    print("save success")
def read_toc():
    toc=[]
    file=open('./toc.csv')
    tocreader = csv.reader(file, delimiter = '|',quotechar="'")
    offset=41 ## csv中的页号和实际pdf页号的偏差
    for row in tocreader:
        toc.append([int(row[0]),row[1],int(row[2])+offset])
    pprint.pprint(toc)
    return toc

set_toc(read_toc())
