import collections


# <word, dict[doc_id, idx[]]>
class Process:
    def __init__(self, data):
        self.data = data
        self.memo = collections.defaultdict(dict)
        for doc_id in data:
            cleaned_data = ""
            for char in data[doc_id]:
                if char.isalnum() or char.isspace():
                    cleaned_data += char.lower()
            cleaned_data = cleaned_data.split()
            self.data[doc_id] = cleaned_data
            for idx, word in enumerate(cleaned_data):
                if doc_id in self.memo[word]:
                    self.memo[word][doc_id].append(idx)
                else:
                    self.memo[word][doc_id] = [idx]

    def search(self, phrase):
        res = []
        phrase = phrase.lower().split()
        candidates = self.memo[phrase[0]]
        phase_word_index = 1
        while len(candidates) != 0 and phase_word_index < len(phrase):
            new_candidates = collections.defaultdict(list)
            for doc_id in candidates:
                for idx in candidates[doc_id]:
                    if (
                        idx + 1 < len(self.data[doc_id])
                        and self.data[doc_id][idx + 1] == phrase[phase_word_index]
                    ):
                        new_candidates[doc_id].append(idx + 1)
            candidates = new_candidates
            phase_word_index += 1
        return candidates.keys()
