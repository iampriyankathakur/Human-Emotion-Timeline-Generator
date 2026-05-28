from keybert import KeyBERT

kw_model = KeyBERT()

def extract_themes(texts):

    combined_text = " ".join(texts)

    keywords = kw_model.extract_keywords(
        combined_text,
        top_n=5
    )

    return [kw[0] for kw in keywords]
