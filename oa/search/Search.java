import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Search {

    public List<Integer> search(List<Pair<Integer, String>> documents, String phrase) {
        if (phrase == null || phrase.length() == 0) {
            return new ArrayList<>();
        }

        // Build inverted index with position
        // key: word, value: set of (docId, position)
        Map<String, Set<Pair<Integer, Integer>>> invertedIndex = new HashMap<>();
        // populate each document
        for (Pair<Integer, String> document : documents) {
            Integer docId = document.getKey();
            String text = document.getValue().replaceAll("[.,!]", "").toLowerCase();
            String[] words = text.split(" ");
            for (int j = 0; j < words.length; j++) {
                invertedIndex.computeIfAbsent(words[j], k -> new HashSet<>()).add(new Pair<>(docId, j));
            }
        }

        // search process
        // Populate candidates from first word index lookup
        String[] phraseWords = phrase.toLowerCase().split(" ");
        Set<Pair<Integer, Integer>> candidates = invertedIndex.getOrDefault(phraseWords[0], new HashSet<>());

        for (int i = 1; i < phraseWords.length; i++) {
            Set<Pair<Integer, Integer>> phraseWordIdx = invertedIndex.getOrDefault(phraseWords[i], new HashSet<>());
            Set<Pair<Integer, Integer>> newCandidates = new HashSet<>();
            for (Pair<Integer, Integer> pair : candidates) {
                Pair<Integer, Integer> nextWordIdx = new Pair<>((pair.getKey()), pair.getValue() + 1);
                if (phraseWordIdx.contains(nextWordIdx)) {
                    newCandidates.add(nextWordIdx);
                }
            }
            candidates = newCandidates;
        }

        Set<Integer> matchingDocuments = new HashSet<>();
        for (Pair<Integer, Integer> wordIdx : candidates) {
            matchingDocuments.add(wordIdx.getKey());
        }

        return new ArrayList<>(matchingDocuments);
    }

}