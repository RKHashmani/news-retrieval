/*
TO-DO: Make it so that we can CHOOSE the FIELD to search in. Very Easy fix, leave it for Raheem.
 */

package Searcher;

import Constants.LuceneConstants;
import org.apache.lucene.document.Document;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.CollectionStatistics;
import org.apache.lucene.search.Explanation;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

import java.io.IOException;

public class SearcherMain {

    Searcher searcher;

    public static void main(String[] args) {
        SearcherMain tester;
        try {
            tester = new SearcherMain();
            tester.search("Former Tourmaline"); // Choose Search Query here. Choose Field in "Searcher.java" file.
        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }
    }

    private void search(String searchQuery) throws IOException, ParseException {
        searcher = new Searcher(LuceneConstants.StandardIndexDir);   //Choosing which Index
        long startTime = System.currentTimeMillis();
        TopDocs hits = searcher.search(searchQuery);

        float docID = hits.scoreDocs[9].score;
        System.out.println(docID); // DocID of the 0th rank? IDK
        long endTime = System.currentTimeMillis();

        if (hits.totalHits.value == 0) {
            SpellCheckerService spellcheck = new SpellCheckerService();
            spellcheck.suggestWords(searchQuery); // dunno how to expand it for multiterm queries
        } else {
            System.out.println(hits.totalHits.value +
                    " documents found. Time :" + (endTime - startTime));
            int x = 0;
            for(ScoreDoc scoreDoc : hits.scoreDocs) {
                Document doc = searcher.getDocument(scoreDoc);
                System.out.println("Article " + x + ": "
                        + doc.get(LuceneConstants.HEADER) + " (Score: " + hits.scoreDocs[x].score + ")");
                x=x+1;
            }
        }
        CollectionStatistics stats = searcher.getStats();
        System.out.println(stats);
    }
}
