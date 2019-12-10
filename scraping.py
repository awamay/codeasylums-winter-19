# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:15:58 2019

@author: awani
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

data=convert_pdf_to_txt("C:/Users/awani/Downloads/BIT-Mesra-AWANIKA.pdf")

import logging
import os
import pandas as pd
import re

mail = re.findall("\w+@\w+\.{1}\w+", data)
number = re.findall("^[1-9]\d{9}",data)




