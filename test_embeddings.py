"""
Quick sanity check: does a multilingual embedding model actually cluster
Gurmukhi Japji Sahib content by CONCEPT the way we need it to?

This tests cross-lingual alignment specifically for Gurmukhi/Punjabi --
an English concept query should land closest to the pauri that's
actually about that concept, not just share surface words.

Run this in an environment with network access to your chosen embedding
provider. Fill in EMBED() with whichever you want to test first --
starter code for a few common options is below.
"""

import numpy as np

# ---------------------------------------------------------------------
# 1. The test set: real Gurmukhi passages from the Japji Sahib skill,
#    each tagged with what it's actually "about" so we can check if
#    the right one comes back for each query.
# ---------------------------------------------------------------------

PASSAGES = {
    "pauri_2": {
        "text": (
            "ਹੁਕਮੀ ਹੋਵਨਿ ਆਕਾਰ ਹੁਕਮੁ ਨ ਕਹਿਆ ਜਾਈ ॥ "
            "ਹੁਕਮੀ ਹੋਵਨਿ ਜੀਅ ਹੁਕਮਿ ਮਿਲੈ ਵਡਿਆਈ ॥ "
            "ਹੁਕਮੀ ਉਤਮੁ ਨੀਚੁ ਹੁਕਮਿ ਲਿਖਿ ਦੁਖ ਸੁਖ ਪਾਈਅਹਿ ॥ "
            "ਹੁਕਮੈ ਅੰਦਰਿ ਸਭੁ ਕੋ ਬਾਹਰਿ ਹੁਕਮ ਨ ਕੋਇ ॥ "
            "ਨਾਨਕ ਹੁਕਮੈ ਜੇ ਬੁਝੈ ਤ ਹਉਮੈ ਕਹੈ ਨ ਕੋਇ ॥੨॥"
        ),
        "about": "Hukam (divine order/will), fate vs free will, ego dissolving through understanding Hukam",
    },
    "pauri_18": {
        "text": (
            "ਅਸੰਖ ਮੂਰਖ ਅੰਧ ਘੋਰ ॥ ਅਸੰਖ ਚੋਰ ਹਰਾਮਖੋਰ ॥ "
            "ਅਸੰਖ ਪਾਪੀ ਪਾਪੁ ਕਰਿ ਜਾਹਿ ॥ ਅਸੰਖ ਕੂੜਿਆਰ ਕੂੜੇ ਫਿਰਾਹਿ ॥ "
            "ਵਾਰਿਆ ਨ ਜਾਵਾ ਏਕ ਵਾਰ ॥ ਜੋ ਤੁਧੁ ਭਾਵੈ ਸਾਈ ਭਲੀ ਕਾਰ ॥ "
            "ਤੂ ਸਦਾ ਸਲਾਮਤਿ ਨਿਰੰਕਾਰ ॥੧੮॥"
        ),
        "about": "the countless sinners, fools, thieves and liars in creation, and total surrender to God's will regardless",
    },
    "pauri_1": {
        "text": (
            "ਸੋਚੈ ਸੋਚਿ ਨ ਹੋਵਈ ਜੇ ਸੋਚੀ ਲਖ ਵਾਰ ॥ "
            "ਚੁਪੈ ਚੁਪ ਨ ਹੋਵਈ ਜੇ ਲਾਇ ਰਹਾ ਲਿਵ ਤਾਰ ॥ "
            "ਭੁਖਿਆ ਭੁਖ ਨ ਉਤਰੀ ਜੇ ਬੰਨਾ ਪੁਰੀਆ ਭਾਰ ॥ "
            "ਹੁਕਮਿ ਰਜਾਈ ਚਲਣਾ ਨਾਨਕ ਲਿਖਿਆ ਨਾਲਿ ॥੧॥"
        ),
        "about": "ritual purity, silent meditation, and worldly hunger cannot achieve truth on their own -- only living by Hukam does",
    },
}

# Concept queries phrased the way an English-speaking kid might actually ask.
# expected = which passage SHOULD be the best match.
QUERIES = [
    {"query": "What does Japji say about fate and free will?", "expected": "pauri_2"},
    {"query": "Where does it talk about ego?", "expected": "pauri_2"},
    {"query": "What does it say about bad or sinful people?", "expected": "pauri_18"},
    {"query": "Can rituals like washing or staying silent make you pure?", "expected": "pauri_1"},
    {"query": "What happens when you truly understand God's will?", "expected": "pauri_2"},
]

# ---------------------------------------------------------------------
# 2. Plug in your embedding provider here. Uncomment ONE of these.
# ---------------------------------------------------------------------

def embed_openai(texts):
    from openai import OpenAI
    client = OpenAI()  # needs OPENAI_API_KEY in env
    resp = client.embeddings.create(model="text-embedding-3-large", input=texts)
    return [d.embedding for d in resp.data]

def embed_cohere(texts, input_type="search_document"):
    import cohere
    co = cohere.Client()  # needs COHERE_API_KEY in env
    resp = co.embed(
        texts=texts,
        model="embed-multilingual-v3.0",
        input_type=input_type,
    )
    return resp.embeddings

def embed_voyage(texts, input_type="document"):
    import voyageai
    vo = voyageai.Client()  # needs VOYAGE_API_KEY in env
    resp = vo.embed(texts, model="voyage-3", input_type=input_type)
    return resp.embeddings

def embed_sentence_transformers(texts):
    # Free, local, no API key -- good first thing to try.
    # pip install sentence-transformers
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("intfloat/multilingual-e5-large")
    # e5 models expect a "query: " / "passage: " prefix convention
    return model.encode(texts, normalize_embeddings=True)

# --- CHOOSE ONE ---
EMBED = embed_sentence_transformers
# EMBED = embed_openai
# EMBED = embed_cohere
# EMBED = embed_voyage

# ---------------------------------------------------------------------
# 3. Run the test
# ---------------------------------------------------------------------

def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def main():
    keys = list(PASSAGES.keys())
    passage_texts = [PASSAGES[k]["text"] for k in keys]
    passage_vecs = EMBED(passage_texts)

    query_texts = [q["query"] for q in QUERIES]
    query_vecs = EMBED(query_texts)

    correct = 0
    print(f"{'Query':<55} {'Expected':<10} {'Got':<10} {'Score':<7} {'Match?'}")
    print("-" * 95)
    for q, qvec in zip(QUERIES, query_vecs):
        sims = [(k, cosine_sim(qvec, pv)) for k, pv in zip(keys, passage_vecs)]
        sims.sort(key=lambda x: -x[1])
        best_key, best_score = sims[0]
        is_correct = best_key == q["expected"]
        correct += is_correct
        print(f"{q['query']:<55} {q['expected']:<10} {best_key:<10} {best_score:<7.3f} {'YES' if is_correct else 'no'}")
        # show runner-up too, useful when it's close
        if len(sims) > 1:
            print(f"    (runner-up: {sims[1][0]} @ {sims[1][1]:.3f})")

    print("-" * 95)
    print(f"Score: {correct}/{len(QUERIES)} correct top-match")
    print()
    print("Read this as a smoke test, not a verdict: 5 queries is not enough to")
    print("fully trust a model, but a model that fails badly here (getting most")
    print("wrong, or all queries landing suspiciously close to the same score)")
    print("is a strong signal to try a different model before building on it.")

if __name__ == "__main__":
    main()
