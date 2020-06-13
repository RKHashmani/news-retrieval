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
            tester.search("what are the structural and aeroelastic problems associated with flight\n" +
                    "of high speed aircraft"); // Choose Search Query here. Choose Field in "Searcher.java" file.
        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }
    }

    private void search(String searchQuery) throws IOException, ParseException {
        searcher = new Searcher(LuceneConstants.TestIndexDir);   //Choosing which Index
        long startTime = System.currentTimeMillis();
        TopDocs hits = searcher.search(searchQuery);

        long endTime = System.currentTimeMillis();

        if (hits.totalHits.value == 0) {
            SpellCheckerService spellcheck = new SpellCheckerService();
            spellcheck.suggestWords(searchQuery); // dunno how to expand it for multiterm queries
        } else {
            System.out.println(hits.totalHits.value +
                    " documents found. Time :" + (endTime - startTime));
            int x = 0;
            /*for(ScoreDoc scoreDoc : hits.scoreDocs) {
                Document doc = searcher.getDocument(scoreDoc);
                System.out.println("Article " + x + ": "
                        + doc.get(LuceneConstants.HEADER)
                        + " Date: " + doc.get(LuceneConstants.DATE)
                        + " (Score: " + hits.scoreDocs[x].score + "; Doc: " + hits.scoreDocs[x].doc + ")"
                        // + "\nScore Explanation:\n" + searcher.explanation(hits.scoreDocs[x].doc) //Uncomment if you want score explanation.
                );
             */
            for(ScoreDoc scoreDoc : hits.scoreDocs) {
                Document doc = searcher.getDocument(scoreDoc);
                System.out.println("Article " + x + ": "
                                + " (Score: " + hits.scoreDocs[x].score + "; Doc: " + (hits.scoreDocs[x].doc) + ")"
                                + doc.get(LuceneConstants.CONTENTS)
                        //+ " Date: " + doc.get(LuceneConstants.DATE)

                        // + "\nScore Explanation:\n" + searcher.explanation(hits.scoreDocs[x].doc) //Uncomment if you want score explanation.
                );
                x=x+1;
            }
        }
        CollectionStatistics stats = searcher.getStats();
        System.out.println(stats);
    }
}
