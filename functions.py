import os
import subprocess

def funcname(self, parameter_list):
    
    pass

def pdfToTxt(pdf_dir,txt_dir):
    
    pdf_filenames = os.listdir(pdf_dir)
    txt_filenames = [x[:-4] + ".txt" for x in pdf_filenames]

    #print(txt_filenames)
    #attributes_for_pdf2txt = " -o {} -t text {}"

    for x,y in zip(txt_filenames,pdf_filenames):
        subprocess.call(["pdf2txt.py", "-o", txt_dir+x, pdf_dir+y])


    
