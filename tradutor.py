# pip install translate

from translate import Translator

Frase = input("Digite a frase/palavra: ")

lingua = input("(Ex: en, pt, uk) \nDiga a lingua de origem: ")
para = input("Traduzir para: ")
s = Translator(from_lang=lingua, # Lingua da frase
    to_lang=para) # Ligua que sera convertida

res = s.translate(Frase) # Fase a ser traduzida
print(res)