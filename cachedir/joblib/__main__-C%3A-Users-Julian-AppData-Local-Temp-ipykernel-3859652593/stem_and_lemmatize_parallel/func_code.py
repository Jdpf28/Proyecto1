# first line: 1
@memory.cache
def stem_and_lemmatize_parallel(words_list):
    texts = [" ".join(words) for words in words_list]  # Convertir listas de palabras en texto
    stems = [stem_words(words) for words in tqdm(words_list, desc="Aplicando stemming")]
    lemmas = lemmatize_text_parallel(texts)  # Lematización en paralelo
    return [{"stems": stem, "lemas": lema} for stem, lema in zip(stems, lemmas)]
