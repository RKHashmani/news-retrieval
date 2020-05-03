package Searcher;

import Constants.LuceneConstants;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.search.spell.PlainTextDictionary;
import org.apache.lucene.search.spell.SpellChecker;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.File;
import java.io.IOException;

public class SpellCheckerService {

    Directory directory;
    SpellChecker spellChecker;

    public SpellCheckerService() throws IOException {
        directory = FSDirectory.open(new File(LuceneConstants.SPELLCHECKER).toPath());
        spellChecker = new SpellChecker(directory);
        spellChecker.indexDictionary(new PlainTextDictionary(new File(LuceneConstants.DICTIONARY).toPath()),
                new IndexWriterConfig(), true);
    }

    public void suggestWords(String wordForSuggestions) throws IOException {
        String[] suggestions = spellChecker.suggestSimilar(wordForSuggestions, LuceneConstants.suggestionsNumber);

        if (suggestions!=null && suggestions.length>0) {
            for (String word : suggestions) {
                System.out.println("Did you mean:" + word);
            }
        }
        else {
            System.out.println("No suggestions found for word:"+wordForSuggestions);
        }
    }
}
