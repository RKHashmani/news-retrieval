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

    private final String indexDir;
    Searcher searcher;
    public SearcherMain(String indexDir) {
        this.indexDir = indexDir;
    }

    public String search(String searchQuery) throws IOException, ParseException {
        searcher = new Searcher(indexDir);
        long startTime = System.currentTimeMillis();
        TopDocs hits = searcher.search(searchQuery);

        long endTime = System.currentTimeMillis();

        if (hits.totalHits.value == 0) {
            SpellCheckerService spellcheck = new SpellCheckerService();
            return spellcheck.suggestWords(searchQuery); // dunno how to expand it for multiterm queries
        } else {
            String message = "\n\n" + hits.totalHits.value +
                    " documents found. Time :" + (endTime - startTime);
            int x = 0;
            for(ScoreDoc scoreDoc : hits.scoreDocs) {
                Document doc = searcher.getDocument(scoreDoc);
                message += "\n\nArticle " + x + ":\n"
                        + doc.get(LuceneConstants.HEADER)
                        + "\nDate: " + doc.get(LuceneConstants.DATE)
                        + " (Score: " + hits.scoreDocs[x].score + "; Doc: " + doc.get("id") + ")";
                        //+ "\nScore Explanation:\n" + searcher.explanation(hits.scoreDocs[x].doc) //Uncomment if you want score explanation.
                x=x+1;
            }
            CollectionStatistics stats = searcher.getStats();
            System.out.println(stats);
            System.out.println(message);
            return message;
        }

        // For Cranfield Output. For evaluation purposes. Do not delete yet.

        /*
        } else {
            System.out.println(hits.totalHits.value +
                    " documents found. Time :" + (endTime - startTime));
            int x = 0;
            for(ScoreDoc scoreDoc : hits.scoreDocs) {
                Document doc = searcher.getDocument(scoreDoc);
                System.out.println("Article " + x + ": "
                                + " (Doc: " + doc.get("id") + ") "
                                + doc.get(LuceneConstants.CONTENTS)
                        //+ " Date: " + doc.get(LuceneConstants.DATE)

                        // + "\nScore Explanation:\n" + searcher.explanation(hits.scoreDocs[x].doc) //Uncomment if you want score explanation.
                );
                x=x+1;
            }
        }
        */
    }
}
