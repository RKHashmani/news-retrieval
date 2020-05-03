/*
TO-DO: Make it so that we can CHOOSE the FIELD to search in. Very Easy fix, leave it for Raheem.
 */

package Searcher;

import Constants.LuceneConstants;
import org.apache.lucene.document.Document;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.CollectionStatistics;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

import java.io.IOException;

public class SearcherMain {

    Searcher searcher;

    public static void main(String[] args) {
        SearcherMain tester;
        try {
            tester = new SearcherMain();
            tester.search("absemt"); // Choose Search Query here. Choose Field below.
        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }
    }

    private void search(String searchQuery) throws IOException, ParseException {
        searcher = new Searcher(LuceneConstants.StopWordsIndexDir);   //Choosing which Index
        long startTime = System.currentTimeMillis();
        TopDocs hits = searcher.search(searchQuery);
        long endTime = System.currentTimeMillis();

        if (hits.totalHits.value == 0) {
            SpellCheckerService spellcheck = new SpellCheckerService();
            spellcheck.suggestWords(searchQuery); // dunno how to expand it for multiterm queries
        } else {
            System.out.println(hits.totalHits.value +
                    " documents found. Time :" + (endTime - startTime));
            for(ScoreDoc scoreDoc : hits.scoreDocs) {
                Document doc = searcher.getDocument(scoreDoc);
                System.out.println("Article: "
                        + doc.get(LuceneConstants.HEADER));
            }
        }
        CollectionStatistics stats = searcher.getStats();
        System.out.println(stats);
    }
}
