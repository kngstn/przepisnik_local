#import pdf2txt
import os
import functions as fnc


##  global varibles

pdf_dir="/home/bartosz/Pulpit/przepisnik/local/pdfs/"
txt_dir="/home/bartosz/Pulpit/przepisnik/local/txt_outputs/"


if __name__ == "__main__":

    fnc.pdfToTxt(pdf_dir,txt_dir)


    # pdfFileObj = open(filename,'rb')
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # num_pages = pdfReader.numPages
    # count = 0
    # text = ""

    # while count < num_pages:
    #     pageObj = pdfReader.getPage(count)
    #     count +=1
    #     text += pageObj.extractText()

    # if text != "":
    #     text = text

    # else:
    #     text = textract.process(fileurl, method='tesseract', language='eng')



    # with open("newtxt.txt","wb") as txt:
    #     txt.write(text.encode(encoding='utf-8'))    

    # #print(text.encode(encoding='utf-8'))    
    

    # pdfFileObj.close()
