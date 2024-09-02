meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "Estar alejado del teclado",
            "GTG": "Tener que irse"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esta palabra no esta en el diccionario o esta mal escrita")
