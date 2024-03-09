class Search:
    def search(documents, phrase):
        if phrase == "" or phrase is None:
            return []

        # build inverted index with position
        # key: word, value: set of (doc_id, position)
        inverted_index = {}

        for doc_id, document in documents.items():
            tokens = "".join(
                [c if c.isalnum() or c == " " else "" for c in document.lower()]
            ).split(" ")

            for j, token in enumerate(tokens):
                if token not in inverted_index:
                    inverted_index[token] = set()

                # add (doc_id, position) to the set
                inverted_index[token].add((doc_id, j))

        # search the phrase
        phrase = phrase.lower().split(" ")
        candidates = inverted_index[phrase[0]]
        # print(candidates)

        for i in range(1, len(phrase)):
            phrase_word_indices = (
                inverted_index[phrase[i]] if phrase[i] in inverted_index else set()
            )
            new_candidates = set()
            for doc_id, position in candidates:
                if (doc_id, position + 1) in phrase_word_indices:
                    new_candidates.add((doc_id, position + 1))

            candidates = new_candidates

        return list(set([doc_id for doc_id, _ in candidates]))


# Test cases

if __name__ == "__main__":
    documents = {
        "doc1": "The sky is blue",
        "doc2": "The sun is bright",
        "doc3": "The sun in the sky is bright",
    }
    print(Search.search(documents, "bright"))  # ['doc2', 'doc3']
    print(Search.search(documents, "sun"))  # ['doc2', 'doc3']
    print(Search.search(documents, "sky"))  # ['doc1', 'doc3']
    print(Search.search(documents, "the"))  # ['doc1', 'doc2', 'doc3']
    print(Search.search(documents, "sun in the sky"))  # ['doc3']
    print(Search.search(documents, "blue"))  # ['doc1']
    print(Search.search(documents, "bright sky"))  # []
    print(Search.search(documents, "bright blue sky"))  # []
    print(Search.search(documents, ""))  # []
    print(Search.search(documents, None))  # []
