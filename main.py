from typing import Union
from transformers import pipeline, TFAutoModelForSequenceClassification, BertTokenizer
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

modelo = TFAutoModelForSequenceClassification.from_pretrained('./modelo')

tokenizador = BertTokenizer.from_pretrained("./modelo")
clasificador = pipeline('sentiment-analysis', model=modelo, tokenizer=tokenizador)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/submit")
def analizar_sentimiento_hf(entrada: str = Form(...)):
    oraciones = sent_tokenize(entrada, language='spanish')
    oraciones_unidas = unir_oraciones(oraciones)
    resultado = clasificacion(oraciones_unidas)
    suma = 0
    mapeo_sentimientos = {
        '1 star': 1,
        '2 stars': 2,
        '3 stars': 3,
        '4 stars': 4,
        '5 stars': 5
    }
    for i in resultado:
        if i in mapeo_sentimientos:
            suma += mapeo_sentimientos.get(i)
    division = round(suma / len(resultado))
    print()
    dicResultados = {
        1: 'malo',
        2: 'no tan malo',
        3: 'intermedio',
        4: 'bueno',
        5: 'excelente'
    }
    print(oraciones_unidas)
    print(len(oraciones_unidas))
    print(resultado)
    print(division)
    print(suma)
    return dicResultados.get(division)

# Une las oraciones que sean más cortas que 490 caracteres
def unir_oraciones(oraciones):
    i = 0
    while i < len(oraciones) - 1:
        if len(oraciones[i]) < 490 and len(oraciones[i + 1]) < 490:
            oraciones[i] += oraciones[i + 1]
            del oraciones[i + 1]
        else:
            i += 1
    return oraciones

# Clasifica los resultados del array para devolver los valores
def clasificacion(oraciones_unidas):
    arrayresults = []
    for i in oraciones_unidas:
        result = clasificador(i)
        arrayresults.append(result[0]['label'])
    return arrayresults
