import spacy

nlp = spacy.load("es_core_news_md")


def ner(text):
    doc = nlp(text)

    for ent in doc.ents:
        print(ent)


def pipeline(text):
    docs = nlp.pipe(text)

    for doc in docs:
        print('TEXT', ' LEMMA', ' POS', ' TAG', ' DEPENDENCY', ' SHAPE', ' ALPHA', ' STOP')
        for token in doc:
            print(token.text,
                  token.lemma_,
                  token.pos_,
                  token.tag_,
                  token.dep_,
                  token.shape_,
                  token.is_alpha,
                  token.is_stop)

        for token in doc:
            print(token.text,
                  token.has_vector,
                  token.vector_norm,
                  token.is_oov,
                  token.vector)

        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)

        return doc.ents


def main():
    text = ["Los niños juegan en los Estados Unidos y Jorge los observa. ",
            "Yo bajo con el hombre bajo a tocar el bajo bajo la escalera. ",
            "Yo bajo el volumen."]
    # ner(text)
    pipeline(text)


if __name__ == '__main__':
    main()

# for doc in nlp.pipe(texts, disable=["tagger", "parser"]):
#     # Do something with the doc here
#     print([(ent.text, ent.label_) for ent in doc.ents])
