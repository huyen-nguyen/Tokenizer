import spacy
import json

nlp = spacy.load('en')

with open('extreme.json','r', encoding='utf-8-sig', errors='ignore') as f:
   data = json.load(f)
for d in data:
   doc = nlp(d['description'])
   d["keywords"] = []
   for chunk in doc.noun_chunks:
       d["keywords"].append(chunk.text)

print(json.dumps(data[0]["keywords"][0]))
with open('outputExtreme.json', 'w') as outfile:
   json.dump(data, outfile)