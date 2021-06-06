#! python3

import docx

def get_text(filename):
    doc = docx.Document(filename)
    fulltext = []
    for par in doc.paragraphs:
        fulltext.append(par.text)
    return '\n'.join(fulltext)
