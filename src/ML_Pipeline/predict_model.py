import spacy
from ML_Pipeline import text_extractor

# function for prediction
def predict(path):
    #path : of resumes
    output={}
    op=[]
    nlp=spacy.load("model") # load the model
    test_text=text_extractor.convert_pdf_to_text(path) # convert
    print("test_text::",test_text)#
    for text in test_text:
        print("text::",text)
        text=text.replace('\n',' ') # replace
        doc = nlp(text)
        print("doc::",doc)#
        for ent in doc.ents:
            print(f'{ent.label_.upper():{30}}-{ent.text}')
            #why we need label_? label_ converts hashmapping into readable format
            op[ent.label_.upper()]=ent.text
            output.append(op)
            op=[]
    return output
