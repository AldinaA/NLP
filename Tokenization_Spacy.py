import spacy
nlp = spacy.load("xx_ent_wiki_sm")
doc = nlp("Pacijent dobio osip po kozi. Ovo je Aldina Avdic")

for token in doc:
    print(token.text,  token.pos_)